# 合约业务 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### PERPETUAL-001 · 运营-合约专题页-活动列表

- 接口声明：`GET /activities`
- 输入字段：`status`, `name`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:37` · `PerpetualSpecialListResource`

### PERPETUAL-002 · 运营-合约专题页-创建活动

- 接口声明：`POST /activities`
- 输入字段：`name`, `start_at`, `end_at`, `activity_count`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:89` · `PerpetualSpecialListResource`

### PERPETUAL-003 · 运营-合约专题页-修改活动

- 接口声明：`PUT /activities`
- 输入字段：`id`, `name`, `start_at`, `end_at`, `activity_count`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:115` · `PerpetualSpecialListResource`

### PERPETUAL-004 · 运营-活动-合约专题页-活动标题模板

- 接口声明：`GET /activities/perpetual/special/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:160` · `PerpetualSpecialTemplateResource`

### PERPETUAL-005 · 运营-活动-合约专题页-导入活动标题模板

- 接口声明：`POST /activities/perpetual/special/template-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:176` · `PerpetualSpecialUploadResource`

### PERPETUAL-006 · 运营-合约专题页-获取活动详情

- 接口声明：`GET /activities/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:244` · `PerpetualSpecialActivityResponse`

### PERPETUAL-007 · 运营-合约专题页-保存活动详情

- 接口声明：`POST /activities/<int:id_>`
- 输入字段：`jump_type`, `jump_id`, `daylight_file_key`, `night_file_key`, `rtl_daylight_file_key`, `rtl_night_file_key`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:309` · `PerpetualSpecialActivityResponse`

### PERPETUAL-008 · 运营-合约专题页-修改活动详情

- 接口声明：`PUT /activities/<int:id_>`
- 输入字段：`activity_id`, `jump_type`, `jump_id`, `daylight_file_key`, `night_file_key`, `rtl_daylight_file_key`, `rtl_night_file_key`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:354` · `PerpetualSpecialActivityResponse`

### PERPETUAL-009 · 运营-合约专题页-修改状态

- 接口声明：`POST /activities/<int:id_>/status`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/perpetual_topic.py:430` · `SpecialActivityUpdateStatusResource`

### PERPETUAL-010 · 市场信息

- 接口声明：`GET /markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:68` · `MarketData`

### PERPETUAL-011 · 永续深度成交-深度列表

- 接口声明：`GET /depth`
- 输入字段：`market`, `side`, `order_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:102` · `DepthList`

### PERPETUAL-012 · 永续深度成交-最新成交

- 接口声明：`GET /latest-deals`
- 输入字段：`market`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:142` · `LatestDeals`

### PERPETUAL-013 · 永续-交易排名-实时净买卖

- 接口声明：`GET /realtime-net-rank`
- 输入字段：`market`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:172` · `RealtimeNetRank`

### PERPETUAL-014 · 永续-交易排名-实时成交量

- 接口声明：`GET /realtime-deal-rank`
- 输入字段：`market`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:240` · `RealtimeDealRank`

### PERPETUAL-015 · 永续-交易排名-历史净买卖

- 接口声明：`GET /history-net-rank`
- 输入字段：`market`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:317` · `HistoryNetRank`

### PERPETUAL-016 · 永续-交易排名-历史成交量

- 接口声明：`GET /history-deal-rank`
- 输入字段：`market`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:426` · `HistoryDealRank`

### PERPETUAL-017 · 永续-交易排名-用户总成交量

- 接口声明：`GET /user-trade-summary-rank`
- 输入字段：`id`, `start_date`, `end_date`, `page`, `sort_type`, `limit`, `user_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:534` · `UserTradeSummaryRank`

### PERPETUAL-018 · 合约-交易排名-成交价排名

- 接口声明：`GET /realtime-price-rank`
- 输入字段：`market`, `bid_rank`, `ask_rank`, `last_hour`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:720` · `RealtimePriceRank`

### PERPETUAL-019 · 永续-交易排名-用户总成交手续费排名

- 接口声明：`GET /user-trade-fee-summary-rank`
- 输入字段：`id`, `start_date`, `end_date`, `page`, `sort_type`, `limit`, `user_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:821` · `UserTradeFeeSummaryRank`

### PERPETUAL-020 · 永续-永续-持仓列表

- 接口声明：`GET /position-list`
- 输入字段：`market`, `side`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:981` · `PositionList`

### PERPETUAL-021 · 永续-永续-持仓统计

- 接口声明：`GET /position-summary`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1034` · `PositionSummary`

### PERPETUAL-022 · 永续-永续-爆仓记录

- 接口声明：`GET /liquidation-records`
- 输入字段：`market`, `side`, `id`, `start_time`, `end_time`, `insurance_change`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1082` · `LiquidationRecords`

### PERPETUAL-023 · 永续-永续-爆仓记录详情

- 接口声明：`GET /liquidation-records/<int:position_id>/<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1186` · `LiquidationRecordsDetail`

### PERPETUAL-024 · 永续-永续-自动减仓记录

- 接口声明：`GET /auto-deleveraging-records`
- 输入字段：`market`, `side`, `id`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1220` · `AutoDeleveragingRecords`

### PERPETUAL-025 · 永续-永续-保险基金

- 接口声明：`GET /insurance`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1270` · `Insurance`

### PERPETUAL-026 · 永续-永续-保险基金明细

- 接口声明：`GET /insurance-detail`
- 输入字段：`asset`, `insurance_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1307` · `InsuranceDetail`

### PERPETUAL-027 · 永续普通委托-未完成订单详情

- 接口声明：`GET /pending-order-detail`
- 输入字段：`user_id`, `order_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1376` · `PendingOrderDetailResource`

### PERPETUAL-028 · 报表-永续-交易报表

- 接口声明：`GET /report-trade`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1451` · `TradeReportResource`

### PERPETUAL-029 · 报表-永续-市场报表

- 接口声明：`GET /report-market`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `order_type`, `market`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1549` · `MarketReportResource`

### PERPETUAL-030 · 报表-永续-市场详情报表 

- 接口声明：`GET /report-market-detail`
- 输入字段：`report_type`, `report_date`, `order`, `order_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1615` · `MarketDetailReportResource`

### PERPETUAL-031 · 报表-永续-保险基金报表

- 接口声明：`GET /report-insurance`
- 输入字段：`report_type`, `start_date`, `end_date`, `asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1712` · `InsuranceReportResource`

### PERPETUAL-032 · 永续-永续配置-普通指数配置

- 接口声明：`GET /market-index`
- 输入字段：`market`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1769` · `MarginIndexResource`

### PERPETUAL-033 · 永续-永续配置-普通指数配置-添加普通指数配置

- 接口声明：`POST /market-index`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1828` · `MarginIndexResource`

### PERPETUAL-034 · 永续-永续配置-普通指数配置-编辑普通指数配置

- 接口声明：`PUT /market-index`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1865` · `MarginIndexResource`

### PERPETUAL-035 · 永续-永续配置-合成指数配置列表

- 接口声明：`GET /compose`
- 输入字段：`name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1925` · `ComposeIndexResource`

### PERPETUAL-036 · 永续-永续配置-新建合成指数配置

- 接口声明：`POST /compose`
- 输入字段：`name`, `compose_method`, `price_precision`, `first_market`, `second_market`, `status`, `is_visible`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:1970` · `ComposeIndexResource`

### PERPETUAL-037 · 永续-永续配置-合成指数设置

- 接口声明：`PUT /compose/<int:index_id>`
- 输入字段：`name`, `compose_method`, `price_precision`, `first_market`, `second_market`, `status`, `is_visible`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2035` · `ComposeIndexIdResource`

### PERPETUAL-038 · 永续-永续配置-合成指数状态设置

- 接口声明：`PATCH /compose/<int:index_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2085` · `ComposeIndexIdResource`

### PERPETUAL-039 · 永续-永续配置-市场配置

- 接口声明：`GET /markets-config`
- 输入字段：`name`, `status`, `offline_visible`, `funding_interval_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2132` · `MarketsConfigResource`

### PERPETUAL-040 · 永续-永续配置-添加市场配置

- 接口声明：`POST /markets-config`
- 输入字段：`name`, `market_type`, `fee_precision`, `amount_precision`, `base_asset`, `quote_asset`, `base_asset_precision`, `quote_asset_precision`, `price_size`, `min_order_amount`, `multiplier`, `leverages`, `depths`, `leverage_default`, `depth_default`, `position_type_default`, `impact_amount`, `funding_start`, `default_funding_interval`, `funding_rate_precision`, `funding_max`, `funding_min`, `funding_limit_type`, `sign_price_limit_threshold`, `liq_risk_alert`, `details`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2207` · `MarketsConfigResource`

### PERPETUAL-041 · 永续-永续配置-市场配置-不符合数量精度的数据导出

- 接口声明：`GET /markets-config/invalid-amount-export`
- 输入字段：`market`, `amount_precision`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2404` · `MarketsConfigInvalidAmountExportResource`

### PERPETUAL-042 · 永续-永续配置-编辑市场配置

- 接口声明：`PUT /markets-config/<int:account_id>`
- 输入字段：`name`, `market_type`, `fee_precision`, `amount_precision`, `base_asset`, `quote_asset`, `base_asset_precision`, `quote_asset_precision`, `price_size`, `min_order_amount`, `multiplier`, `leverages`, `depths`, `leverage_default`, `depth_default`, `position_type_default`, `impact_amount`, `funding_start`, `default_funding_interval`, `funding_rate_precision`, `funding_max`, `funding_min`, `funding_limit_type`, `sign_price_limit_threshold`, `liq_risk_alert`, `details`, `status`, `offline_visible`, `ended_at`, `api_perpetual_trading_disabled`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2460` · `MarketsConfigDetailResource`

### PERPETUAL-043 · 永续-永续配置-市场配置-开关

- 接口声明：`PATCH /markets-config/<int:account_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2606` · `MarketsConfigDetailResource`

### PERPETUAL-044 · 永续-永续配置-编辑资产配置

- 接口声明：`PUT /assets/<int:asset_id>`
- 输入字段：`is_visible`, `status`, `save_precision`, `show_precision`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2637` · `PerpetualAssetsDetailResource`

### PERPETUAL-045 · 永续-永续配置-资产配置-添加资产配置

- 接口声明：`POST /assets`
- 输入字段：`is_visible`, `status`, `name`, `save_precision`, `show_precision`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2678` · `PerpetualAssetsResource`

### PERPETUAL-046 · 永续-永续配置-资产配置列表

- 接口声明：`GET /assets`
- 输入字段：`name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2712` · `PerpetualAssetsResource`

### PERPETUAL-047 · 永续-通知更新永续配置

- 接口声明：`PUT /update-config`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual.py:2743` · `UpdateConfigResource`

### PERPETUAL-048 · 合约-策略交易-网格市场配置列表 

- 接口声明：`GET /markets`
- 输入字段：`market`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:69` · `PerpGridMarketsResource`

### PERPETUAL-049 · 合约-策略交易-新增网格市场配置

- 接口声明：`POST /markets`
- 输入字段：`market`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:106` · `PerpGridMarketsResource`

### PERPETUAL-050 · 合约-策略交易-网格市场配置修改

- 接口声明：`PUT /markets`
- 输入字段：`market`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:132` · `PerpGridMarketsResource`

### PERPETUAL-051 · 合约-策略交易-网格市场下架

- 接口声明：`DELETE /markets`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:160` · `PerpGridMarketsResource`

### PERPETUAL-052 · 合约-策略交易-网格市场配置-批量终止策略

- 接口声明：`PUT /batch-terminate`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:205` · `PerpGridBatchTerminateResource`

### PERPETUAL-053 · 合约-策略交易-网格策略列表

- 接口声明：`GET /grid-list`
- 输入字段：`grid_id`, `user_id`, `market`, `status`, `terminate_type`, `direction`, `created_start`, `created_end`, `terminated_start`, `terminated_end`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:256` · `PerpGridListResource`

### PERPETUAL-054 · 合约-策略交易-网格策略详情

- 接口声明：`GET /grid-detail/<int:grid_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:466` · `PerpGridDetailResource`

### PERPETUAL-055 · 合约-策略交易-终止网格策略

- 接口声明：`DELETE /grid-detail/<int:grid_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:541` · `PerpGridDetailResource`

### PERPETUAL-056 · 合约-策略交易-编辑网格备注

- 接口声明：`POST /grid-remark`
- 输入字段：`grid_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:561` · `PerpGridRemarkResource`

### PERPETUAL-057 · 合约-策略交易-网格策略详情-成交记录

- 接口声明：`GET /arbitrage-orders`
- 输入字段：`grid_id`, `side`, `order_type`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:735` · `PerpGridArbitrageOrdersResource`

### PERPETUAL-058 · 合约-策略交易-网格策略详情-资金费用

- 接口声明：`GET /funding-history`
- 输入字段：`grid_id`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:844` · `PerpGridFundingHistoryResource`

### PERPETUAL-059 · 合约网格-关联历史

- 接口声明：`GET /relation-history`
- 输入字段：`history_type`, `start`, `end`, `row_id`, `grid_id`, `grid_index`, `round_id`, `open_order_id`, `close_order_id`, `user_id`, `operator_id`, `from_user_id`, `to_user_id`, `asset`, `order_id`, `side`, `direction`, `order_status`, `transfer_status`, `transfer_type`, `change_op_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/perpetual_grid.py:898` · `PerpGridRelationHisResource`

### PERPETUAL-060 · 报表-资产报表-合约

- 接口声明：`GET /balance`
- 输入字段：`query_date`, `asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:37` · `DailyPerpetualBalanceResource`

### PERPETUAL-061 · 报表-资产报表-合约-币种详情

- 接口声明：`GET /asset-balance`
- 输入字段：`asset`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:77` · `DailyPerpetualAssetBalanceResource`

### PERPETUAL-062 · 报表-合约报表-爆仓-市场

- 接口声明：`GET /liquidation`
- 输入字段：`report_type`, `start_date`, `end_date`, `market`, `page`, `limit`, `sort_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:125` · `MarginLiquidationResource`

### PERPETUAL-063 · 报表-合约报表-全站爆仓聚合统计

- 接口声明：`GET /liquidation-summary`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:224` · `MarginLiquidationSummaryResource`

### PERPETUAL-064 · 报表-做市报表-合约

- 接口声明：`GET /maker-deals`
- 输入字段：`report_type`, `maker_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:343` · `DailySpotMakerDealsResource`

### PERPETUAL-065 · 报表-做市报表-合约交易市场详情

- 接口声明：`GET /maker-market-detail`
- 输入字段：`report_date`, `order`, `trading_area`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:414` · `DailySpotMakerMarketDetailResource`

### PERPETUAL-066 · 报表-合约交易-深度报表

- 接口声明：`GET /depth`
- 输入字段：`report_type`, `start_date`, `end_date`, `market`, `exchange`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:522` · `DailyPerpetualDepthResource`

### PERPETUAL-067 · 报表-合约交易-深度详情

- 接口声明：`GET /depth-detail`
- 输入字段：`report_date`, `order`, `report_type`, `exchange`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:688` · `DailySpotDepthDetailResource`

### PERPETUAL-068 · 报表-合约交易-资金费用

- 接口声明：`GET /funding-fee`
- 输入字段：`start_date`, `end_date`, `report_type`, `market`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:794` · `FundingFeeResource`

### PERPETUAL-069 · 报表-合约交易-资金费用市场详情

- 接口声明：`GET /funding-fee-detail`
- 输入字段：`report_date`, `report_type`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:845` · `FundingFeeDetailResource`

### PERPETUAL-070 · 报表-合约报表-合约划转报表

- 接口声明：`GET /transfer`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:961` · `PerpetualTransferReportResource`

### PERPETUAL-071 · 报表-合约报表-合约盈亏统计

- 接口声明：`GET /profit-loss`
- 输入字段：`start_date`, `end_date`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/perpetual.py:1044` · `PerpetualProfitLossResource`

### PERPETUAL-072 · 合约划转（in）

- 接口声明：`POST /transfer/in`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/balance.py:48` · `BalanceTransferIn`

### PERPETUAL-073 · 合约可划转数量

- 接口声明：`GET /transfer/balance`
- 输入字段：`coin_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/balance.py:81` · `TransferBalanceResource`

### PERPETUAL-074 · 合约划转（out）

- 接口声明：`POST /transfer/out`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/balance.py:101` · `BalanceTransferOut`

### PERPETUAL-075 · 合约资产流水

- 接口声明：`GET /history`
- 输入字段：`asset`, `business`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/balance.py:150` · `BalanceHistory`

### PERPETUAL-076 · 合约资产流水类型

- 接口声明：`GET /history/type`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/balance.py:215` · `AssetHistoryType`

### PERPETUAL-077 · 合约市场信息

- 接口声明：`GET /list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:65` · `MarketList`

### PERPETUAL-078 · 实时保险基金，客户端和前端都没有调用

- 接口声明：`GET /insurance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:105` · `MarketInsurances`

### PERPETUAL-079 · 市场信息-溢价指数

- 接口声明：`GET /premium`
- 输入字段：`market`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:123` · `MarketPremiumHistory`

### PERPETUAL-080 · PerMarketOfflineInfoResource.get（用途待确认）

- 接口声明：`GET /offline-info`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:149` · `PerMarketOfflineInfoResource`

### PERPETUAL-081 · 市场信息-资金费率

- 接口声明：`GET /funding/history`
- 输入字段：`market`, `start_time`, `end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:172` · `MarketFundingHistory`

### PERPETUAL-082 · 获取实时资金费率

- 接口声明：`GET /funding`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:206` · `FundingIntimeResource`

### PERPETUAL-083 · 市场信息-保险基金

- 接口声明：`GET /insurance/history`
- 输入字段：`asset`, `market`, `page`, `limit`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:244` · `InsuranceHistoryResource`

### PERPETUAL-084 · 市场信息-开仓数量、多空比例(APP端上线合约信息相关功能后可删除该接口)

- 接口声明：`GET /position/history`
- 输入字段：`market`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:297` · `PositionHistoryResource`

### PERPETUAL-085 · 市场信息-开仓数量、多空比例

- 接口声明：`GET /position-interval/history`
- 输入字段：`market`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:353` · `PositionIntervalHistoryResource`

### PERPETUAL-086 · 市场信息-大户持仓多空比例

- 接口声明：`GET /big-customer-position/history`
- 输入字段：`market`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:408` · `BigCustomerPositionHistoryResource`

### PERPETUAL-087 · 交易量、主动买入卖出量

- 接口声明：`GET /trade/history`
- 输入字段：`market`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:466` · `PerpetualTradeHistoryResource`

### PERPETUAL-088 · 全市场加权资金费率

- 接口声明：`GET /weighted-funding-rate/history`
- 输入字段：`interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:563` · `WeightedFundingRateHistoryResource`

### PERPETUAL-089 · 合约杠杆配置

- 接口声明：`GET /limit/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:599` · `MarketLimitConfig`

### PERPETUAL-090 · 用户全仓、逐仓配置

- 接口声明：`GET /preference`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/market.py:611` · `MarketPreference`

### PERPETUAL-091 · 获取合约费率

- 接口声明：`GET /fee/rate`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/market.py:676` · `MarketFeeRate`

### PERPETUAL-092 · 获取多个市场的合约费率

- 接口声明：`GET /fee/rates`
- 输入字段：`markets`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/market.py:694` · `MarketsFeeRateResource`

### PERPETUAL-093 · 开通合约交易

- 接口声明：`POST /sign`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/market.py:713` · `MarketSignAgreement`

### PERPETUAL-094 · 市场信息-合约信息、指数价格

- 接口声明：`GET /index`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:750` · `MarketIndex`

### PERPETUAL-095 · MarketIndexDetailResource.get（用途待确认）

- 接口声明：`GET /index-detail`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:761` · `MarketIndexDetailResource`

### PERPETUAL-096 · 调整市场杠杆

- 接口声明：`POST /leverage/adjust`
- 输入字段：`market`, `position_type`, `leverage`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/market.py:853` · `MarketLeverageAdjust`

### PERPETUAL-097 · 订单信息-交易记录

- 接口声明：`GET /user/deals`
- 输入字段：`market`, `side`, `start_time`, `end_time`, `page`, `limit`, `export`, `market_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/market.py:935` · `MarketUserDeals`

### PERPETUAL-098 · AssetsResource.get（用途待确认）

- 接口声明：`GET /assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:997` · `AssetsResource`

### PERPETUAL-099 · MarketKlineResource.get（用途待确认）

- 接口声明：`GET /kline`
- 输入字段：`market`, `start_time`, `end_time`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:1009` · `MarketKlineResource`

### PERPETUAL-100 · 获取合约市场基差价格

- 接口声明：`GET /basis-history`
- 输入字段：`market`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:1054` · `BasisPriceResource`

### PERPETUAL-101 · MonthlyMarketChangeRateResource.get（用途待确认）

- 接口声明：`GET /change-rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:1157` · `MonthlyMarketChangeRateResource`

### PERPETUAL-102 · 合约市场强平信息统计

- 接口声明：`GET /liquidation/history`
- 输入字段：`market`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:1181` · `LiquidationHistoryResource`

### PERPETUAL-103 · 全市场加权爆仓数据

- 接口声明：`GET /weighted-liquidation/history`
- 输入字段：`interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:1237` · `WeightedLiquidationResource`

### PERPETUAL-104 · 市场详情

- 接口声明：`GET /detail`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/market.py:1350` · `PerpetualMarketDetailResource`

### PERPETUAL-105 · 限价下单

- 接口声明：`PUT /limit`
- 输入字段：`market`, `side`, `amount`, `price`, `effect_type`, `hide`, `stop_loss_take_profit`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL]); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/order.py:86` · `LimitOrderResource`

### PERPETUAL-106 · 撤销普通成交

- 接口声明：`DELETE /limit`
- 输入字段：`market`, `order_id`, `type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:200` · `LimitOrderResource`

### PERPETUAL-107 · 获取普通成交订单信息

- 接口声明：`GET /limit`
- 输入字段：`market`, `side`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:267` · `LimitOrderResource`

### PERPETUAL-108 · 预览分段委托订单的子订单列表

- 接口声明：`GET /scaled`
- 输入字段：`min_price`, `max_price`, `total_segment`, `total_amount`, `mode`, `market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/order.py:303` · `PerpScaledOrderResource`

### PERPETUAL-109 · 提交分段委托订单

- 接口声明：`POST /scaled`
- 输入字段：`min_price`, `max_price`, `total_segment`, `total_amount`, `mode`, `market`, `side`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL]); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/order.py:351` · `PerpScaledOrderResource`

### PERPETUAL-110 · 市价下单

- 接口声明：`PUT /market`
- 输入字段：`market`, `side`, `amount`, `stop_loss_take_profit`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL]); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/order.py:466` · `MarketOrderResource`

### PERPETUAL-111 · 限价平仓(目前web端在使用，后期考虑移除)

- 接口声明：`PUT /close`
- 输入字段：`market`, `position_id`, `amount`, `price`, `effect_type`
- 显式控制：require_login; trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/perpetual/order.py:539` · `CloseOrderResource`

### PERPETUAL-112 · 市价全平(兼容旧版本，未来可移除)

- 接口声明：`POST /close`
- 输入字段：`market`, `position_id`
- 显式控制：require_login; trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/perpetual/order.py:607` · `CloseOrderResource`

### PERPETUAL-113 · 自定义市价平仓(目前web端在使用，后期考虑移除)

- 接口声明：`PUT /market/close`
- 输入字段：`market`, `position_id`, `amount`
- 显式控制：require_login; trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/perpetual/order.py:649` · `MarketCloseOrderResource`

### PERPETUAL-114 · 一键全平(目前web端在使用，后期考虑移除)

- 接口声明：`POST /market/close`
- 输入字段：`market`, `position_id`
- 显式控制：require_login; trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/perpetual/order.py:702` · `MarketCloseOrderResource`

### PERPETUAL-115 · 计划限价

- 接口声明：`PUT /stop`
- 输入字段：`market`, `side`, `stop_type`, `amount`, `stop_price`, `price`, `effect_type`, `hide`, `stop_loss_take_profit`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL]); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/order.py:744` · `StopOrderResource`

### PERPETUAL-116 · 计划市价

- 接口声明：`POST /stop`
- 输入字段：`market`, `side`, `stop_type`, `amount`, `stop_price`, `stop_loss_take_profit`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL]); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/order.py:855` · `StopOrderResource`

### PERPETUAL-117 · 获取计划委托订单信息

- 接口声明：`GET /stop`
- 输入字段：`market`, `side`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:956` · `StopOrderResource`

### PERPETUAL-118 · 撤销计划委托订单

- 接口声明：`DELETE /stop`
- 输入字段：`market`, `order_id`, `type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:987` · `StopOrderResource`

### PERPETUAL-119 · 修改订单

- 接口声明：`POST /modify`
- 输入字段：`market`, `order_id`, `amount`, `price`, `stop_loss_take_profit`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL]); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/order.py:1021` · `ModifyOrderResource`

### PERPETUAL-120 · 修改计划订单

- 接口声明：`POST /stop/modify`
- 输入字段：`market`, `order_id`, `amount`, `price`, `stop_price`, `stop_loss_take_profit`, `stop_type`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL]); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/order.py:1090` · `ModifyOrderStopResource`

### PERPETUAL-121 · 历史普通委托

- 接口声明：`GET /finished`
- 输入字段：`market`, `side`, `start_time`, `end_time`, `page`, `limit`, `stop_order_id`, `export`, `market_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:1242` · `FinishedOrderResource`

### PERPETUAL-122 · 历史计划委托

- 接口声明：`GET /finished/stop`
- 输入字段：`market`, `side`, `start_time`, `end_time`, `page`, `limit`, `export`, `market_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:1388` · `FinishedStopOrderResource`

### PERPETUAL-123 · 成交明细

- 接口声明：`GET /deals`
- 输入字段：`order_id`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:1464` · `OrderDealsResource`

### PERPETUAL-124 · 市场信息-强平订单（未成交）

- 接口声明：`GET /liqing`
- 输入字段：`market`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/order.py:1497` · `OrderLiqingResource`

### PERPETUAL-125 · 市场信息-强平订单（最近7天/30天已成交）

- 接口声明：`GET /finished/liquidation`
- 输入字段：`market`, `page`, `limit`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/order.py:1523` · `OrderFinishedLiquidationResource`

### PERPETUAL-126 · StopOrderSummaryResource.get（用途待确认）

- 接口声明：`GET /stop-order-summary/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:1596` · `StopOrderSummaryResource`

### PERPETUAL-127 · 自营交易用户的挂单会在深度中隐藏(相当于冰山委托)， 但是他们自己要能在深度中看到自己的挂单，该接口指示客户端合并挂单到深度

- 接口声明：`GET /motd`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/order.py:1641` · `MergeOrderToDepthResource`

### PERPETUAL-128 · 市场信息-仓位档位介绍-仓位维持保证金率

- 接口声明：`GET /pending`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:45` · `PositionPendingResource`

### PERPETUAL-129 · 获取最大可开数量

- 接口声明：`GET /expect`
- 输入字段：`market`, `price`, `side`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:74` · `PositionExpectResource`

### PERPETUAL-130 · 历史持仓

- 接口声明：`GET /finished`
- 输入字段：`market`, `market_type`, `page`, `limit`, `start_time`, `end_time`, `side`, `export`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:150` · `PositionFinishedResource`

### PERPETUAL-131 · 资金费用

- 接口声明：`GET /funding`
- 输入字段：`market`, `market_type`, `page`, `limit`, `start_time`, `end_time`, `side`, `export`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:261` · `PositionFundingResource`

### PERPETUAL-132 · 仓位明细-加减仓

- 接口声明：`GET /deal/detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:376` · `PositionDealDetailResource`

### PERPETUAL-133 · 仓位明细-追加/减少保证金

- 接口声明：`GET /margin/detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:426` · `PositionMarginResource`

### PERPETUAL-134 · 仓位明细-资金费用

- 接口声明：`GET /funding/detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:465` · `FundingDetailResource`

### PERPETUAL-135 · 仓位明细-仓位信息

- 接口声明：`GET /summary`
- 输入字段：`position_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:501` · `PositionSummaryResource`

### PERPETUAL-136 · 加减保证金

- 接口声明：`POST /margin/adjust`
- 输入字段：`market`, `type`, `amount`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:535` · `PositionAdjustResource`

### PERPETUAL-137 · PositionLimitConfigResource.get（用途待确认）

- 接口声明：`GET /limit/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/position.py:579` · `PositionLimitConfigResource`

### PERPETUAL-138 · 设置止损

- 接口声明：`POST /stop-loss`
- 输入字段：`position_id`, `market`, `price`, `type`, `amount`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:599` · `PositionStopLossResource`

### PERPETUAL-139 · 止损单修改

- 接口声明：`PATCH /stop-loss`
- 输入字段：`position_id`, `market`, `price`, `type`, `amount`, `sl_id`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:684` · `PositionStopLossResource`

### PERPETUAL-140 · 清除止损

- 接口声明：`DELETE /stop-loss`
- 输入字段：`position_id`, `market`, `sl_id`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:776` · `PositionStopLossResource`

### PERPETUAL-141 · 清除止损(兼容旧版本，未来可移除)

- 接口声明：`PUT /stop-loss`
- 输入字段：`position_id`, `market`, `sl_id`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:793` · `PositionStopLossResource`

### PERPETUAL-142 · 设置止盈

- 接口声明：`POST /take-profit`
- 输入字段：`position_id`, `market`, `price`, `type`, `amount`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:814` · `PositionTakeProfitResource`

### PERPETUAL-143 · 止盈单修改

- 接口声明：`PATCH /take-profit`
- 输入字段：`position_id`, `market`, `price`, `type`, `amount`, `tp_id`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:898` · `PositionTakeProfitResource`

### PERPETUAL-144 · 清除止盈

- 接口声明：`DELETE /take-profit`
- 输入字段：`position_id`, `market`, `tp_id`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:983` · `PositionTakeProfitResource`

### PERPETUAL-145 · 清除止盈(兼容旧版本，未来可移除)

- 接口声明：`PUT /take-profit`
- 输入字段：`position_id`, `market`, `tp_id`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.PERPETUAL])
- 代码依据：`app/api/frontend/perpetual/position.py:1000` · `PositionTakeProfitResource`

### PERPETUAL-146 · 限价平仓

- 接口声明：`DELETE /limit`
- 输入字段：`market`, `position_id`, `amount`, `price`, `effect_type`
- 显式控制：require_login; trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/perpetual/position.py:1027` · `LimitClosePositionResource`

### PERPETUAL-147 · 市价平仓

- 接口声明：`DELETE /market`
- 输入字段：`market`, `position_id`, `amount`, `type`
- 显式控制：require_login; trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/perpetual/position.py:1095` · `MarketClosePositionResource`

### PERPETUAL-148 · 一键全平(拍卖式下单（目前app端在使用）)

- 接口声明：`DELETE `
- 输入字段：`market`, `position_id`
- 显式控制：require_login; trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/perpetual/position.py:1157` · `CloseAllOrderResource`

### PERPETUAL-149 · 仓位明细-结算记录

- 接口声明：`GET /settle/detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:1212` · `SettleDetailResource`

### PERPETUAL-150 · 设置结算开关

- 接口声明：`PUT /settle/setting`
- 输入字段：`status`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:1241` · `SettleSettingResource`

### PERPETUAL-151 · 获取结算开关状态

- 接口声明：`GET /settle/setting`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:1251` · `SettleSettingResource`

### PERPETUAL-152 · 获取一键平仓相关信息

- 接口声明：`GET /auction-pending`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/perpetual/position.py:1263` · `AuctionPendingResource`

### PERPETUAL-153 · 合约网格-支持的市场列表

- 接口声明：`GET /grid/markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/perpetual/strategy.py:64` · `PerpGridMarketsResource`

### PERPETUAL-154 · 合约网格列表

- 接口声明：`GET /grid`
- 输入字段：`market`, `status`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:272` · `PerpGridListResource`

### PERPETUAL-155 · 合约网格-新建策略

- 接口声明：`POST /grid`
- 输入字段：`market`, `direction`, `leverage`, `lowest_price`, `highest_price`, `grid_count`, `margin_amount`, `reserved_margin_amount`, `auto_reserve_margin`, `trigger_price`, `take_profit_price`, `stop_loss_price`, `is_market_open`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True); trade_permission_validate(is_spot=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:362` · `PerpGridListResource`

### PERPETUAL-156 · 合约网格-策略详情

- 接口声明：`GET /grid/<int:grid_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:475` · `PerpGridDetailResource`

### PERPETUAL-157 · 合约网格-修改策略参数

- 接口声明：`PATCH /grid/<int:grid_id>`
- 输入字段：`take_profit_price`, `stop_loss_price`, `trigger_price`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/perpetual/strategy.py:487` · `PerpGridDetailResource`

### PERPETUAL-158 · 合约网格-终止策略

- 接口声明：`DELETE /grid/<int:grid_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/perpetual/strategy.py:543` · `PerpGridDetailResource`

### PERPETUAL-159 · 合约网格-获取终止预览信息

- 接口声明：`GET /grid/terminate-preview`
- 输入字段：`grid_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:559` · `PerpGridTerminatePreviewResource`

### PERPETUAL-160 · 合约网格-获取网格可减少的保证金数目

- 接口声明：`GET /grid/margin`
- 输入字段：`grid_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:633` · `PerpGridMarginResource`

### PERPETUAL-161 · 合约网格-调整保证金

- 接口声明：`POST /grid/margin`
- 输入字段：`grid_id`, `type`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:654` · `PerpGridMarginResource`

### PERPETUAL-162 · 合约网格-策略当前委托

- 接口声明：`GET /grid/pending-orders`
- 输入字段：`grid_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:702` · `PerpGridPendingOrderResource`

### PERPETUAL-163 · 合约网格-策略资金费用

- 接口声明：`GET /grid/funding-history`
- 输入字段：`grid_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:753` · `PerpGridFundingHisResource`

### PERPETUAL-164 · 合约网格-策略套利历史

- 接口声明：`GET /grid/arbitrage-orders`
- 输入字段：`grid_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:882` · `PerpGridArbitrageOrderResource`

### PERPETUAL-165 · 合约网格-策略收益曲线 

- 接口声明：`GET /grid/profit-series`
- 输入字段：`grid_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/perpetual/strategy.py:985` · `PerpGridStrategyProfitSeriesResource`

### PERPETUAL-166 · [     {         "name": "BTC",  //资产名         "prec_save": 20, //保存精度         "prec_show": 8,   //展示精度         "show":true       //是否显示， 默认为true     },     {         "name": "ETH",

- 接口声明：`GET /assets/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/perpetual.py:23` · `PerpetualAssetsResource`

### PERPETUAL-167 ·     { //普通指数配置     "BTCUSD": {         "name": "BTCUSD", //展示市场名         "prec": 2,   //指数价格精度         "sources": [  //交易所配置             {                 "exchange": "bitstamp",  

- 接口声明：`GET /markets/index`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/perpetual.py:57` · `PerpetualMarketsIndex`

### PERPETUAL-168 ·     [ {     "type": 2,         //市场类型 1: 正向合约, 2: 反向合约     "name": "BTCUSD",  //市场名     "fee_prec": 5,     //费率精度     "amount_prec": 0,  //U本位市场为下单数量精度，币本位市场为合约张数精度     "stock": { 

- 接口声明：`GET /markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/perpetual.py:133` · `PerpetualMarketsResource`

### PERPETUAL-169 · PropTradingConfigResource.get（用途待确认）

- 接口声明：`GET /prop-trading/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/perpetual.py:226` · `PropTradingConfigResource`

### PERPETUAL-170 · BoostConfigResource.get（用途待确认）

- 接口声明：`GET /boost/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/perpetual.py:244` · `BoostConfigResource`

### PERPETUAL-171 · {     "code": 0,     "data": [user_id1, user_id2, ...],     "message": "Success" }

- 接口声明：`GET /special-position-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/perpetual.py:256` · `SpecialPositionUsersResource`

## 相关测试文件（路径归类，未执行）

- `tests/business/equity_center/test_perpetual_trial_monitor.py`
- `tests/business/equity_center/test_perpetual_trial_profit_threshold.py`
- `tests/business/perpetual/test_slice_user_export.py`
- `tests/business/strategy/test_perpetual_grid.py`
- `tests/caches/test_perpetual.py`
- `tests/schedules/test_perpetual.py`
- `tests/schedules/test_perpetual_market_info.py`
- `tests/schedules/test_perpetual_upgrade_user_export.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
