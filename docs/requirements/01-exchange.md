# 兑换与闪兑 · 现状需求草稿

> 由代码反推，尚未经过产品确认。业务规则以索引中的代码快照为依据；未执行交易或业务测试。
> 整理基线：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`。后续代码更新不会自动改写本文，需重新评审。

## 目标与使用对象

推断目标：支持调用方查询可兑换币种、获取报价、提交兑换订单并查看结果。代码注释指出这组 API 用于 ViaWallet 和矿池，是否仍保持该开放范围需产品确认。

依据：`app/api/v2/assets/swap.py` 的模块说明及 `SwapAssetsResource`、`SwapTargetAssetsResource`。

## 已实现规则

### EX-01 · 兑换币种与数量范围

- 支持查询可兑换币种，以及根据源币种查询目标币种。
- 目标币种查询中，源币种为 USDT 时最小量使用 1，否则读取资产配置的最小下单量。
- 最大量由目标配置的最大美元金额除以源资产美元价格得到；价格缺失时该分支使用零值。
- 上述行为仅对应目标币种列表计算，不能直接推断订单校验的全部规则。

依据：`app/api/v2/assets/swap.py` · `SwapTargetAssetsResource._get`。

### EX-02 · 询价

- 询价要求 API v2 鉴权，输入源币种、目标币种和正数源数量。
- 源币种等于目标币种时拒绝；没有可用兑换路径时返回参数错误。
- 当前分支支持一条或两条市场组成的路径，优先选择缓存中深度足够的路径。
- 有报价时按 taker 费率及路径市场数量计算手续费估算，目标数量和费用进行精度处理。
- 报价格式中，大于 1 的价格保留四位小数；其他非零价格使用有效数字处理函数。最终精度细节应继续核查该函数。

依据：`app/api/v2/assets/swap.py` · `SwapQuoteResource.get`、`format_swap_price`。

### EX-03 · 提交订单

- 提交要求交易权限，并通过用户维度请求锁限制并发。
- 用户未开启 2FA 时抛出 `TwoFactorAuthenticationRequired`。
- `client_id` 为可选字符串，声明最大长度 64；有值时保存与兑换订单的映射。
- 创建订单后投递异步处理任务；接口返回创建结果不代表兑换已完成。
- 本层记录 `client_id` 不能证明全链路具备幂等保证，需要继续核查创建订单与存储实现。

依据：`app/api/v2/assets/swap.py` · `SwapOrdersResource.post`；`tests/api/v2/test_swap.py` · `test_swap_order_rejects_concurrent_request_for_same_user`。

### EX-04 · 状态展示与查询

- 订单查询按当前用户过滤，可叠加订单编号、源/目标币种、状态、时间、client_id 和分页条件。
- 底层非 FAILED/FINISHED 状态对外归为 PROCESSING。
- 底层 FINISHED 且目标成交量为零时，格式化响应将状态显示为 FAILED。
- 查询 FINISHED 使用底层 FINISHED 条件，因此“查询条件”和“展示状态”存在需产品确认的边界。
- 结果字段包含实际成交、退款数量、目标数量、费用和 client_id；目标实际数量包含针对特定费用类型的扣减逻辑，并限制不小于零。

依据：`app/api/v2/assets/swap.py` · `SwapOrdersResource.get`、`format_order`；`tests/api/v2/test_swap.py` · `test_swap_orders_filters_finished_status`。

## 验收用例建议（未执行）

| 编号 | 场景 | 预期及依据 |
|---|---|---|
| EX-T01 | 相同源/目标币种询价 | 根据询价分支拒绝 |
| EX-T02 | 无 2FA 提交订单 | 抛出 2FA 必需错误 |
| EX-T03 | 同用户并发提交，锁获取失败 | 拒绝后不创建订单；现有测试包含该断言 |
| EX-T04 | 查询 FINISHED | 查询包含底层 FINISHED 条件；已有对应测试 |
| EX-T05 | FINISHED 且目标量为零 | 返回展示状态 FAILED；同时核对产品预期 |
| EX-T06 | client_id 超过 64 字符 | 字段校验拒绝，具体错误响应需验证 |
| EX-T07 | 外部成交延迟或异步投递失败 | 预期尚未确认，需要补充重试与补偿规则 |

## 待产品/研发确认

- 报价有效期、价格波动容忍、实际成交与询价差异如何解释？
- client_id 是否要求幂等？跨端重试如何处理？
- 订单状态过滤与展示状态不一致是否属于预期兼容行为？
- 异步执行失败后的补偿和资金最终一致性需要哪些额外服务证据？
