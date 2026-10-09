# 理财与策略 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### INVESTMENT-001 · 现货-理财-双币投资-获取市场列表

- 接口声明：`GET /market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:76` · `DualInvestmentMarketResource`

### INVESTMENT-002 · 现货-理财-双币投资-修改市场列表

- 接口声明：`POST /market`
- 输入字段：`base`, `quote`, `is_open`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:81` · `DualInvestmentMarketResource`

### INVESTMENT-003 · 现货-理财-双币投资-产品列表

- 接口声明：`GET /product`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:115` · `DualInvestmentProductResource`

### INVESTMENT-004 · 现货-理财-双币投资-订单列表

- 接口声明：`GET /order`
- 输入字段：`market`, `di_type`, `status`, `user`, `coinex_order_id`, `matrixport_order_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:152` · `DualInvestmentOrderResource`

### INVESTMENT-005 · 现货-理财-双币投资-投资记录

- 接口声明：`GET /history`
- 输入字段：`market`, `di_type`, `opt_type`, `user`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:222` · `DualInvestmentHistoryResource`

### INVESTMENT-006 · 现货-理财-双币投资-持仓排名

- 接口声明：`GET /position/statistic`
- 输入字段：`asset`, `market`, `user`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:281` · `DualInvestmentPositionStatisticResource`

### INVESTMENT-007 · 现货-理财-双币投资-报表

- 接口声明：`GET /report`
- 输入字段：`report_type`, `start_date`, `end_date`, `market`, `report_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:373` · `DualInvestmentReportResource`

### INVESTMENT-008 · 现货-理财-双币投资-统计

- 接口声明：`GET /statistic`
- 输入字段：`period`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/dual_investment.py:430` · `DualInvestmentStatisticResource`

### INVESTMENT-009 · 现货-理财-定期理财-产品列表

- 接口声明：`GET /product-list`
- 输入字段：`name`, `asset`, `product_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fixed_investment.py:40` · `FixedInvestProductListResource`

### INVESTMENT-010 · 现货-理财-定期理财-新增产品

- 接口声明：`POST /product-list`
- 输入字段：`asset`, `lock_days`, `base_apr`, `min_subscription_amount`, `max_user_total_amount`, `total_amount`
- 显式控制：lock_request('admin_fixed_invest_product')
- 代码依据：`app/api/admin/fixed_investment.py:110` · `FixedInvestProductListResource`

### INVESTMENT-011 · 现货-理财-定期理财-编辑产品

- 接口声明：`PUT /product-list`
- 输入字段：`id`, `min_subscription_amount`, `max_user_total_amount`, `total_amount`
- 显式控制：lock_request('admin_fixed_invest_product')
- 代码依据：`app/api/admin/fixed_investment.py:151` · `FixedInvestProductListResource`

### INVESTMENT-012 · 现货-理财-定期理财-上架产品

- 接口声明：`PATCH /product-list`
- 输入字段：`id`, `status`
- 显式控制：lock_request('admin_fixed_invest_product')
- 代码依据：`app/api/admin/fixed_investment.py:184` · `FixedInvestProductListResource`

### INVESTMENT-013 · 现货-理财-定期理财-下架产品

- 接口声明：`DELETE /product-list`
- 输入字段：`id`
- 显式控制：lock_request('admin_fixed_invest_product')
- 代码依据：`app/api/admin/fixed_investment.py:222` · `FixedInvestProductListResource`

### INVESTMENT-014 · 现货-理财-定期理财-存单列表

- 接口声明：`GET /user-record-list`
- 输入字段：`name`, `asset`, `user_id`, `product_id`, `record_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fixed_investment.py:261` · `FixedInvestUserRecordListResource`

### INVESTMENT-015 · 现货-理财-定期理财-编辑存单

- 接口声明：`PUT /user-record-list`
- 输入字段：`id`, `subsidy_apr`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fixed_investment.py:322` · `FixedInvestUserRecordListResource`

### INVESTMENT-016 · 现货-理财-定期理财-存单操作记录

- 接口声明：`GET /user-record/changelog`
- 输入字段：`record_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fixed_investment.py:353` · `FixedInvestUserRecordChangelogResource`

### INVESTMENT-017 · 现货-理财-定期理财-相关记录

- 接口声明：`GET /relation-history`
- 输入字段：`history_type`, `start`, `end`, `start_date`, `end_date`, `row_id`, `user_id`, `product_id`, `record_id`, `asset`, `operate_his_type`, `operate_his_status`, `interest_his_type`, `interest_his_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fixed_investment.py:417` · `FixedInvestRelationHisResource`

### INVESTMENT-018 · 币币-理财-理财收益排名

- 接口声明：`GET /rank`
- 输入字段：`asset`, `time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:35` · `InvestmentRankResource`

### INVESTMENT-019 · 币币-理财-理财余额排名

- 接口声明：`GET /balance-rank`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:71` · `InvestmentBalanceRankResource`

### INVESTMENT-020 · 币币-理财-活期理财记录

- 接口声明：`GET /record`
- 输入字段：`asset`, `user_id`, `history_type`, `time_type`, `interest_type`, `trans_type`, `status`, `interest_status`, `cursor`, `start_at`, `end_at`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:112` · `InvestmentBalanceRecordResource`

### INVESTMENT-021 · 理财-活期理财配置-获取配置列表

- 接口声明：`GET /config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:224` · `InvestmentConfigResource`

### INVESTMENT-022 · 理财-活期理财配置-新增配置

- 接口声明：`POST /config`
- 输入字段：`asset`, `min_amount`, `ladder_limit`, `ladder_rate`, `fixed_rate`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:343` · `InvestmentConfigResource`

### INVESTMENT-023 · 理财-活期理财配置-编辑配置

- 接口声明：`PUT /config`
- 输入字段：`asset`, `min_amount`, `ladder_limit`, `ladder_rate`, `fixed_rate`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:385` · `InvestmentConfigResource`

### INVESTMENT-024 · 理财-活期理财配置-上架/下架

- 接口声明：`PUT /config/<string:asset>/status`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:429` · `InvestmentConfigStatusResource`

### INVESTMENT-025 · 理财-活期理财配置-获取操作日志

- 接口声明：`GET /config/operation-logs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/investment.py:469` · `InvestmentConfigOperationLogsResource`

### INVESTMENT-026 · 报表-AMM全站/市场报表

- 接口声明：`GET `
- 输入字段：`market`, `start_date`, `end_date`, `report_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/amm.py:32` · `AmmReportResource`

### INVESTMENT-027 · 报表-AMM市场报表-异步下载

- 接口声明：`GET /async-download`
- 输入字段：`report_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/amm.py:206` · `AmmReportAsyncDownloadResource`

### INVESTMENT-028 · 报表-AMM-市场详情报表 

- 接口声明：`GET /report-market-detail`
- 输入字段：`report_type`, `report_date`, `order`, `order_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/amm.py:234` · `MarketDetailReportResource`

### INVESTMENT-029 · 报表-理财报表-定期理财全站报表

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/fixed-investment.py:42` · `FixedInvestSiteReportResource`

### INVESTMENT-030 · 报表-理财报表-定期理财币种报表

- 接口声明：`GET /asset-report`
- 输入字段：`report_type`, `asset`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/fixed-investment.py:143` · `FixedInvestAssetReportResource`

### INVESTMENT-031 · 报表-理财报表-定期理财全站报表详情

- 接口声明：`GET /asset-detail-report`
- 输入字段：`report_date`, `order`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/fixed-investment.py:234` · `FixedInvestDetailReportResource`

### INVESTMENT-032 · 报表-理财报表-全站理财报表

- 接口声明：`GET /site-investment-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/investment.py:93` · `SiteInvestmentReportResource`

### INVESTMENT-033 · 报表-理财报表-全站理财详情

- 接口声明：`GET /asset-detail`
- 输入字段：`report_date`, `order`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/investment.py:159` · `DailyInvestmentAssetDetailResource`

### INVESTMENT-034 · 报表-理财报表-币种理财报表

- 接口声明：`GET /asset-investment-report`
- 输入字段：`report_type`, `asset`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/investment.py:284` · `AssetInvestmentReportResource`

### INVESTMENT-035 · 报表-现货报表-现货网格报表 

- 接口声明：`GET /spot-grid/site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/strategy.py:40` · `SpotGridSiteReportResource`

### INVESTMENT-036 · 报表-合约报表-合约网格报表 

- 接口声明：`GET /perpetual-grid/site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/strategy.py:128` · `PerpGridSiteReportResource`

### INVESTMENT-037 · 全站质押理财报表

- 接口声明：`GET /report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `asset`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/staking.py:63` · `AssetStakingReportResource`

### INVESTMENT-038 · 质押理财报表-币种详情

- 接口声明：`GET /report/detail`
- 输入字段：`report_type`, `report_date`, `order`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/staking.py:126` · `AssetStakingReportDetailResource`

### INVESTMENT-039 · 质押理财汇总报表

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/staking.py:190` · `SiteStakingReportResource`

### INVESTMENT-040 · 币币-理财-链上质押排名

- 接口声明：`GET /balance-rank`
- 输入字段：`asset`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/staking.py:244` · `StakingBalanceRankResource`

### INVESTMENT-041 · 币币-理财-链上质押赎回记录

- 接口声明：`GET /system-record`
- 输入字段：`asset`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/staking.py:320` · `SystemStakingRecordResource`

### INVESTMENT-042 · 币币-理财-用户质押赎回记录

- 接口声明：`GET /user-record`
- 输入字段：`asset`, `user_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/staking.py:362` · `UserStakingRecordResource`

### INVESTMENT-043 · 统计-质押统计

- 接口声明：`GET /statistics`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/staking.py:416` · `UserStakingStatisticsResource`

### INVESTMENT-044 · 币币-理财-超额质押目标值配置

- 接口声明：`POST /config`
- 输入字段：`asset`, `target_bufsize`, `min_staking_amount`, `min_unstaking_amount`, `validator_amount`, `min_wallet_staking_amount`, `staking_threshold`, `unstaking_threshold`, `system_sharing_ratio`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/staking.py:491` · `StakingConfigResource`

### INVESTMENT-045 · 统计-理财统计-报表查看

- 接口声明：`GET `
- 输入字段：`investment_type`, `asset`, `time_range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/investment.py:29` · `InvestmentStatisticResource`

### INVESTMENT-046 · 币币-现货网格-档位配置 

- 接口声明：`GET /grid/spot/stage-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:78` · `SpotGridConfigResource`

### INVESTMENT-047 · 币币-现货网格-档位配置修改 

- 接口声明：`PUT /grid/spot/stage-config`
- 输入字段：`configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:93` · `SpotGridConfigResource`

### INVESTMENT-048 · 币币-现货网格-市场配置列表 

- 接口声明：`GET /grid/spot/markets`
- 输入字段：`market`, `stage`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:149` · `SpotGridMarketsResource`

### INVESTMENT-049 · 币币-现货网格-新增市场配置 

- 接口声明：`POST /grid/spot/markets`
- 输入字段：`market`, `status`, `min_order_amount_mul`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:221` · `SpotGridMarketsResource`

### INVESTMENT-050 · 币币-现货网格-市场配置修改 

- 接口声明：`PUT /grid/spot/markets`
- 输入字段：`market`, `status`, `min_order_amount_mul`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:263` · `SpotGridMarketsResource`

### INVESTMENT-051 · 币币-现货网格-市场下架 

- 接口声明：`DELETE /grid/spot/markets`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:303` · `SpotGridMarketsResource`

### INVESTMENT-052 · 币币-现货网格-市场配置-批量终止策略

- 接口声明：`PUT /grid/spot/batch-stop`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:354` · `SpotGridStrategyBatchStopResource`

### INVESTMENT-053 · 币币-现货网格-策略列表 

- 接口声明：`GET /grid/spot/list`
- 输入字段：`user_id`, `market`, `status`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:398` · `SpotGridStrategyListResource`

### INVESTMENT-054 · 币币-现货网格-策略详情 

- 接口声明：`GET /grid/spot/<int:strategy_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:507` · `SpotGridStrategyDetailResource`

### INVESTMENT-055 · 币币-现货网格-终止策略 

- 接口声明：`DELETE /grid/spot/<int:strategy_id>`
- 输入字段：`hold_asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:587` · `SpotGridStrategyDetailResource`

### INVESTMENT-056 · 币币-现货网格-策略详情-历史委托 

- 接口声明：`GET /grid/spot/finished-orders`
- 输入字段：`strategy_id`, `side`, `order_type`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:613` · `SpotGridStrategyFinishedOrdersResource`

### INVESTMENT-057 · 币币-现货网格-手续费订单 

- 接口声明：`GET /grid/spot/web-order-history`
- 输入字段：`strategy_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:717` · `SpotGridStrategyOrderHistoryResource`

### INVESTMENT-058 · 币币-现货网格-策略历史 

- 接口声明：`GET /grid/spot/change-history`
- 输入字段：`strategy_id`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/strategy.py:743` · `SpotGridStrategyChangeHistoryResource`

### INVESTMENT-059 · AmmMarketsResource.get（用途待确认）

- 接口声明：`GET /markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:58` · `AmmMarketsResource`

### INVESTMENT-060 · LiquidityPoolResource.get（用途待确认）

- 接口声明：`GET /liquidity/pool`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:70` · `LiquidityPoolResource`

### INVESTMENT-061 · accquire reatime pool price when adding/removing liquidity.

- 接口声明：`GET /liquidity/pool/price`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:121` · `LiquidityPoolPriceResource`

### INVESTMENT-062 · LiquidityResource.get（用途待确认）

- 接口声明：`GET /liquidity`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/amm.py:146` · `LiquidityResource`

### INVESTMENT-063 · LiquidityResource.post（用途待确认）

- 接口声明：`POST /liquidity`
- 输入字段：`market`, `base_amount`, `quote_amount`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.AMM])
- 代码依据：`app/api/frontend/amm.py:180` · `LiquidityResource`

### INVESTMENT-064 · LiquidityResource.delete（用途待确认）

- 接口声明：`DELETE /liquidity`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/amm.py:247` · `LiquidityResource`

### INVESTMENT-065 · AccountsResource.get（用途待确认）

- 接口声明：`GET /accounts`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:291` · `AccountsResource`

### INVESTMENT-066 · LiquidityHistoryResource.get（用途待确认）

- 接口声明：`GET /liquidity/history`
- 输入字段：`scope`, `market`, `business`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/amm.py:403` · `LiquidityHistoryResource`

### INVESTMENT-067 · LiquidityRankResource.get（用途待确认）

- 接口声明：`GET /liquidity/rank`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:448` · `LiquidityRankResource`

### INVESTMENT-068 · LiquiditySliceResource.get（用途待确认）

- 接口声明：`GET /liquidity/slice`
- 输入字段：`market`, `scope`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：require_login
- 代码依据：`app/api/frontend/amm.py:500` · `LiquiditySliceResource`

### INVESTMENT-069 · LiquidityTotalSliceResource.get（用途待确认）

- 接口声明：`GET /liquidity/slice/total`
- 输入字段：`start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：require_login
- 代码依据：`app/api/frontend/amm.py:776` · `LiquidityTotalSliceResource`

### INVESTMENT-070 · LastLiquidityIncomeTotalResource.get（用途待确认）

- 接口声明：`GET /income/summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/amm.py:852` · `LastLiquidityIncomeTotalResource`

### INVESTMENT-071 · AmmInfoResource.get（用途待确认）

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:879` · `AmmInfoResource`

### INVESTMENT-072 · LiquiditySeriesResource.get（用途待确认）

- 接口声明：`GET /series`
- 输入字段：`series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:893` · `LiquiditySeriesResource`

### INVESTMENT-073 · 查看用户做市账户历史年化收益率

- 接口声明：`GET /profit_rate/history`
- 输入字段：`market`, `time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/amm.py:910` · `DayRateHistoryResource`

### INVESTMENT-074 · DIBalanceResource.get（用途待确认）

- 接口声明：`GET /balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/dual_investment.py:65` · `DIBalanceResource`

### INVESTMENT-075 · DISupportResource.get（用途待确认）

- 接口声明：`GET /support`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/dual_investment.py:75` · `DISupportResource`

### INVESTMENT-076 · DIBaseResource.get（用途待确认）

- 接口声明：`GET /base`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/dual_investment.py:109` · `DIBaseResource`

### INVESTMENT-077 · DIProductResource.get（用途待确认）

- 接口声明：`GET /product`
- 输入字段：`base`, `quote`, `di_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/dual_investment.py:152` · `DIProductResource`

### INVESTMENT-078 · DIProductDetailResource.get（用途待确认）

- 接口声明：`GET /product/<int:product_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/dual_investment.py:199` · `DIProductDetailResource`

### INVESTMENT-079 · DIQuoteResource.post（用途待确认）

- 接口声明：`POST /quote`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/dual_investment.py:266` · `DIQuoteResource`

### INVESTMENT-080 · DIOrderResource.get（用途待确认）

- 接口声明：`GET /order`
- 输入字段：`market`, `status`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/dual_investment.py:382` · `DIOrderResource`

### INVESTMENT-081 · DIOrderResource.post（用途待确认）

- 接口声明：`POST /order`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/dual_investment.py:430` · `DIOrderResource`

### INVESTMENT-082 · DIOrderDetailResource.get（用途待确认）

- 接口声明：`GET /order/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/dual_investment.py:476` · `DIOrderDetailResource`

### INVESTMENT-083 · DIHistoryResource.get（用途待确认）

- 接口声明：`GET /history`
- 输入字段：`asset`, `type`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/dual_investment.py:492` · `DIHistoryResource`

### INVESTMENT-084 · 定期理财-币种列表

- 接口声明：`GET /assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/fixed_investment.py:54` · `FixedInvestAssetListResource`

### INVESTMENT-085 · 定期理财-产品列表

- 接口声明：`GET /products`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/fixed_investment.py:95` · `FixedInvestAssetProductsResource`

### INVESTMENT-086 · 定期产品-获取剩余申购数目

- 接口声明：`GET /subscribe`
- 输入字段：`product_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fixed_investment.py:152` · `FixedInvestProductSubscribeResource`

### INVESTMENT-087 · 定期产品-申购操作

- 接口声明：`POST /subscribe`
- 输入字段：`product_id`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fixed_investment.py:173` · `FixedInvestProductSubscribeResource`

### INVESTMENT-088 · 定期产品-赎回操作

- 接口声明：`POST /redeem`
- 输入字段：`record_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fixed_investment.py:200` · `FixedInvestProductRedeemResource`

### INVESTMENT-089 · 定期理财-用户申购记录

- 接口声明：`GET /records`
- 输入字段：`asset`, `status`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fixed_investment.py:237` · `FixedInvestRecordsResource`

### INVESTMENT-090 · 定期产品-用户操作记录

- 接口声明：`GET /history`
- 输入字段：`asset`, `type`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fixed_investment.py:300` · `FixedInvestOpHistoryResource`

### INVESTMENT-091 · 定期产品-收益汇总信息

- 接口声明：`GET /profit-summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fixed_investment.py:357` · `FixedInvestProfitSummaryResource`

### INVESTMENT-092 · AccountListResource.get（用途待确认）

- 接口声明：`GET /accounts`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/investment.py:45` · `AccountListResource`

### INVESTMENT-093 · AccountHistoryResource.get（用途待确认）

- 接口声明：`GET /accounts/history`
- 输入字段：`page`, `limit`, `coin_type`, `opt`
- 显式控制：require_login
- 代码依据：`app/api/frontend/investment.py:59` · `AccountHistoryResource`

### INVESTMENT-094 · InvestmentTransferResource.get（用途待确认）

- 接口声明：`GET /transfer`
- 输入字段：`coin_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/investment.py:91` · `InvestmentTransferResource`

### INVESTMENT-095 · InvestmentTransferResource.post（用途待确认）

- 接口声明：`POST /transfer`
- 输入字段：`from_account`, `to_account`, `coin_type`, `amount`
- 显式控制：require_login
- 代码依据：`app/api/frontend/investment.py:107` · `InvestmentTransferResource`

### INVESTMENT-096 · 查看用户理财历史收益率

- 接口声明：`GET /day_rate/history`
- 输入字段：`asset`, `time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/investment.py:155` · `DayRateHistoryResource`

### INVESTMENT-097 · 理财专题页

- 接口声明：`GET /summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/investment.py:204` · `InvestmentSummaryResource`

### INVESTMENT-098 · InvestmentNewSummaryResource.get（用途待确认）

- 接口声明：`GET /summary/new`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/investment.py:328` · `InvestmentNewSummaryResource`

### INVESTMENT-099 · InvestmentRecommendResource.get（用途待确认）

- 接口声明：`GET /recommend`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/investment.py:339` · `InvestmentRecommendResource`

### INVESTMENT-100 · InvestAssetsRecommendResource.get（用途待确认）

- 接口声明：`GET /products/recommend`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/investment.py:363` · `InvestAssetsRecommendResource`

### INVESTMENT-101 · 理财记录(支持查询活期理财、定期理财和链上质押)

- 接口声明：`GET /history`
- 输入字段：`next_key`, `asset`, `type`, `bus_type`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/investment.py:430` · `InvestmentHistoryResource`

### INVESTMENT-102 · InterestPreviewResource.get（用途待确认）

- 接口声明：`GET /interest/preview`
- 输入字段：`asset`, `exist_amount`, `add_amount`
- 显式控制：require_login
- 代码依据：`app/api/frontend/investment.py:650` · `InterestPreviewResource`

### INVESTMENT-103 · StakingAccountsResource.get（用途待确认）

- 接口声明：`GET /accounts`
- 输入字段：`page`, `limit`, `order`
- 显式控制：require_login
- 代码依据：`app/api/frontend/staking.py:93` · `StakingAccountsResource`

### INVESTMENT-104 · StakingOperationResource.post（用途待确认）

- 接口声明：`POST `
- 输入字段：`asset`, `amount`
- 显式控制：require_login
- 代码依据：`app/api/frontend/staking.py:162` · `StakingOperationResource`

### INVESTMENT-105 · StakingOperationResource.delete（用途待确认）

- 接口声明：`DELETE `
- 输入字段：`asset`, `amount`
- 显式控制：require_login
- 代码依据：`app/api/frontend/staking.py:184` · `StakingOperationResource`

### INVESTMENT-106 · StakingHistoryResource.get（用途待确认）

- 接口声明：`GET /history`
- 输入字段：`asset`, `type`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/staking.py:216` · `StakingHistoryResource`

### INVESTMENT-107 · StakingIntroductionResource.get（用途待确认）

- 接口声明：`GET /introduction`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/staking.py:288` · `StakingIntroductionResource`

### INVESTMENT-108 · 策略列表 

- 接口声明：`GET /list`
- 输入字段：`type`, `status`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/strategy.py:87` · `StrategyListResource`

### INVESTMENT-109 · 现货网格-支持的市场列表 

- 接口声明：`GET /grid/spot/markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/strategy.py:248` · `SpotGridMarketsResource`

### INVESTMENT-110 · 策略市场的配置 

- 接口声明：`GET /grid/spot/config`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/strategy.py:264` · `SpotGridConfigResource`

### INVESTMENT-111 · 现货网格-策略参数推荐 

- 接口声明：`GET /grid/spot/recommend`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/strategy.py:308` · `SpotGridRecommendResource`

### INVESTMENT-112 · 现货网格-新建策略 

- 接口声明：`POST /grid/spot`
- 输入字段：`market`, `lowest_price`, `highest_price`, `grid_count`, `quote_amount`, `base_amount`, `trigger_price`, `take_profit_price`, `stop_loss_price`, `recommend_days`, `is_recommend`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True); trade_permission_validate(is_spot=True, account_id=0)
- 代码依据：`app/api/frontend/strategy.py:360` · `SpotGridListResource`

### INVESTMENT-113 · 现货网格-策略详情 

- 接口声明：`GET /grid/spot/<int:strategy_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/strategy.py:602` · `SpotGridDetailResource`

### INVESTMENT-114 · 现货网格-策略修改 

- 接口声明：`PUT /grid/spot/<int:strategy_id>`
- 输入字段：`take_profit_price`, `stop_loss_price`, `trigger_price`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/strategy.py:662` · `SpotGridDetailResource`

### INVESTMENT-115 · 现货网格-策略终止 

- 接口声明：`DELETE /grid/spot/<int:strategy_id>`
- 输入字段：`hold_asset`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/strategy.py:705` · `SpotGridDetailResource`

### INVESTMENT-116 · 现货网格-策略当前委托 

- 接口声明：`GET /grid/spot/<int:strategy_id>/pending-orders`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/strategy.py:726` · `SpotGridPendingOrderResource`

### INVESTMENT-117 · 现货网格-策略历史委托 

- 接口声明：`GET /grid/spot/<int:strategy_id>/finished-orders`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/strategy.py:792` · `SpotGridFinishedOrderResource`

### INVESTMENT-118 · 现货网格-策略收益曲线 

- 接口声明：`GET /grid/spot/profit/history`
- 输入字段：`strategy_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/strategy.py:843` · `SpotGridStrategyProfitResource`

### INVESTMENT-119 · AmmLiquidityResource.get（用途待确认）

- 接口声明：`GET /liquidity`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/amm.py:49` · `AmmLiquidityResource`

### INVESTMENT-120 · AmmAddLiquidityResource.post（用途待确认）

- 接口声明：`POST /add-liquidity`
- 输入字段：`base_ccy_amount`, `quote_ccy_amount`, `market`
- 显式控制：require_api_v2_auth(require_trading_permission=True); require_user_permission(sub_account_permissions=[SubAccountPermission.AMM])
- 代码依据：`app/api/v2/assets/amm.py:77` · `AmmAddLiquidityResource`

### INVESTMENT-121 · AmmRemoveLiquidityResource.post（用途待确认）

- 接口声明：`POST /remove-liquidity`
- 输入字段：`market`
- 显式控制：require_api_v2_auth(require_trading_permission=True); require_user_permission(sub_account_permissions=[SubAccountPermission.AMM])
- 代码依据：`app/api/v2/assets/amm.py:142` · `AmmRemoveLiquidityResource`

### INVESTMENT-122 · AmmLiquidityPoolResource.get（用途待确认）

- 接口声明：`GET /liquidity-pool`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/assets/amm.py:189` · `AmmLiquidityPoolResource`

### INVESTMENT-123 · 获取 AMM 收益记录  由于 UserLiquidityProfit 并不一定有数据，因此计算用户AMM收益有以下两种计算方法：     1. 存在记录，直接获取 UserLiquidityProfit.fee_usd     2. 缺失记录，获取 UserLiquiditySlice（用户流动性每日快照） 及 LiquiditySlice（市场流动性每日

- 接口声明：`GET /income-history`
- 输入字段：`market`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/amm.py:256` · `AmmIncomeHistoryResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/frontend/test_dual_investment.py`
- `tests/business/clients/test_wallet_staking.py`
- `tests/business/investment/test_investment_biz.py`
- `tests/business/investment/test_investment_cache.py`
- `tests/business/investment/test_investment_statistic.py`
- `tests/business/strategy/__init__.py`
- `tests/business/test_fixed_investment.py`
- `tests/business/test_staking.py`
- `tests/schedules/test_amm.py`
- `tests/schedules/test_staking.py`
- `tests/schedules/test_staking_summary.py`
- `tests/scripts/test_staking_asset_online.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
