# 兑换与闪兑 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### EXCHANGE-001 · 币币-兑换-兑换档位配置 

- 接口声明：`GET /config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/exchange.py:51` · `AssetExchangeConfigResource`

### EXCHANGE-002 · 币币-兑换-兑换档位配置-修改 

- 接口声明：`PUT /config`
- 输入字段：`configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/exchange.py:67` · `AssetExchangeConfigResource`

### EXCHANGE-003 · 币币-兑换-市场兑换档位 

- 接口声明：`GET /market-depths`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/exchange.py:120` · `AssetExchangeMarketsResource`

### EXCHANGE-004 · 币币-兑换-兑换订单列表 

- 接口声明：`GET /orders`
- 输入字段：`start`, `end`, `user_id`, `source_asset`, `target_asset`, `status`, `result`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/exchange.py:158` · `AssetExchangeOrderListResource`

### EXCHANGE-005 · 币币-兑换-系统兑换订单列表 

- 接口声明：`GET /sys-orders`
- 输入字段：`exchange_order_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/exchange.py:230` · `SysAssetExchangeOrderListResource`

### EXCHANGE-006 · 币币-兑换-系统兑换订单-挂单历史 

- 接口声明：`GET /sys-trade-orders`
- 输入字段：`sys_order_id`, `status`, `has_deal`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/exchange.py:277` · `SysAssetExchangeTradeOrderListResource`

### EXCHANGE-007 · 币币-兑换-兑换排名 

- 接口声明：`GET /asset-pair-rank`
- 输入字段：`start_time`, `end_time`, `time_type`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/exchange.py:33` · `DailyAssetExchangeAssetPairReportResource`

### EXCHANGE-008 · 报表-兑换报表-全站报表 

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/exchange.py:214` · `DailyAssetExchangeSiteReportResource`

### EXCHANGE-009 · 报表-兑换报表-币种报表 

- 接口声明：`GET /asset-report`
- 输入字段：`report_type`, `asset`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/exchange.py:309` · `DailyAssetExchangeAssetReportResource`

### EXCHANGE-010 · 报表-兑换报表-币种详情报表 

- 接口声明：`GET /asset-detail-report`
- 输入字段：`report_type`, `report_date`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/exchange.py:401` · `DailyAssExcAssDetailReportResource`

### EXCHANGE-011 · 资产报表-竞品币种-上币速度

- 接口声明：`GET /online-report`
- 输入字段：`asset`, `status`, `rank`, `exchange`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/exchanges_assets.py:61` · `AssetOnlineReportResource`

### EXCHANGE-012 · 资产报表-竞品币种-交易额

- 接口声明：`GET /trade-report`
- 输入字段：`asset`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/exchanges_assets.py:199` · `AssetTradeReportResource`

### EXCHANGE-013 · 资产报表-竞品币种-交易额-异步下载

- 接口声明：`GET /trade-report/async-download`
- 输入字段：`start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/exchanges_assets.py:293` · `AssetTradeReportAsyncDownloadResource`

### EXCHANGE-014 · 返回可见的兑换币种列表（下拉列表） 

- 接口声明：`GET /visible-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:154` · `AssetExchangeVisibleAssetsResource`

### EXCHANGE-015 · 返回支持的兑换币种数组列表，不包括目标币种、最大兑换市值 

- 接口声明：`GET /available-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:166` · `AssetExchangeAvailableAssetsResource`

### EXCHANGE-016 · 支持的兑换币种列表，已废弃，兼容老版本APP保留 

- 接口声明：`GET /assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:178` · `AssetExchangeAssetsResource`

### EXCHANGE-017 · 根据源币种 获取支持兑换的 目标币种列表 

- 接口声明：`GET /target-assets`
- 输入字段：`source_asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:191` · `ExchangeTargetAssetsResource`

### EXCHANGE-018 · 获取兑换路径 

- 接口声明：`GET /path`
- 输入字段：`source_asset`, `target_asset`, `restricted`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:213` · `AssetExchangePathResource`

### EXCHANGE-019 · 预览兑换订单路径（提前计算兑换路径） 

- 接口声明：`POST /preview`
- 输入字段：`source_asset`, `target_asset`, `source_asset_amount`
- 显式控制：require_login; trade_permission_validate(is_spot=True, account_id=0)
- 代码依据：`app/api/frontend/exchange.py:265` · `AssetExchangeOrderPreviewResource`

### EXCHANGE-020 · 提交兑换订单 

- 接口声明：`POST /orders`
- 输入字段：`source_asset`, `target_asset`, `source_asset_amount`
- 显式控制：require_login; lock_request(with_user=True); trade_permission_validate(is_spot=True, account_id=0)
- 代码依据：`app/api/frontend/exchange.py:452` · `AssetExchangeOrdersResource`

### EXCHANGE-021 · 兑换订单列表 

- 接口声明：`GET /orders`
- 输入字段：`source_asset`, `target_asset`, `status`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/exchange.py:533` · `AssetExchangeOrdersResource`

### EXCHANGE-022 · 兑换订单明细 

- 接口声明：`GET /orders/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/exchange.py:602` · `AssetExchangeOrderDetailResource`

### EXCHANGE-023 · 热门兑换榜 

- 接口声明：`GET /rank`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:688` · `AssetExchangeRankResource`

### EXCHANGE-024 · 热门目标币种榜 

- 接口声明：`GET /rank/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:701` · `AssetExchangeAssetRankResource`

### EXCHANGE-025 · 兑换币种榜 

- 接口声明：`GET /rank/assets/<string:direction>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/exchange.py:716` · `AssetExchangeAssetRankByDirectionResource`

### EXCHANGE-026 · 返回支持的兑换币种数组列表 

- 接口声明：`GET /ccys`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/assets/swap.py:38` · `SwapAssetsResource`

### EXCHANGE-027 · 根据源币种 获取支持兑换的 目标币种列表 

- 接口声明：`GET /target-ccys`
- 输入字段：`source_ccy`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/assets/swap.py:49` · `SwapTargetAssetsResource`

### EXCHANGE-028 · 询价 

- 接口声明：`GET /quote`
- 输入字段：`source_ccy`, `target_ccy`, `source_ccy_amount`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/swap.py:85` · `SwapQuoteResource`

### EXCHANGE-029 · 提交兑换订单 

- 接口声明：`POST /orders`
- 输入字段：`source_ccy`, `target_ccy`, `source_ccy_amount`, `client_id`
- 显式控制：require_api_v2_auth(require_trading_permission=True); lock_request(with_user=True)
- 代码依据：`app/api/v2/assets/swap.py:202` · `SwapOrdersResource`

### EXCHANGE-030 · 查询兑换订单 

- 接口声明：`GET /orders`
- 输入字段：`swap_id`, `source_ccy`, `target_ccy`, `status`, `start_time`, `end_time`, `client_id`, `page`, `limit`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/swap.py:286` · `SwapOrdersResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/v2/test_swap.py`
- `tests/business/test_summary_exchange_trade_users.py`
- `tests/business/test_third_exchange.py`
- `tests/schedules/test_country_user_report_exchange_history.py`
- `tests/schedules/test_user_business_record_exchange.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
