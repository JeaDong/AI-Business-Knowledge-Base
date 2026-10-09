# 现货与市场 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### TRADING-001 · 用户-用户特殊费率列表-配置列表

- 接口声明：`GET /config`
- 输入字段：`page`, `limit`, `business_type`, `market_name`, `trade_type`, `fixed`, `start_time`, `end_time`, `search_keyword`, `active_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:79` · `UserFeeConfigResource`

### TRADING-002 · 用户-用户特殊费率列表-添加配置

- 接口声明：`POST /config`
- 输入字段：`user_id`, `fee_config`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:218` · `UserFeeConfigResource`

### TRADING-003 · 用户-用户特殊费率列表-修改配置

- 接口声明：`PUT /config`
- 输入字段：`id`, `remark`, `fee`, `business_type`, `trade_type`, `expired_time`, `fixed`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:378` · `UserFeeConfigResource`

### TRADING-004 · 用户-用户特殊费率列表-删除配置

- 接口声明：`DELETE /config`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:432` · `UserFeeConfigResource`

### TRADING-005 · 用户-CET特殊折扣配置

- 接口声明：`GET /discount/config`
- 输入字段：`page`, `limit`, `market_name`, `start_time`, `end_time`, `search_keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:477` · `UserFeeDiscountConfigResource`

### TRADING-006 · 用户-CET特殊折扣配置-新增

- 接口声明：`POST /discount/config`
- 输入字段：`user_id`, `remark`, `market_name`, `discount`, `expired_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:533` · `UserFeeDiscountConfigResource`

### TRADING-007 · 用户-CET特殊折扣配置-编辑

- 接口声明：`PUT /discount/config/<int:id_>`
- 输入字段：`remark`, `discount`, `expired_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:605` · `UserFeeDiscountConfigDetailResource`

### TRADING-008 · 用户-CET特殊折扣配置-删除

- 接口声明：`DELETE /discount/config/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fee.py:645` · `UserFeeDiscountConfigDetailResource`

### TRADING-009 · 系统 - AI任务查询 - K线分析触发列表

- 接口声明：`GET /trigger-markets`
- 输入字段：`market`, `business_type`, `interval`, `tier`, `status`, `trigger_type`, `is_triggered`, `page`, `page_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kline_ai.py:385` · `TriggerMarketResource`

### TRADING-010 · 系统 - AI任务查询 - K线分析市场分层

- 接口声明：`GET /market-tiers`
- 输入字段：`asset`, `tier`, `has_spot`, `has_perpetual`, `page`, `page_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kline_ai.py:405` · `MarketTierResource`

### TRADING-011 · 系统 - AI任务查询 - K线分析支持周期

- 接口声明：`GET /intervals`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kline_ai.py:422` · `KlineIntervalResource`

### TRADING-012 · 系统 - AI任务查询 - K线分析历史

- 接口声明：`GET /analysis-history`
- 输入字段：`market`, `business_type`, `interval`, `start_time`, `end_time`, `page`, `page_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kline_ai.py:431` · `AnalysisHistoryResource`

### TRADING-013 · 系统 - AI任务查询 - K线分析详情

- 接口声明：`GET /analysis/<int:analysis_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kline_ai.py:449` · `AnalysisDetailResource`

### TRADING-014 · 用户-做市商列表

- 接口声明：`GET `
- 输入字段：`search_keyword`, `maker_type`, `level`, `order`, `page`, `limit`, `appraisal_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:80` · `MarketMakerResource`

### TRADING-015 · 用户-添加做市商

- 接口声明：`POST `
- 输入字段：`maker_type`, `user_id`, `real_level`, `lock_level`, `remark`, `expired_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:275` · `MarketMakerResource`

### TRADING-016 · 用户-删除做市商

- 接口声明：`DELETE `
- 输入字段：`maker_type`, `user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:403` · `MarketMakerResource`

### TRADING-017 · 用户-编辑做市商

- 接口声明：`PATCH `
- 输入字段：`maker_type`, `user_id`, `remark`, `lock_level`, `expired_time`, `appraisal_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:487` · `MarketMakerResource`

### TRADING-018 · 用户-内部做市商-内部做市商列表

- 接口声明：`GET /inner-list`
- 输入字段：`user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:580` · `InnerMarketMakerResource`

### TRADING-019 · 用户-内部做市商-添加内部做市商

- 接口声明：`POST /inner-list`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:622` · `InnerMarketMakerResource`

### TRADING-020 · 用户-内部做市商-编辑内部做市商

- 接口声明：`PUT /inner-list`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:696` · `InnerMarketMakerResource`

### TRADING-021 · 用户-内部做市商-删除内部做市商

- 接口声明：`DELETE /inner-list`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:731` · `InnerMarketMakerResource`

### TRADING-022 · 用户-做市商-查询做市商日报接收邮箱 

- 接口声明：`GET /report-email`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:786` · `MarketMakerReportEmailResource`

### TRADING-023 · 用户-做市商-新增做市商日报接收邮箱 

- 接口声明：`POST /report-email`
- 输入字段：`user_id`, `email`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:801` · `MarketMakerReportEmailResource`

### TRADING-024 · 用户-做市商-编辑做市商日报接收邮箱 

- 接口声明：`PUT /report-email`
- 输入字段：`id`, `email`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:844` · `MarketMakerReportEmailResource`

### TRADING-025 · 用户-做市商-删除做市商日报接收邮箱 

- 接口声明：`DELETE /report-email`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:887` · `MarketMakerReportEmailResource`

### TRADING-026 · 用户-做市商变更记录

- 接口声明：`GET /change-history`
- 输入字段：`search_keyword`, `maker_type`, `change_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:941` · `MarketMakerChangeHistoryResource`

### TRADING-027 · 做市商-做市商交易记录

- 接口声明：`GET /deals`
- 输入字段：`id`, `start_date`, `end_date`, `page`, `system`, `limit`, `maker_type`, `report_type`, `export`, `search_keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:1073` · `UserTradeSummaryRank`

### TRADING-028 · 做市商-市场交易记录

- 接口声明：`GET /market/deals`
- 输入字段：`system`, `report_type`, `market`, `start_date`, `end_date`, `user_id`, `search_keyword`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:1172` · `MarketMakerMarketDealsResource`

### TRADING-029 · 做市商申请列表

- 接口声明：`GET /application-list`
- 输入字段：`user_id`, `location_code`, `type`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:1273` · `MarketMakerApplyListResource`

### TRADING-030 · 做市商申请详情

- 接口声明：`GET /application/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:1355` · `MarketMakerApplyDetailResource`

### TRADING-031 · 做市商申请编辑备注

- 接口声明：`PUT /application/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/market_maker.py:1373` · `MarketMakerApplyDetailResource`

### TRADING-032 · 现货-链上交易-链上交易明细-列表

- 接口声明：`GET `
- 输入字段：`order_id`, `wallet_order_id`, `status`, `user_id`, `side`, `from_asset`, `to_asset`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/order.py:66` · `OnchainOrderResource`

### TRADING-033 · 运营-营销Banner-获取banners列表

- 接口声明：`GET /banners`
- 输入字段：`status`, `lang`, `type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:45` · `MarketBannersResource`

### TRADING-034 · 运营-营销Banner-创建banner

- 接口声明：`POST /banners`
- 输入字段：`name`, `type`, `lang`, `begin_at`, `end_at`, `url`, `code`, `refer_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:101` · `MarketBannersResource`

### TRADING-035 · 运营-营销Banner-获取单条banner

- 接口声明：`GET /banners/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:162` · `MarketBannerContentResource`

### TRADING-036 · 运营-营销Banner-编辑banner

- 接口声明：`PATCH /banners/<int:id_>`
- 输入字段：`name`, `lang`, `begin_at`, `end_at`, `url`, `refer_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:184` · `MarketBannerContentResource`

### TRADING-037 · 运营-营销Banner-删除、下架

- 接口声明：`DELETE /banners/<int:id_>`
- 输入字段：`is_offline`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:220` · `MarketBannerContentResource`

### TRADING-038 · 运营-营销Banner-banners上移

- 接口声明：`POST /banners/<int:id_>/sort_id`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:255` · `MarketBannerSortIDResource`

### TRADING-039 · 运营-营销Banner-获取单条banner内容

- 接口声明：`GET /banners/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:288` · `MarketBannerContentLangResource`

### TRADING-040 · 运营-营销Banner-编辑banner内容

- 接口声明：`POST /banners/<int:id_>/langs/<lang>/img`
- 输入字段：`same_as`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:315` · `MarketBannerContentImageResource`

### TRADING-041 · 运营-营销Banner-删除banner

- 接口声明：`DELETE /banners/<int:id_>/langs/<lang>/img`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:375` · `MarketBannerContentImageResource`

### TRADING-042 · 运营-营销Banner-banner拖拽排序

- 接口声明：`POST /banners/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/marketing.py:403` · `MarketBannerSortResource`

### TRADING-043 · 报表-现货交易-全站交易

- 接口声明：`GET /deals`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:74` · `DailySpotDealsResource`

### TRADING-044 · 报表-现货交易-交易区详情

- 接口声明：`GET /deal-detail`
- 输入字段：`report_date`, `order`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:152` · `DailySpotDealDetailResource`

### TRADING-045 · 报表-现货交易-交易区

- 接口声明：`GET /blocks`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `trading_area`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:219` · `DailySpotBlocksResource`

### TRADING-046 · 报表-现货交易-交易区详情

- 接口声明：`GET /block-detail`
- 输入字段：`report_date`, `order`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:322` · `DailySpotBlockDetailResource`

### TRADING-047 · 报表-现货交易-交易市场

- 接口声明：`GET /markets`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `market`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:413` · `DailySpotMarketsResource`

### TRADING-048 · 报表-现货交易-交易市场详情

- 接口声明：`GET /market-detail`
- 输入字段：`report_date`, `order`, `trading_area`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:578` · `DailySpotMarketDetailResource`

### TRADING-049 · 报表-现货交易-交易币种

- 接口声明：`GET /coin`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `coin`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:714` · `DailySpotCoinResource`

### TRADING-050 · 报表-现货交易-交易币种-异步下载

- 接口声明：`GET /coin-async-download`
- 输入字段：`report_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:856` · `DailySpotCoinAsyncDownloadResource`

### TRADING-051 · 报表-现货交易-交易币种

- 接口声明：`GET /coin-detail`
- 输入字段：`report_date`, `order`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:882` · `DailySpotCoinDetailResource`

### TRADING-052 · 报表-资产报表-币币

- 接口声明：`GET /balance`
- 输入字段：`query_date`, `asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:977` · `DailySpotBalanceResource`

### TRADING-053 · 报表-资产报表-币币-币种详情

- 接口声明：`GET /asset-balance`
- 输入字段：`asset`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1016` · `DailySpotAssetBalanceResource`

### TRADING-054 · 报表-现货交易-充提报表

- 接口声明：`GET /deposit-withdrawal`
- 输入字段：`asset`, `start_date`, `end_date`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1062` · `DepositWithdrawalResource`

### TRADING-055 · 报表-充提报表-未KYC充提-全站

- 接口声明：`GET /unkyc-deposit-withdrawal`
- 输入字段：`start_date`, `end_date`, `report_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1172` · `UnkycDepositWithdrawalResource`

### TRADING-056 · 报表-充提报表-未KYC充提-币种

- 接口声明：`GET /unkyc-deposit-withdrawal-asset`
- 输入字段：`asset`, `start_date`, `end_date`, `report_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1214` · `UnkycDepositWithdrawalAssetResource`

### TRADING-057 · 报表-充提报表-未KYC充提-币种详情

- 接口声明：`GET /unkyc-deposit-withdrawal-asset-detail`
- 输入字段：`report_date`, `report_type`, `sort_name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1273` · `UnkycDepositWithdrawalAssetDetailResource`

### TRADING-058 · 报表-现货交易-充提报表-异步下载

- 接口声明：`GET /deposit-withdrawal-async-download`
- 输入字段：`start_time`, `end_time`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1307` · `DepositWithdrawalAsyncDownloadResource`

### TRADING-059 · 报表-现货交易-Viabtc充值报表-币种-异步下载

- 接口声明：`GET /deposit-withdrawal-local-async-download`
- 输入字段：`start_time`, `end_time`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1337` · `DepositWithdrawalLocalAsyncDownloadResource`

### TRADING-060 · 报表-现货交易-公链充提报表

- 接口声明：`GET /chain-deposit-withdrawal`
- 输入字段：`chain`, `start_date`, `end_date`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1366` · `ChainDepositWithdrawalResource`

### TRADING-061 · 报表-现货交易-充提报表-公链详情

- 接口声明：`GET /deposit-withdrawal-chain-detail`
- 输入字段：`report_date`, `report_type`, `sort_name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1452` · `DepositWithdrawalChainDetailResource`

### TRADING-062 · 报表-充提报表-链上充提币种报表

- 接口声明：`GET /chain-asset-deposit-withdrawal`
- 输入字段：`asset`, `start_date`, `end_date`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1502` · `ChainAssetDepositWithdrawalResource`

### TRADING-063 · 报表-充提报表-链上充提币种报表-币种详情

- 接口声明：`GET /deposit-withdrawal-chain-asset-detail`
- 输入字段：`report_date`, `report_type`, `sort_name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1570` · `DepositWithdrawalChainAssetDetailResource`

### TRADING-064 · 报表-现货交易-充提报表-币种详情

- 接口声明：`GET /deposit-withdrawal-asset-detail`
- 输入字段：`asset`, `report_date`, `report_type`, `sort_name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1619` · `DepositWithdrawalAssetDetailResource`

### TRADING-065 · 报表-内部转账

- 接口声明：`GET /inner-transfer`
- 输入字段：`asset`, `report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1679` · `InnerTransferResource`

### TRADING-066 · 报表-内部转账-异步下载

- 接口声明：`GET /inner-transfer-async-download`
- 输入字段：`report_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1751` · `InnerTransferAsyncDownloadResource`

### TRADING-067 · 报表-币种内部转账

- 接口声明：`GET /inner-asset-transfer`
- 输入字段：`sort_name`, `report_date`, `page`, `limit`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1777` · `InnerAssetTransferResource`

### TRADING-068 · 报表-现货报表-AMM市场

- 接口声明：`GET /amm-market`
- 输入字段：`market`, `report_date`, `page`, `limit`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1811` · `AmmMarketResource`

### TRADING-069 · 报表-做市报表-现货

- 接口声明：`GET /maker-deals`
- 输入字段：`report_type`, `maker_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1906` · `DailySpotMakerDealsResource`

### TRADING-070 · 报表-做市报表-现货交易市场详情

- 接口声明：`GET /maker-market-detail`
- 输入字段：`report_date`, `order`, `trading_area`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:1977` · `DailySpotMakerMarketDetailResource`

### TRADING-071 · 报表-现货交易-深度报表

- 接口声明：`GET /depth`
- 输入字段：`report_type`, `start_date`, `end_date`, `market`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:2074` · `DailySpotDepthResource`

### TRADING-072 · 报表-现货交易-深度详情

- 接口声明：`GET /depth-detail`
- 输入字段：`report_date`, `order`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/spot.py:2178` · `DailySpotDepthDetailResource`

### TRADING-073 · 市场信息

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:62` · `MarketInfoResource`

### TRADING-074 · 系统-市场配置

- 接口声明：`GET /markets`
- 输入字段：`trading_area`, `mode`, `status`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:109` · `MarketsResource`

### TRADING-075 · 系统-市场配置-添加市场

- 接口声明：`POST /markets`
- 输入字段：`trading_area`, `mode`, `default_depth`, `depths`, `base_asset`, `base_asset_precision`, `quote_asset`, `quote_asset_precision`, `taker_fee_rate`, `maker_fee_rate`, `max_price_deviation`, `opening_price_asset`, `opening_price`, `started_at`, `bidding_matching_started_at`, `bidding_ended_at`, `countdown_ended_at`, `is_stablecoin_market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:169` · `MarketsResource`

### TRADING-076 · 系统-市场配置-市场

- 接口声明：`GET /markets/<name>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:286` · `MarketResource`

### TRADING-077 · 系统-市场配置-编辑市场

- 接口声明：`PATCH /markets/<name>`
- 输入字段：`mode`, `default_depth`, `depths`, `base_asset_precision`, `quote_asset_precision`, `taker_fee_rate`, `maker_fee_rate`, `max_price_deviation`, `opening_price_asset`, `opening_price`, `started_at`, `bidding_matching_started_at`, `bidding_ended_at`, `countdown_ended_at`, `status`, `is_stablecoin_market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:296` · `MarketResource`

### TRADING-078 · 系统-市场配置-编辑市场下架配置

- 接口声明：`PATCH /markets/offline/<name>`
- 输入字段：`ended_at`, `trading_disabled`, `api_spot_trading_disabled`, `offline_visible`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:519` · `MarketOfflineResource`

### TRADING-079 · 系统-市场配置-获取市场下架文案

- 接口声明：`GET /markets/offline-contents`
- 输入字段：`market`, `market_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:597` · `MarketOfflineContentsResource`

### TRADING-080 · 系统-市场配置-市场下架文案-保存

- 接口声明：`PUT /markets/offline-contents/<market_type>/<int:id_>/langs/<lang>`
- 输入字段：`content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:663` · `MarketOfflineLangContentResource`

### TRADING-081 · 市场撤单

- 接口声明：`DELETE /markets/<name>/orders`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:710` · `MarketOrdersResource`

### TRADING-082 · 现货市场-撤销兑换订单

- 接口声明：`DELETE /markets/<name>/exhcange-orders`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:726` · `MarketExchangeOrdersResource`

### TRADING-083 · 市场配置辅助

- 接口声明：`GET /market-help-me`
- 输入字段：`quote_asset`, `opening_price`, `opening_price_asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:745` · `MarketAutoGenerationResource`

### TRADING-084 · 币种汇率

- 接口声明：`GET /asset-rates`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:762` · `AssetRatesResource`

### TRADING-085 · 币币-币币深度列表

- 接口声明：`GET /trade-depth`
- 输入字段：`market`, `side`, `is_stop`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:781` · `CoinTradeDepthResource`

### TRADING-086 · 币币-币币深度列表-币币最新成交

- 接口声明：`GET /latest-deals`
- 输入字段：`market`, `last_id`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:827` · `LatestDeals`

### TRADING-087 · 币币-交易排名-实时净买卖

- 接口声明：`GET /realtime-net-rank`
- 输入字段：`market`, `asset`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:862` · `RealtimeNetRank`

### TRADING-088 · 币币-交易排名-成交价排名

- 接口声明：`GET /realtime-price-rank`
- 输入字段：`market`, `bid_rank`, `ask_rank`, `last_hour`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:969` · `RealtimePriceRank`

### TRADING-089 · 币币-交易排名-实时成交量

- 接口声明：`GET /realtime-deal-rank`
- 输入字段：`market`, `asset`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1092` · `RealtimeDealRank`

### TRADING-090 · 币币-交易排名-币币历史净买卖

- 接口声明：`GET /history-net-rank`
- 输入字段：`market`, `asset`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1175` · `HistoryNetRank`

### TRADING-091 · 币币-交易排名-币币历史成交量

- 接口声明：`GET /history-deal-rank`
- 输入字段：`market`, `asset`, `time_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1320` · `HistoryDealRank`

### TRADING-092 · 币币-交易排名-用户总成交量

- 接口声明：`GET /user-trade-summary-rank`
- 输入字段：`id`, `start_date`, `end_date`, `page`, `sort_type`, `limit`, `user_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1449` · `UserTradeSummaryRank`

### TRADING-093 · 币币-交易排名-用户总成交手续费排名

- 接口声明：`GET /user-trade-fee-summary-rank`
- 输入字段：`id`, `start_date`, `end_date`, `page`, `sort_type`, `limit`, `user_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1616` · `UserTradeFeeSummaryRank`

### TRADING-094 · 币币-AMM-市场配置

- 接口声明：`GET /amm-market-config`
- 输入字段：`trading_area`, `amm_type`, `status`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1754` · `AmmMarketConfig`

### TRADING-095 · 币币-AMM-添加市场

- 接口声明：`POST /amm-market-config`
- 输入字段：`name`, `amm_type`, `fee_refund_rate`, `delta`, `initial_price`, `allow_in_bidding`, `min_price`, `max_price`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1799` · `AmmMarketConfig`

### TRADING-096 · 币币-AMM-编辑市场

- 接口声明：`PUT /amm-market-config`
- 输入字段：`name`, `amm_type`, `fee_refund_rate`, `delta`, `initial_price`, `allow_in_bidding`, `min_price`, `max_price`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1896` · `AmmMarketConfig`

### TRADING-097 · 币币-AMM-上下架市场

- 接口声明：`PATCH /amm-market-config`
- 输入字段：`name`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:1981` · `AmmMarketConfig`

### TRADING-098 · 币币-AMM-撤销流动性

- 接口声明：`DELETE /amm-market-config`
- 输入字段：`name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:2010` · `AmmMarketConfig`

### TRADING-099 · 币币-AMM市场列表

- 接口声明：`GET /amm-markets`
- 输入字段：`order`, `market`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:2039` · `AMMMarketResource`

### TRADING-100 · 币币-用户流动性排行

- 接口声明：`GET /liquidity-rank`
- 输入字段：`market`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:2123` · `LiquidityRankResource`

### TRADING-101 · 币币-用户做市记录

- 接口声明：`GET /liquidity-history`
- 输入字段：`market`, `user_id`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/spot.py:2190` · `LiquidityHistoryResource`

### TRADING-102 · AnalysisResource.get（用途待确认）

- 接口声明：`GET /analysis`
- 输入字段：`market`, `business_type`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/kline_ai.py:21` · `AnalysisResource`

### TRADING-103 · MarketsResource.get（用途待确认）

- 接口声明：`GET /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:39` · `MarketsResource`

### TRADING-104 · MarketListResource.get（用途待确认）

- 接口声明：`GET /list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:58` · `MarketListResource`

### TRADING-105 · MarketStatusListResource.get（用途待确认）

- 接口声明：`GET /status`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:71` · `MarketStatusListResource`

### TRADING-106 · MarketOfflineInfoResource.get（用途待确认）

- 接口声明：`GET /offline-info`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:88` · `MarketOfflineInfoResource`

### TRADING-107 · MarketConfigResource.get（用途待确认）

- 接口声明：`GET /config`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:111` · `MarketConfigResource`

### TRADING-108 · RateResource.get（用途待确认）

- 接口声明：`GET /rate/<market_name>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:127` · `RateResource`

### TRADING-109 · AssetsResource.get（用途待确认）

- 接口声明：`GET /asset`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:169` · `AssetsResource`

### TRADING-110 · CurrenciesResource.get（用途待确认）

- 接口声明：`GET /currency`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:178` · `CurrenciesResource`

### TRADING-111 · CurrencyRatesResource.get（用途待确认）

- 接口声明：`GET /currency/rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:187` · `CurrencyRatesResource`

### TRADING-112 · TODO: 待移除，后续币种汇率与法币汇率分开两个接口

- 接口声明：`GET /usd/exchange/rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:196` · `Prices`

### TRADING-113 · AssetPrices.get（用途待确认）

- 接口声明：`GET /asset/prices`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:215` · `AssetPrices`

### TRADING-114 · AssetRecentChangeRates.get（用途待确认）

- 接口声明：`GET /asset/recent-change-rates`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:225` · `AssetRecentChangeRates`

### TRADING-115 · FiatPrices.get（用途待确认）

- 接口声明：`GET /fiat/prices`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:234` · `FiatPrices`

### TRADING-116 · MarketIndexPriceListResource.get（用途待确认）

- 接口声明：`GET /index/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:245` · `MarketIndexPriceListResource`

### TRADING-117 · 获取订阅列表

- 接口声明：`GET /follow`
- 输入字段：`trade_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:265` · `FollowMarketListResource`

### TRADING-118 · 单个订阅

- 接口声明：`POST /follow`
- 输入字段：`market_type`, `trade_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:288` · `FollowMarketListResource`

### TRADING-119 · 批量订阅

- 接口声明：`POST /batch-follow`
- 输入字段：`market_list`, `trade_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:330` · `FollowMarketBatchListResource`

### TRADING-120 · 重新排序

- 接口声明：`POST /follow/reorder`
- 输入字段：`follow_ids`, `trade_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:372` · `FollowMarketReorderResource`

### TRADING-121 · FollowMarketResource.delete（用途待确认）

- 接口声明：`DELETE /follow/<int:follow_market_id>`
- 输入字段：`trade_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:409` · `FollowMarketResource`

### TRADING-122 · MarketPriceAlertsResouce.get（用途待确认）

- 接口声明：`GET /price/alerts`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:447` · `MarketPriceAlertsResouce`

### TRADING-123 · MarketPriceAlertsResouce.post（用途待确认）

- 接口声明：`POST /price/alerts`
- 输入字段：`market`, `price`, `direction`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:457` · `MarketPriceAlertsResouce`

### TRADING-124 · MarketPriceAlertsResouce.delete（用途待确认）

- 接口声明：`DELETE /price/alerts`
- 输入字段：`market`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:469` · `MarketPriceAlertsResouce`

### TRADING-125 · MarketPriceAlertResource.delete（用途待确认）

- 接口声明：`DELETE /price/alerts/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:483` · `MarketPriceAlertResource`

### TRADING-126 · MarketPriceNoticeResource.get（用途待确认）

- 接口声明：`GET /price/notice`
- 输入字段：`market`, `trade_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:494` · `MarketPriceNoticeResource`

### TRADING-127 · MarketPriceNoticeResource.post（用途待确认）

- 接口声明：`POST /price/notice`
- 输入字段：`market`, `value`, `direction`, `ttl_type`, `trade_type`, `notice_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:537` · `MarketPriceNoticeResource`

### TRADING-128 · 删除提醒记录

- 接口声明：`PUT /price/notice`
- 输入字段：`notice_ids`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:602` · `MarketPriceNoticeResource`

### TRADING-129 · MarketPriceNoticeDetailResource.patch（用途待确认）

- 接口声明：`PATCH /price/notice/<int:id_>`
- 输入字段：`market`, `value`, `direction`, `ttl_type`, `notice_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:625` · `MarketPriceNoticeDetailResource`

### TRADING-130 · MarketPriceNoticeDetailResource.put（用途待确认）

- 接口声明：`PUT /price/notice/<int:id_>`
- 输入字段：`state`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:680` · `MarketPriceNoticeDetailResource`

### TRADING-131 · MarketKlineResource.get（用途待确认）

- 接口声明：`GET /kline`
- 输入字段：`market`, `start_time`, `end_time`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:697` · `MarketKlineResource`

### TRADING-132 · 市场深度数据 

- 接口声明：`GET /depth`
- 输入字段：`market`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:743` · `MarketDepthResource`

### TRADING-133 · MonthlyMarketChangeRateResource.get（用途待确认）

- 接口声明：`GET /change-rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:774` · `MonthlyMarketChangeRateResource`

### TRADING-134 · FloatWindowsResource.post（用途待确认）

- 接口声明：`POST /float-windows`
- 输入字段：`display_type`, `market_float_windows`, `wheel_interval`, `page_limit`, `rate_status`
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:839` · `FloatWindowsResource`

### TRADING-135 · FloatWindowsResource.get（用途待确认）

- 接口声明：`GET /float-windows`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/market.py:875` · `FloatWindowsResource`

### TRADING-136 · 批量获取市场实时行情，用于 客户端行情组件 展示  Args:     markets (str): 逗号分隔的市场列表，每项格式为 trade_type:market，如 spot:BTCUSDT,perpetual:BTCUSDT，最多 10 个  Returns:     market (str): 市场名称     trade_type (str):

- 接口声明：`GET /widget`
- 输入字段：`markets`, `with_kline`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market.py:912` · `MarketWidgetResource`

### TRADING-137 · MarketMakerLevelResource.get（用途待确认）

- 接口声明：`GET /level`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market_maker.py:43` · `MarketMakerLevelResource`

### TRADING-138 · ContractMarketMakerLevelResource.get（用途待确认）

- 接口声明：`GET /contract/level`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/market_maker.py:77` · `ContractMarketMakerLevelResource`

### TRADING-139 · MarketMakerResource.get（用途待确认）

- 接口声明：`GET /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/market_maker.py:117` · `MarketMakerResource`

### TRADING-140 · ContractMarketMakerResource.get（用途待确认）

- 接口声明：`GET /contract`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/market_maker.py:162` · `ContractMarketMakerResource`

### TRADING-141 · 做市商日报接收邮箱列表 

- 接口声明：`GET /report/emails`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/market_maker.py:213` · `MarketMakerReportEmailsResource`

### TRADING-142 · 新增做市商日报接收邮箱 

- 接口声明：`POST /report/emails`
- 输入字段：`email`, `remark`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/market_maker.py:241` · `MarketMakerReportEmailsResource`

### TRADING-143 · 删除做市商日报接收邮箱 

- 接口声明：`DELETE /report/emails/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/market_maker.py:285` · `MarketMakerReportEmailDetailResource`

### TRADING-144 · 获取做市商申请信息 

- 接口声明：`GET /application`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/market_maker.py:313` · `MarketMakerApplyResource`

### TRADING-145 · 提交做市商申请 

- 接口声明：`POST /application`
- 输入字段：`name`, `contact_name`, `contact_info`, `city`, `types`, `source`, `introduction`, `trade_volume_images`, `official_website`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/market_maker.py:326` · `MarketMakerApplyResource`

### TRADING-146 · OnchainQuoteResource.get（用途待确认）

- 接口声明：`GET /quote`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:65` · `OnchainQuoteResource`

### TRADING-147 · OnchainOrderResource.post（用途待确认）

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:100` · `OnchainOrderResource`

### TRADING-148 · OnchainStopOrderResource.post（用途待确认）

- 接口声明：`POST /stop`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:142` · `OnchainStopOrderResource`

### TRADING-149 · OnchainStopOrderResource.delete（用途待确认）

- 接口声明：`DELETE /stop`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:189` · `OnchainStopOrderResource`

### TRADING-150 · CancelOnchainStopOrderResource.post（用途待确认）

- 接口声明：`POST /stop/cancel`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:213` · `CancelOnchainStopOrderResource`

### TRADING-151 · OrderStatsResource.get（用途待确认）

- 接口声明：`GET /stats`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:231` · `OrderStatsResource`

### TRADING-152 · PendingTradedTokensResource.get（用途待确认）

- 接口声明：`GET /pending/traded-tokens`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:391` · `PendingTradedTokensResource`

### TRADING-153 · FinishedTradedTokensResource.get（用途待确认）

- 接口声明：`GET /finished/traded-tokens`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:404` · `FinishedTradedTokensResource`

### TRADING-154 · PendingOrderListResource.get（用途待确认）

- 接口声明：`GET /pending`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:417` · `PendingOrderListResource`

### TRADING-155 · FinishedOrderListResource.get（用途待确认）

- 接口声明：`GET /finished`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:436` · `FinishedOrderListResource`

### TRADING-156 · StopPendingTradedTokensResource.get（用途待确认）

- 接口声明：`GET /stop/pending/traded-tokens`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:552` · `StopPendingTradedTokensResource`

### TRADING-157 · StopFinishedTradedTokensResource.get（用途待确认）

- 接口声明：`GET /stop/finished/traded-tokens`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:565` · `StopFinishedTradedTokensResource`

### TRADING-158 · PendingStopOrderListResource.get（用途待确认）

- 接口声明：`GET /stop/pending`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:578` · `PendingStopOrderListResource`

### TRADING-159 · FinishedStopOrderListResource.get（用途待确认）

- 接口声明：`GET /stop/finished`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/order.py:597` · `FinishedStopOrderListResource`

### TRADING-160 · LimitOrderResource.post（用途待确认）

- 接口声明：`POST /limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login; trade_permission_validate(is_spot=True)
- 代码依据：`app/api/frontend/order.py:305` · `LimitOrderResource`

### TRADING-161 · 预览分段委托订单的子订单列表

- 接口声明：`GET /scaled`
- 输入字段：`min_price`, `max_price`, `total_segment`, `total_amount`, `mode`, `market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/order.py:386` · `ScaledOrderResource`

### TRADING-162 · 提交分段委托订单

- 接口声明：`POST /scaled`
- 输入字段：`min_price`, `max_price`, `total_segment`, `total_amount`, `mode`, `market`, `side`, `account_id`
- 显式控制：require_login; trade_permission_validate(is_spot=True)
- 代码依据：`app/api/frontend/order.py:433` · `ScaledOrderResource`

### TRADING-163 · OrderModifyResource.post（用途待确认）

- 接口声明：`POST /modify`
- 输入字段：`amount`, `price`, `market`, `order_id`, `account_id`
- 显式控制：require_login; trade_permission_validate(is_spot=True)
- 代码依据：`app/api/frontend/order.py:576` · `OrderModifyResource`

### TRADING-164 · OrderModifyStopResource.post（用途待确认）

- 接口声明：`POST /stop/modify`
- 输入字段：`amount`, `price`, `stop_price`, `market`, `order_id`, `account_id`, `stop_type`
- 显式控制：require_login; trade_permission_validate(is_spot=True)
- 代码依据：`app/api/frontend/order.py:647` · `OrderModifyStopResource`

### TRADING-165 · MarketOrderResource.post（用途待确认）

- 接口声明：`POST /market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login; trade_permission_validate(is_spot=True)
- 代码依据：`app/api/frontend/order.py:748` · `MarketOrderResource`

### TRADING-166 · StopLimitOrderResource.post（用途待确认）

- 接口声明：`POST /stop/limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login; trade_permission_validate(is_spot=True)
- 代码依据：`app/api/frontend/order.py:868` · `StopLimitOrderResource`

### TRADING-167 · StopMarketOrderResource.post（用途待确认）

- 接口声明：`POST /stop/market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login; trade_permission_validate(is_spot=True)
- 代码依据：`app/api/frontend/order.py:967` · `StopMarketOrderResource`

### TRADING-168 · FinishedOrderListResource.get（用途待确认）

- 接口声明：`GET /finished`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1106` · `FinishedOrderListResource`

### TRADING-169 · FinishedOrderResource.get（用途待确认）

- 接口声明：`GET /finished/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1162` · `FinishedOrderResource`

### TRADING-170 · PendingOrderListResource.get（用途待确认）

- 接口声明：`GET /pending`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1236` · `PendingOrderListResource`

### TRADING-171 · PendingOrderListResource.delete（用途待确认）

- 接口声明：`DELETE /pending`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1276` · `PendingOrderListResource`

### TRADING-172 · PendingOrderResource.get（用途待确认）

- 接口声明：`GET /pending/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1310` · `PendingOrderResource`

### TRADING-173 · PendingOrderResource.delete（用途待确认）

- 接口声明：`DELETE /pending/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1341` · `PendingOrderResource`

### TRADING-174 · OrderDealListResource.get（用途待确认）

- 接口声明：`GET /deals`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1399` · `OrderDealListResource`

### TRADING-175 · StopFinishedOrderListResource.get（用途待确认）

- 接口声明：`GET /stop/finished`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1476` · `StopFinishedOrderListResource`

### TRADING-176 · StopPendingOrderListResource.get（用途待确认）

- 接口声明：`GET /stop/pending`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1537` · `StopPendingOrderListResource`

### TRADING-177 · StopPendingOrderListResource.delete（用途待确认）

- 接口声明：`DELETE /stop/pending`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1563` · `StopPendingOrderListResource`

### TRADING-178 · StopPendingOrderResource.delete（用途待确认）

- 接口声明：`DELETE /stop/pending/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1579` · `StopPendingOrderResource`

### TRADING-179 · StopOrderSummaryResource.get（用途待确认）

- 接口声明：`GET /stop-order-summary/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/order.py:1613` · `StopOrderSummaryResource`

### TRADING-180 · MarketListResource.get（用途待确认）

- 接口声明：`GET /list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:38` · `MarketListResource`

### TRADING-181 · MarginMarketResource.get（用途待确认）

- 接口声明：`GET /margin-market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:50` · `MarginMarketResource`

### TRADING-182 · USD2CNYRateResource.get（用途待确认）

- 接口声明：`GET /usd2cny`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:59` · `USD2CNYRateResource`

### TRADING-183 · CurrencyRateResource.get（用途待确认）

- 接口声明：`GET /currency_rate`
- 输入字段：`from_asset`, `to_aset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:73` · `CurrencyRateResource`

### TRADING-184 · MarketPriceResource.get（用途待确认）

- 接口声明：`GET /price`
- 输入字段：`from_coin_type`, `to_coin_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:91` · `MarketPriceResource`

### TRADING-185 · example return { # 正常指数 "BTCUSDT": {     "prec": 2,     "sources": [         {           "exchange": "huobiglobal",           "trade_url": "https://api.huobi.pro/market/trade?symbo

- 接口声明：`GET /index/new_config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:106` · `MarketIndexNewConfigResource`

### TRADING-186 · RatesResource.get（用途待确认）

- 接口声明：`GET /rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:214` · `RatesResource`

### TRADING-187 · AmmMarketListResource.get（用途待确认）

- 接口声明：`GET /amm/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:224` · `AmmMarketListResource`

### TRADING-188 · AssetsResource.get（用途待确认）

- 接口声明：`GET /assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:281` · `AssetsResource`

### TRADING-189 · AssetRecentChangeRatesResource.get（用途待确认）

- 接口声明：`GET /assets/recent-change-rates`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:299` · `AssetRecentChangeRatesResource`

### TRADING-190 · AssetPriceResource.get（用途待确认）

- 接口声明：`GET /assets/close-price`
- 输入字段：`date_`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:307` · `AssetPriceResource`

### TRADING-191 · AssetsRankResource.get（用途待确认）

- 接口声明：`GET /assets-rank`
- 输入字段：`sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:319` · `AssetsRankResource`

### TRADING-192 · OnchainTokenListResource.get（用途待确认）

- 接口声明：`GET /onchain/token`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/market.py:337` · `OnchainTokenListResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/admin/test_kline_ai.py`
- `tests/api/frontend/test_activity_tab_ordering.py`
- `tests/api/frontend/test_kline_ai.py`
- `tests/business/kline_ai/__init__.py`
- `tests/business/kline_ai/test_kline_agent.py`
- `tests/business/kline_ai/test_kline_analyzer.py`
- `tests/business/kline_ai/test_kline_back_test_agent.py`
- `tests/business/kline_ai/test_kline_trigger_engine.py`
- `tests/business/kline_ai/test_pandas_api_compatibility.py`
- `tests/business/onchain/test_order.py`
- `tests/business/push/test_market_push_association.py`
- `tests/business/test_fee.py`
- `tests/business/test_scaled_order.py`
- `tests/schedules/test_spot_reserve_ratio_notice.py`
- `tests/utils/test_kline_online_runtime_patch.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
