# 法币与 P2P · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### P2P-001 · 法币-快捷支付-订单记录

- 接口声明：`GET /orders`
- 输入字段：`user_id`, `payment_id`, `asset`, `fiat_currency`, `third_party`, `payment_method`, `order_type`, `status`, `created_at_start`, `created_at_end`, `finished_at_start`, `finished_at_end`, `canceled_at_start`, `canceled_at_end`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/direct_fiat.py:59` · `OrdersResource`

### P2P-002 · 法币-快捷购币明细

- 接口声明：`GET /order-details`
- 输入字段：`order_type`, `asset`, `fiat_currency`, `third_party`, `search_keyword`, `status`, `country_code`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fiat.py:51` · `OrderDetailsResource`

### P2P-003 · 法币-活动列表

- 接口声明：`GET /activities`
- 输入字段：`status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fiat.py:212` · `FiatActivitiesResource`

### P2P-004 · 法币-活动详情

- 接口声明：`GET /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fiat.py:268` · `FiatActivityResource`

### P2P-005 · 运营-活动编辑/新建

- 接口声明：`PATCH /activity/<int:id_>`
- 输入字段：`partner`, `name`, `is_top`, `begin_at`, `end_at`, `activity_value`, `fiats`, `assets`, `side`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fiat.py:308` · `FiatActivityResource`

### P2P-006 · 运营-活动删除

- 接口声明：`DELETE /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fiat.py:399` · `FiatActivityResource`

### P2P-007 · 运营-活动上移

- 接口声明：`POST /activity/<int:id_>/sort_id`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/fiat.py:428` · `FiatActivitySortIDResource`

### P2P-008 · 运营-WEB-p2p主页运营位

- 接口声明：`GET `
- 输入字段：`name`, `platform`, `status`, `display_to_merchant`, `content_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/p2p.py:69` · `P2pActivityListResource`

### P2P-009 · 运营-WEB-p2p主页运营位详情

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/p2p.py:123` · `P2pActivityDetailResource`

### P2P-010 · 运营-WEB-新建/编辑p2p主页运营位

- 接口声明：`PUT /<int:id_>`
- 输入字段：`name`, `platform`, `content_type`, `display_to_merchant`, `fiats`, `start_at`, `end_at`, `jump_id`, `lang_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/p2p.py:170` · `P2pActivityDetailResource`

### P2P-011 · 运营-WEB-删除p2p主页运营位

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/p2p.py:227` · `P2pActivityDetailResource`

### P2P-012 · 运营-WEB-下架p2p主页运营位

- 接口声明：`PATCH /<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/p2p.py:249` · `P2pActivityOfflineResource`

### P2P-013 · 运营-WEB-p2p主页运营位上移

- 接口声明：`POST /<int:id_>/sort_id`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/p2p.py:270` · `P2pActivitySortIDResource`

### P2P-014 · 运营-WEB-p2p主页运营位详情

- 接口声明：`GET /<int:id_>/langs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/p2p.py:305` · `NewInsetConfigContentResource`

### P2P-015 · p2p-广告列表-获取列表

- 接口声明：`GET `
- 输入字段：`fiat`, `adv_type`, `order_mode`, `status`, `asset`, `adv_number`, `user_id`, `start_at`, `end_at`, `page`, `limit`, `export`, `sort_by`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/advertising.py:149` · `P2pAdvertisingResource`

### P2P-016 · p2p-广告列表-获取详情

- 接口声明：`GET /<string:adv_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/advertising.py:236` · `P2pAdvertisingDetailResource`

### P2P-017 · p2p-广告列表-下架广告

- 接口声明：`PUT /<string:adv_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/advertising.py:297` · `P2pAdvertisingDetailResource`

### P2P-018 · p2p配置-p2p参数配置-获取

- 接口声明：`GET /asset`
- 输入字段：`asset`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:81` · `P2pAssetConfigResource`

### P2P-019 · p2p参数配置-p2p参数配置-新增

- 接口声明：`POST /asset`
- 输入字段：`asset`, `merchant_fee_rate`, `min_limit`, `max_limit`, `precision`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:116` · `P2pAssetConfigResource`

### P2P-020 · p2p参数配置-p2p参数配置-修改

- 接口声明：`PUT /asset`
- 输入字段：`asset`, `merchant_fee_rate`, `min_limit`, `max_limit`, `precision`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:148` · `P2pAssetConfigResource`

### P2P-021 · p2p参数配置-p2p参数配置-修改状态

- 接口声明：`PATCH /asset`
- 输入字段：`asset`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:178` · `P2pAssetConfigResource`

### P2P-022 · p2p参数配置-p2p参数配置-获取交易配置

- 接口声明：`GET /settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:215` · `P2pTradeConfigResource`

### P2P-023 · p2p参数配置-p2p参数配置-修改交易配置

- 接口声明：`POST /settings`
- 输入字段：`settings`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:225` · `P2pTradeConfigResource`

### P2P-024 · p2p参数配置-验证单白名单-列表

- 接口声明：`GET /verify-order-whitelist`
- 输入字段：`merchant_user_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:258` · `P2pVerifyOrderMerchantWhitelistResource`

### P2P-025 · p2p参数配置-验证单白名单-新增

- 接口声明：`POST /verify-order-whitelist`
- 输入字段：`merchant_user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:272` · `P2pVerifyOrderMerchantWhitelistResource`

### P2P-026 · p2p参数配置-验证单白名单-修改状态

- 接口声明：`PATCH /verify-order-whitelist/<int:merchant_user_id>`
- 输入字段：`status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:297` · `P2pVerifyOrderMerchantWhitelistDetailResource`

### P2P-027 · p2p参数配置-验证单白名单-删除

- 接口声明：`DELETE /verify-order-whitelist/<int:merchant_user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:318` · `P2pVerifyOrderMerchantWhitelistDetailResource`

### P2P-028 · p2p配置-法币配置-获取

- 接口声明：`GET /fiat`
- 输入字段：`fiat`, `status`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:340` · `P2pFiatResource`

### P2P-029 · p2p配置-法币配置-新增

- 接口声明：`POST /fiat`
- 输入字段：`fiat`, `fiat_symbol`, `precision`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:362` · `P2pFiatResource`

### P2P-030 · p2p配置-法币配置-修改状态

- 接口声明：`PATCH /fiat`
- 输入字段：`fiat`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:388` · `P2pFiatResource`

### P2P-031 · p2p配置-法币市场-获取

- 接口声明：`GET /fiat/market`
- 输入字段：`fiat`, `asset`, `status`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:438` · `P2pFiatMarketResource`

### P2P-032 · p2p配置-法币市场-新增/修改

- 接口声明：`POST /fiat/market`
- 输入字段：`fiat`, `asset`, `min_limit`, `max_limit`, `is_price_limit`, `price_type`, `manual_price`, `rule`, `visible_countries`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:480` · `P2pFiatMarketResource`

### P2P-033 · p2p配置-法币市场-修改状态

- 接口声明：`PUT /fiat/market`
- 输入字段：`fiat`, `asset`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:544` · `P2pFiatMarketResource`

### P2P-034 · p2p参数配置-(地区)支付渠道配置表-获取列表数据

- 接口声明：`GET /pay-channel`
- 输入字段：`id`, `status`, `config_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:604` · `P2pPayChannelResource`

### P2P-035 · p2p参数配置-(地区)支付渠道配置表-新增数据

- 接口声明：`POST /pay-channel`
- 输入字段：`name`, `config_type`, `is_need_name`, `form`, `lang_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:663` · `P2pPayChannelResource`

### P2P-036 · p2p参数配置-(地区)支付渠道配置表-获取详情数据

- 接口声明：`GET /pay-channel/<string:pay_channel_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:731` · `PayChannelConfigDetailResource`

### P2P-037 · p2p参数配置-(地区)支付渠道配置表-修改数据

- 接口声明：`PUT /pay-channel/<string:pay_channel_id>`
- 输入字段：`name`, `is_need_name`, `form`, `lang_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:750` · `PayChannelConfigDetailResource`

### P2P-038 · p2p参数配置-(地区)支付渠道配置表-修改状态

- 接口声明：`PUT /pay-channel/<string:pay_channel_id>/status`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:825` · `PayChannelConfigStatusResource`

### P2P-039 · p2p参数配置-(地区)支付渠道配置表-修改锁定状态

- 接口声明：`PUT /pay-channel/<string:pay_channel_id>/lock`
- 输入字段：`lock`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:866` · `PayChannelConfigLockResource`

### P2P-040 · p2p参数配置-(地区)支付渠道配置表-转换类型

- 接口声明：`PUT /pay-channel/<string:pay_channel_id>/type`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:894` · `PayChannelConfigTypeResource`

### P2P-041 · p2p参数配置-(地区)支付渠道配置表-支付渠道反馈

- 接口声明：`GET /pay-channel/feed-back`
- 输入字段：`user_id`, `name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:939` · `P2pPayChannelFeedBackResource`

### P2P-042 · p2p参数配置-法币/支付渠道配置表-数据获取

- 接口声明：`GET /pay-chanel/fiat`
- 输入字段：`fiat`, `channel_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:991` · `P2pFiatChannelResource`

### P2P-043 · p2p参数配置-法币/支付渠道配置表-新增

- 接口声明：`POST /pay-chanel/fiat`
- 输入字段：`fiat`, `pay_channel_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1043` · `P2pFiatChannelResource`

### P2P-044 · p2p参数配置-法币/支付渠道配置表-修改

- 接口声明：`PUT /pay-chanel/fiat`
- 输入字段：`id`, `fiat`, `pay_channel_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1071` · `P2pFiatChannelResource`

### P2P-045 · p2p参数配置-法币/支付渠道配置表-删除

- 接口声明：`DELETE /pay-chanel/fiat`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1109` · `P2pFiatChannelResource`

### P2P-046 · p2p参数配置-地区推荐支付渠道配置-数据获取

- 接口声明：`GET /pay-chanel/country`
- 输入字段：`country_code`, `pay_channel_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1141` · `P2pCountryPayChannelResource`

### P2P-047 · p2p参数配置-地区推荐支付渠道配置-新增数据

- 接口声明：`POST /pay-chanel/country`
- 输入字段：`country_code`, `fiat`, `pay_channel_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1196` · `P2pCountryPayChannelResource`

### P2P-048 · P2p参数配置-地区推荐支付渠道配置-修改数据

- 接口声明：`PUT /pay-chanel/country`
- 输入字段：`id`, `fiat`, `pay_channel_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1260` · `P2pCountryPayChannelResource`

### P2P-049 · P2p参数配置-地区推荐支付渠道配置-修改状态

- 接口声明：`PATCH /pay-chanel/country`
- 输入字段：`id`, `fiat`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1319` · `P2pCountryPayChannelResource`

### P2P-050 · P2p参数配置-地区法币对照-数据获取

- 接口声明：`GET /country-fiat`
- 输入字段：`country_code`, `fiat`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1366` · `P2pCountryResource`

### P2P-051 · P2p参数配置-地区法币对照-修改数据

- 接口声明：`PUT /country-fiat`
- 输入字段：`id`, `fiat`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1403` · `P2pCountryResource`

### P2P-052 · P2p参数配置-地区法币对照-删除数据

- 接口声明：`DELETE /country-fiat`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1428` · `P2pCountryResource`

### P2P-053 · P2p参数配置-公允价格-查看

- 接口声明：`GET /fair-price`
- 输入字段：`fiat`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1455` · `P2pFairPriceResource`

### P2P-054 · P2p参数配置-T+N风控策略配置-列表

- 接口声明：`GET /t-plus-n/rule`
- 输入字段：`name`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1546` · `P2pTPlusNRuleResource`

### P2P-055 · P2p参数配置-T+N风控策略配置-新增配置

- 接口声明：`POST /t-plus-n/rule`
- 输入字段：`name`, `status`, `limit_days`, `group_condition`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1572` · `P2pTPlusNRuleResource`

### P2P-056 · P2p参数配置-T+N风控策略配置-配置详情

- 接口声明：`GET /t-plus-n/rule/<int:rule_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1664` · `P2pTPlusNRuleDetailResource`

### P2P-057 · P2p参数配置-T+N风控策略配置-配置修改

- 接口声明：`PUT /t-plus-n/rule/<int:rule_id>`
- 输入字段：`name`, `status`, `limit_days`, `group_condition`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1679` · `P2pTPlusNRuleDetailResource`

### P2P-058 · P2p参数配置-T+N风控策略配置-修改状态

- 接口声明：`PATCH /t-plus-n/rule/<int:rule_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1709` · `P2pTPlusNRuleDetailResource`

### P2P-059 · P2p参数配置-T+N风控策略配置-删除配置

- 接口声明：`DELETE /t-plus-n/rule/<int:rule_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1730` · `P2pTPlusNRuleDetailResource`

### P2P-060 · P2p参数配置-T+N风控策略配置-获取全局T+N配置

- 接口声明：`GET /t-plus-n/rule/settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1751` · `P2pTPlusNRuleConfigSettingResource`

### P2P-061 · p2p参数配置-T+N风控策略配置-修改全局T+N配置

- 接口声明：`POST /t-plus-n/rule/settings`
- 输入字段：`t_plus_n_days`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1759` · `P2pTPlusNRuleConfigSettingResource`

### P2P-062 · P2p参数配置-T+N风控命中-列表

- 接口声明：`GET /t-plus-n/user-record`
- 输入字段：`user_id`, `rule_name`, `match_rule_id`, `real_rule_id`, `real_days`, `limit`, `page`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/config.py:1794` · `P2pTPlusNUserRecordResource`

### P2P-063 · p2p配置-p2p地区商家保证金配置-查看

- 接口声明：`GET /country`
- 输入字段：`country_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:46` · `P2pMarginCountryResource`

### P2P-064 · p2p配置-p2p地区商家保证金配置-修改

- 接口声明：`PUT /country`
- 输入字段：`id`, `amount`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:61` · `P2pMarginCountryResource`

### P2P-065 · p2p配置-商家保证金配置-用户

- 接口声明：`GET /user`
- 输入字段：`user_id`, `margin_type`, `email`, `kyc_country`, `has_kyc_country`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:127` · `P2pUserMarginResource`

### P2P-066 · p2p-商家保证金配置-创建个人保证金记录

- 接口声明：`POST /user`
- 输入字段：`user_id`, `require_margin`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:183` · `P2pUserMarginResource`

### P2P-067 · p2p-商家保证金配置-应缴保证金修改

- 接口声明：`PATCH /user`
- 输入字段：`user_id`, `margin_type`, `require_margin`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:205` · `P2pUserMarginResource`

### P2P-068 · p2p-商家保证金配置-下载批量上传模板

- 接口声明：`GET /user/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:269` · `P2pUserMarginTemplateResource`

### P2P-069 · p2p-商家保证金配置-批量上传

- 接口声明：`POST /user/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:288` · `P2pUserMarginImportResource`

### P2P-070 · p2p交易-商家保证金收支表-查看

- 接口声明：`GET /sys_history`
- 输入字段：`type`, `user_id`, `start_at`, `end_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:545` · `P2pMarginHistoryResource`

### P2P-071 · p2p交易-商家保证金收支表-备注

- 接口声明：`PATCH /sys_history`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:606` · `P2pMarginHistoryResource`

### P2P-072 · p2p-商家保证金收支表-查看

- 接口声明：`GET /user_history`
- 输入字段：`id`, `biz_type`, `user_id`, `start_at`, `end_at`, `status`, `page`, `limit`, `is_mer`, `is_export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:648` · `P2pUserMarginHistoryResource`

### P2P-073 · p2p-商家保证金收支表-创建

- 接口声明：`POST /user_history`
- 输入字段：`user_id`, `biz_type`, `amount`, `biz_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:757` · `P2pUserMarginHistoryResource`

### P2P-074 · p2p-商家保证金收支表-编辑备注

- 接口声明：`PATCH /user_history`
- 输入字段：`id`, `biz_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:787` · `P2pUserMarginHistoryResource`

### P2P-075 · p2p-商家保证金收支表-审核

- 接口声明：`PATCH /user_history/audit/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/p2p/margin.py:817` · `P2pUserMarginAuditHistoryResource`

### P2P-076 · p2p-商家保证金收支表-取消

- 接口声明：`PATCH /user_history/cancel/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/margin.py:858` · `P2pUserMarginCancelHistoryResource`

### P2P-077 · p2p商家活动-活动管理-列表

- 接口声明：`GET /list`
- 输入字段：`act_id`, `name`, `fiat`, `asset`, `status`, `start_at`, `end_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:76` · `P2pMerActList`

### P2P-078 · p2p商家活动-活动管理-创建活动

- 接口声明：`POST /list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:126` · `P2pMerActList`

### P2P-079 · p2p商家活动-活动管理-活动详情

- 接口声明：`GET /<int:act_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:198` · `P2pMerActDetail`

### P2P-080 · p2p商家活动-活动管理-活动编辑

- 接口声明：`PUT /<int:act_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:211` · `P2pMerActDetail`

### P2P-081 · p2p商家活动-活动管理-状态编辑

- 接口声明：`PATCH /<int:act_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:253` · `P2pMerActDetail`

### P2P-082 · p2p商家活动-活动管理-积分排行榜

- 接口声明：`GET /point/rank`
- 输入字段：`report_date`, `act_id`, `side`, `user_id`, `email`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:376` · `P2pMerActPointRankResource`

### P2P-083 · p2p商家活动-积分奖励记录-列表

- 接口声明：`GET /user/reward/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:438` · `P2pMerActRewardList`

### P2P-084 · p2p商家活动-积分明细-列表

- 接口声明：`GET /user/point/list`
- 输入字段：`fiat`, `side`, `report_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:501` · `P2pMerActPointList`

### P2P-085 · p2p商家活动-奖励明细-列表

- 接口声明：`GET /user/reward/detail`
- 输入字段：`reward_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:557` · `P2pMerActRewardDetail`

### P2P-086 · p2p商家活动-奖励记录-状态编辑

- 接口声明：`PATCH /user/reward/detail`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:605` · `P2pMerActRewardDetail`

### P2P-087 · p2p商家活动-报名用户-列表

- 接口声明：`GET /user/list`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:651` · `P2pMerActUserList`

### P2P-088 · p2p商家活动-报名用户-下一个审核

- 接口声明：`GET /user/next`
- 输入字段：`id`, `act_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:679` · `P2pMerActUserNextList`

### P2P-089 · p2p商家活动-报名用户-审核详情

- 接口声明：`GET /user/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:715` · `P2pMerActUserDetail`

### P2P-090 · p2p商家活动-报名用户-修改状态

- 接口声明：`PATCH /user/<int:id_>`
- 输入字段：`status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:727` · `P2pMerActUserDetail`

### P2P-091 · p2p商家活动-查看活动配置

- 接口声明：`GET /config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:809` · `P2pMerActConfig`

### P2P-092 · p2p商家活动-查看公允价格-列表

- 接口声明：`GET /fair-price`
- 输入字段：`asset`, `fiat`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:822` · `P2pMerActFairPriceResource`

### P2P-093 · p2p商家活动-创建公允价格

- 接口声明：`POST /fair-price`
- 输入字段：`fiat`, `asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:841` · `P2pMerActFairPriceResource`

### P2P-094 · p2p商家活动-修改公允价格

- 接口声明：`PUT /fair-price`
- 输入字段：`id`, `manual_price`, `rule`, `price_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:863` · `P2pMerActFairPriceResource`

### P2P-095 · p2p商家活动-导出用户每分钟积分详情

- 接口声明：`GET /user-point-export`
- 输入字段：`act_id`, `user_id`, `start_at`, `end_at`, `side`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:934` · `UserPointExport`

### P2P-096 · p2p商家活动-导出活动奖励详情

- 接口声明：`GET /user-reward-export`
- 输入字段：`act_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/mer_act.py:977` · `UserRewardExport`

### P2P-097 · p2p-订单-获取列表

- 接口声明：`GET `
- 输入字段：`order_id`, `side`, `status`, `order_type`, `base`, `quote`, `adv_id`, `adv_number`, `email`, `user_id`, `user_id2`, `customer_id`, `merchant_id`, `start_at`, `end_at`, `pay_channel_id`, `is_need_cert_file`, `complaint_status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:104` · `P2pOrderResource`

### P2P-098 · p2p-订单-获取订单详情

- 接口声明：`GET /<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:245` · `P2pOrderDetailResource`

### P2P-099 · p2p-订单-修改订单信息

- 接口声明：`PATCH /<int:order_id>`
- 输入字段：`admin_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:383` · `P2pOrderDetailResource`

### P2P-100 · p2p-订单-获取订单消息（渐进加载：IM sync DESC 拉最新一页；limit 默认 50；before_seq 为上一页返回的 next_before_seq）

- 接口声明：`GET /<int:order_id>/im-msgs`
- 输入字段：`limit`, `before_seq`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:487` · `P2pOrderImMsgResource`

### P2P-101 · p2p-订单-翻译消息

- 接口声明：`POST /translate`
- 输入字段：`msg_id`, `source_text`, `msg_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:619` · `P2pOrderMessageTranslateResource`

### P2P-102 · p2p-订单-获取申诉列表

- 接口声明：`POST /complaint/list`
- 输入字段：`order_id`, `complaint_statuses`, `quote`, `user_id`, `complaint_reason`, `created_start_at`, `created_end_at`, `finished_at`, `is_unread`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:692` · `P2pOrderComplaintResource`

### P2P-103 · p2p-订单-获取申诉详情

- 接口声明：`GET /<int:complaint_id>/complaint`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:845` · `P2pOrderComplaintDetailResource`

### P2P-104 · p2p-订单-修改申诉

- 接口声明：`PUT /<int:complaint_id>/complaint`
- 输入字段：`status`, `winner`, `msg`, `to_user_id`, `remark`, `operate`, `cancel_reason`, `cancel_user_defined_reason`, `duration_days`, `violation_types`, `image_keys`, `video_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:887` · `P2pOrderComplaintDetailResource`

### P2P-105 · p2p-订单-申诉消息撤回

- 接口声明：`PUT /<int:complaint_id>/complaint/record/<int:record_id>/recall`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:973` · `P2pOrderComplaintRecordRecallResource`

### P2P-106 · p2p-申诉-查看申诉话术

- 接口声明：`GET /complaint/reply`
- 输入字段：`export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:1001` · `P2pOrderComplaintReplyResource`

### P2P-107 · p2p-申诉-创建单条申诉话术

- 接口声明：`POST /complaint/reply`
- 输入字段：`reply_type`, `title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:1022` · `P2pOrderComplaintReplyResource`

### P2P-108 · p2p-申诉-修改单条申诉话术

- 接口声明：`PATCH /complaint/reply/<int:reply_id>`
- 输入字段：`reply_type`, `title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:1059` · `P2pOrderComplaintReplyDetailResource`

### P2P-109 · p2p-申诉-删除单条申诉话术

- 接口声明：`DELETE /complaint/reply/<int:reply_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:1090` · `P2pOrderComplaintReplyDetailResource`

### P2P-110 · p2p-申诉-上传申诉话术

- 接口声明：`POST /complaint/reply/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:1118` · `P2pOrderComplaintReplyBatchResource`

### P2P-111 · p2p-订单-查看相同渠道文件

- 接口声明：`GET /cert-file`
- 输入字段：`user_pay_channel_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/order.py:1158` · `P2pOrderCertFileResource`

### P2P-112 · p2p-用户权限管理-列表

- 接口声明：`GET `
- 输入字段：`user_id`, `status`, `violation_types`, `permission_types`, `duration_days`, `ban_at_start`, `ban_at_end`, `unban_at_start`, `unban_at_end`, `is_export`, `page`, `limit`
- 显式控制：ns.use_kwargs(dict(user_id=fields.Integer, status=fields.String(load_default=None), violation_types=EnumField(P2pPermissionRecord.ViolationType), permission_types=EnumField(P2pPerm
- 代码依据：`app/api/admin/p2p/permission.py:49` · `P2pPermissionBanListResource`

### P2P-113 · p2p-用户权限管理-创建

- 接口声明：`POST `
- 输入字段：`user_id`, `violation_types`, `permission_types`, `duration_days`, `remark`
- 显式控制：ns.use_kwargs(dict(user_id=fields.Integer(required=True), violation_types=fields.List(EnumField(P2pPermissionRecord.ViolationType), required=True), permission_types=fields.List(Enu
- 代码依据：`app/api/admin/p2p/permission.py:157` · `P2pPermissionBanListResource`

### P2P-114 · p2p-用户权限管理-修改

- 接口声明：`PUT /<int:ban_id>`
- 输入字段：`violation_types`, `permission_types`, `duration_days`, `remark`
- 显式控制：ns.use_kwargs(dict(violation_types=fields.List(EnumField(P2pPermissionRecord.ViolationType), required=True), permission_types=fields.List(EnumField(P2pPermissionRecord.PermissionTy
- 代码依据：`app/api/admin/p2p/permission.py:215` · `P2pPermissionBanDetailResource`

### P2P-115 · p2p-用户权限管理-解封

- 接口声明：`POST /<int:ban_id>/unban`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/permission.py:272` · `P2pPermissionBanUnbanResource`

### P2P-116 · P2P-商家功能白名单-列表

- 接口声明：`GET /merchant-whitelist`
- 输入字段：`keyword`, `merchant_user_id`, `location`, `quote`, `feature_tag`, `status`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:60` · `P2pMerchantFunctionWhitelistResource`

### P2P-117 · P2P-商家功能白名单-新增

- 接口声明：`POST /merchant-whitelist`
- 输入字段：`merchant_user_id`, `feature_tags`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:80` · `P2pMerchantFunctionWhitelistResource`

### P2P-118 · P2P-商家功能白名单-导入模板

- 接口声明：`GET /merchant-whitelist/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:111` · `P2pMerchantFunctionWhitelistTemplateResource`

### P2P-119 · P2P-商家功能白名单-批量导入

- 接口声明：`POST /merchant-whitelist/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:121` · `P2pMerchantFunctionWhitelistBatchUploadResource`

### P2P-120 · P2P-商家功能白名单-编辑

- 接口声明：`PUT /merchant-whitelist/<int:merchant_user_id>`
- 输入字段：`feature_tags`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:134` · `P2pMerchantFunctionWhitelistDetailResource`

### P2P-121 · P2P-商家功能白名单-删除

- 接口声明：`DELETE /merchant-whitelist/<int:merchant_user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:160` · `P2pMerchantFunctionWhitelistDetailResource`

### P2P-122 · P2P-商家功能白名单-修改状态

- 接口声明：`PATCH /merchant-whitelist/<int:merchant_user_id>/status`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:181` · `P2pMerchantFunctionWhitelistStatusResource`

### P2P-123 · 用户详情-法币数据-p2p基础信息

- 接口声明：`GET /<int:id_>/fiat-data`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:381` · `UserFiatDataResource`

### P2P-124 · 用户详情-法币数据-p2p关系详情

- 接口声明：`GET /<int:id_>/fiat-relations`
- 输入字段：`relation`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:434` · `UserFiatRelationResource`

### P2P-125 · 用户-P2P-商家列表

- 接口声明：`GET /merchant`
- 输入字段：`user_id`, `name`, `location`, `quote`, `shop_status`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:576` · `P2pMerchantResource`

### P2P-126 · 用户-P2P-修改商家备注

- 接口声明：`PUT /merchant`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:669` · `P2pMerchantResource`

### P2P-127 · 用户-p2p-修改商家状态

- 接口声明：`PATCH /merchant`
- 输入字段：`user_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:688` · `P2pMerchantResource`

### P2P-128 · 用户-P2P-查看商家详情

- 接口声明：`GET /merchant/<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/p2p/user.py:837` · `P2pMerchantDetailResource`

### P2P-129 · 现货-收付款-一口价兑换档位配置

- 接口声明：`GET /stage-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/payment.py:58` · `PaymentQuoteStageConfigResource`

### P2P-130 · 现货-收付款-一口价兑换档位配置修改

- 接口声明：`PUT /stage-config`
- 输入字段：`configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/payment.py:75` · `PaymentQuoteStageConfigResource`

### P2P-131 · 现货-收付款-市场兑换档位

- 接口声明：`GET /quote-market-depths`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/payment.py:128` · `PaymentQuoteMarketStageResource`

### P2P-132 · 现货-收付款-收付款列表

- 接口声明：`GET /transaction-list`
- 输入字段：`row_id`, `payer_id`, `receiver_id`, `pay_asset`, `receive_asset`, `is_diff_asset`, `status`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/payment.py:168` · `PaymentTracListResource`

### P2P-133 · 现货-收付款-相关记录

- 接口声明：`GET /relation-history`
- 输入字段：`history_type`, `start`, `end`, `row_id`, `user_id`, `sys_user_id`, `transaction_id`, `hedging_his_id`, `exchange_id`, `biz_id`, `asset`, `pay_tran_status`, `hedging_his_status`, `hedging_tran_his_status`, `fixed_exchange_his_status`, `change_his_status`, `order_id`, `market`, `side`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/payment.py:267` · `PaymentRelationHisResource`

### P2P-134 · 报表-法币报表-快捷买币报表

- 接口声明：`GET /direct-fiat-report`
- 输入字段：`is_third_party`, `third_party`, `report_type`, `type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/direct_fiat.py:68` · `DirectFiatReportResource`

### P2P-135 · 报表-法币报表-全站法币报表

- 接口声明：`GET /site-fiat-order-report`
- 输入字段：`is_third_party`, `third_party`, `report_type`, `type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/fiat.py:48` · `SiteFiatOrderReportResource`

### P2P-136 · 报表-法币报表-法币服务商报表详情

- 接口声明：`GET /site-fiat-order-detail-report`
- 输入字段：`report_type`, `is_third_party`, `type`, `report_date`, `sort_by`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/fiat.py:163` · `SiteFiatOrderDetailReportResource`

### P2P-137 · 报表-法币报表-币种法币报表

- 接口声明：`GET /asset-fiat-order-report`
- 输入字段：`report_type`, `start_date`, `asset`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/fiat.py:236` · `AssetFiatOrderReportResource`

### P2P-138 · 报表-法币报表-币种法币详情报表

- 接口声明：`GET /asset-fiat-order-report-detail`
- 输入字段：`report_type`, `report_date`, `sort_by`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/fiat.py:324` · `AssetFiatOrderReportDetail`

### P2P-139 · 报表-p2p交易报表-获取列表

- 接口声明：`GET `
- 输入字段：`report_type`, `key_type`, `key`, `page`, `limit`, `start_date`, `end_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/p2p.py:97` · `P2pReportResource`

### P2P-140 · 报表-p2p交易报表-报表详情

- 接口声明：`GET /detail`
- 输入字段：`report_type`, `key_type`, `report_date`, `sort_by`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/p2p.py:139` · `P2pReportDetailResource`

### P2P-141 · 报表-p2p交易报表-商家报表

- 接口声明：`GET /merchant`
- 输入字段：`report_type`, `page`, `limit`, `start_date`, `end_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/p2p.py:189` · `P2pMerchantReportResource`

### P2P-142 · 报表-充提报表-收付款全站报表

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/payment.py:38` · `PaymentSiteReportResource`

### P2P-143 · 报表-充提报表-收付款币种报表

- 接口声明：`GET /pay-asset-report`
- 输入字段：`report_type`, `asset`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/payment.py:139` · `PaymentPayAssetReportResource`

### P2P-144 · 目前是用于获取 swapix 所需的校验信息

- 接口声明：`GET /<partner>/validation`
- 输入字段：`type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:44` · `DirectFiatValidationResource`

### P2P-145 · 目前是用于 swapix 出金 pix key 比对

- 接口声明：`POST /<partner>/offramp/validation`
- 输入字段：`business_data`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:80` · `DirectFiatBusinessValidationResource`

### P2P-146 · DirectFiatPartners.get（用途待确认）

- 接口声明：`GET /partners`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/direct_fiat.py:109` · `DirectFiatPartners`

### P2P-147 · DirectFiatQuoteResource.post（用途待确认）

- 接口声明：`POST /<partner>/quotes`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:161` · `DirectFiatQuoteResource`

### P2P-148 · DirectFiatBuyOrdersResource.post（用途待确认）

- 接口声明：`POST /<partner>/buy-orders`
- 输入字段：`quote_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:312` · `DirectFiatBuyOrdersResource`

### P2P-149 · DirectFiatSellOrdersResource.post（用途待确认）

- 接口声明：`POST /<partner>/sell-orders`
- 输入字段：`quote_id`, `business_data`, `withdraw_password`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:356` · `DirectFiatSellOrdersResource`

### P2P-150 · DirectFiatWidgetEventResource.get（用途待确认）

- 接口声明：`GET /<partner>/widget-event`
- 输入字段：`order_id`, `type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:457` · `DirectFiatWidgetEventResource`

### P2P-151 · DirectFiatWidgetEventResource.post（用途待确认）

- 接口声明：`POST /<partner>/widget-event`
- 输入字段：`order_id`, `business_data`, `type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:473` · `DirectFiatWidgetEventResource`

### P2P-152 · DirectFiatSellOrdersWithdrawalResource.post（用途待确认）

- 接口声明：`POST /<partner>/sell-orders/withdrawal`
- 输入字段：`order_id`, `withdraw_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/direct_fiat.py:507` · `DirectFiatSellOrdersWithdrawalResource`

### P2P-153 · DirectFiatOrderListResource.get（用途待确认）

- 接口声明：`GET /order-list`
- 输入字段：`order_type`, `status`, `statuses`, `asset`, `fiat`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:587` · `DirectFiatOrderListResource`

### P2P-154 · DirectFiatOrderDetailResource.get（用途待确认）

- 接口声明：`GET /orders/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:682` · `DirectFiatOrderDetailResource`

### P2P-155 · 手动取消订单

- 接口声明：`PATCH /orders/<int:order_id>`
- 输入字段：`is_timeout`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/direct_fiat.py:709` · `DirectFiatOrderDetailResource`

### P2P-156 · FiatPartners.get（用途待确认）

- 接口声明：`GET /partners`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/fiat.py:29` · `FiatPartners`

### P2P-157 · FiatPricesResource.get（用途待确认）

- 接口声明：`GET /prices`
- 输入字段：`asset`, `fiat`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/fiat.py:72` · `FiatPricesResource`

### P2P-158 · 仅兼容 app，不再他用

- 接口声明：`GET /amounts`
- 输入字段：`asset`, `fiat`, `fiat_amount`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/fiat.py:123` · `FiatAmountsResource`

### P2P-159 · FiatQuoteResource.post（用途待确认）

- 接口声明：`POST /<partner>/quotes`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fiat.py:165` · `FiatQuoteResource`

### P2P-160 · FiatOrdersResource.post（用途待确认）

- 接口声明：`POST /<partner>/orders`
- 输入字段：`quote_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fiat.py:216` · `FiatOrdersResource`

### P2P-161 · FiatOrderListResource.get（用途待确认）

- 接口声明：`GET /order-list`
- 输入字段：`order_type`, `status`, `asset`, `fiat`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/fiat.py:274` · `FiatOrderListResource`

### P2P-162 · 首页广告列表（按筛选与排序查询）  Note:     与预览接口 GET /res/p2p/order/verify/adv-items 的 verify_items[] 条目结构一致（列表接口无 need_scan）。     若全局人脸识别开关关闭，FACE_VERIFY 项会从列表中整块省略。     verify_items 各元素：id (int

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/advertising.py:74` · `AdvertisingResource`

### P2P-163 · 校验广告草稿参数（不写库）  当 content 缺省或为空对象时，仅执行库存与单笔限额相关精简校验（check_stock_limit_params），成功时响应体 data 为空； 传入完整 content 时走 domain 全量校验，成功时 data 为空。

- 接口声明：`POST /merchant/check`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_trading=True, is_valid_mer=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:239` · `MerchantAdvertisingCheckResource`

### P2P-164 · 按交易方向分组的本人广告列表  Returns:     buy (array): P2pBusinessType.BUY（value 为 "buy"）对应的商家侧广告列表         id (string): 广告 Mongo ObjectId（32 位十六进制字符串）         adv_number (string): 业务广告编号（日+随机串

- 接口声明：`GET /merchant`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:270` · `MerchantAdvertisingResource`

### P2P-165 · 新建 P2P 广告  Returns:     mongo_id (string): 新建广告 Mongo ObjectId（标准响应 envelope 中的 data 实际为字符串直出，         YApi schema 中为便于描述列在 data 的子属性上）

- 接口声明：`POST /merchant`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_trading=True, is_valid_mer=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:300` · `MerchantAdvertisingResource`

### P2P-166 · 商家验证单默认验证项-列表  Returns:     items (list): 验证项列表；每项字段与同资源 POST/PUT/PATCH 返回的单条结构一致：         id (int): 验证项 ID         merchant_id (int): 商家用户 ID         key (str): 系统项为预设 VerifyOrder

- 接口声明：`GET /merchant/verify-order-items`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:319` · `MerchantVerifyOrderItemResource`

### P2P-167 · 商家验证单-新增（仅自定义项，无需传 key / type）  后端写入默认：key 为空串，type 为 CUSTOM（VerifyOrderItemType 枚举成员名，非请求体传入）。  Returns:     id (int): 验证项 ID     merchant_id (int): 商家用户 ID     key (str): 系统项为预设 

- 接口声明：`POST /merchant/verify-order-items`
- 输入字段：`name`, `desc`
- 显式控制：require_p2p_permission(is_merchant=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:339` · `MerchantVerifyOrderItemResource`

### P2P-168 · 商家验证单验证项-修改（仅自定义项可改名称与说明）  Returns:     id (int): 验证项 ID     merchant_id (int): 商家用户 ID     key (str): 系统项为预设 VerifyOrderItemKey 枚举成员名 FACE_VERIFY / FUND_FLOW_VERIFY / REAL_NAME_VE

- 接口声明：`PUT /merchant/verify-order-items/<int:item_id>`
- 输入字段：`name`, `desc`
- 显式控制：require_p2p_permission(is_merchant=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:376` · `MerchantVerifyOrderItemDetailResource`

### P2P-169 · 商家验证单验证项-删除（仅未被在线广告使用）

- 接口声明：`DELETE /merchant/verify-order-items/<int:item_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_merchant=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:407` · `MerchantVerifyOrderItemDetailResource`

### P2P-170 · 编辑 P2P 广告  Returns:     data (string): 广告 Mongo ObjectId 字符串，与新建 POST 一致为标准 envelope 下的字符串 data

- 接口声明：`PUT /<string:advertising_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_valid_mer=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:418` · `AdvertisingDetailResource`

### P2P-171 · 查看指定广告详情（须登录；仅广告所属商户 user_id 与当前用户一致时通过 info 校验）  Returns:     id (string): 广告 Mongo ObjectId     adv_type (string): 商家挂单方向枚举成员名 SELL / BUY     base (string): 数字货币     quote (strin

- 接口声明：`GET /<string:advertising_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/p2p/advertising.py:433` · `AdvertisingDetailResource`

### P2P-172 · 变更广告上架状态（上线 / 下线 / 删除）；成功时响应体 data 通常为空

- 接口声明：`PUT /<string:advertising_id>/status`
- 输入字段：`status`
- 显式控制：require_p2p_permission(is_valid_mer=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:465` · `AdvertisingStatusResource`

### P2P-173 · 商家侧广告盘口深度（按价聚合）  Query: asset 默认 USDT；fiat 缺省时按用户国家解析法币，若无则 USD。  Returns:     asset (string): 数字资产     fiat (string): 法币     rate (string): asset 对 fiat 的参考汇率（decimal 字符串形式由业务层格式化

- 接口声明：`GET /book`
- 输入字段：`asset`, `fiat`
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/advertising.py:495` · `AdvertisingBookResource`

### P2P-174 · 下单前广告详情（需已登录且开通 P2P；并校验 KYC / 2FA）  Returns:     id (string): 广告 Mongo ObjectId（32 位十六进制字符串）     adv_type (string): 「用户视角」方向的 P2pBusinessType 枚举成员名 SELL / BUY     base (string): 数字

- 接口声明：`GET /<string:advertising_id>/order`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/advertising.py:526` · `AdvertisingOrderResource`

### P2P-175 · P2pConfigResource.get（用途待确认）

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/config.py:45` · `P2pConfigResource`

### P2P-176 · P2pFiatMarketResource.get（用途待确认）

- 接口声明：`GET /fiat-market`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/config.py:111` · `P2pFiatMarketResource`

### P2P-177 · P2pUserAssetResource.get（用途待确认）

- 接口声明：`GET /user/asset`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/config.py:130` · `P2pUserAssetResource`

### P2P-178 · P2pUserAssetResource.patch（用途待确认）

- 接口声明：`PATCH /user/asset`
- 输入字段：`asset`, `fiat`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/config.py:156` · `P2pUserAssetResource`

### P2P-179 · P2pConfigAdvertisingResource.get（用途待确认）

- 接口声明：`GET /advertising-limit`
- 输入字段：`fiat`, `asset`, `limit_unit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/config.py:174` · `P2pConfigAdvertisingResource`

### P2P-180 · ImMessageResource.get（用途待确认）

- 接口声明：`GET /im-message`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/config.py:228` · `ImMessageResource`

### P2P-181 · P2pQuestionResource.get（用途待确认）

- 接口声明：`GET /question`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/p2p/config.py:240` · `P2pQuestionResource`

### P2P-182 · P2pAdvFiatResource.get（用途待确认）

- 接口声明：`GET /adv/fiats`
- 输入字段：`asset`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/p2p/config.py:253` · `P2pAdvFiatResource`

### P2P-183 · P2pMerActListResource.get（用途待确认）

- 接口声明：`GET /list`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/mer_act.py:39` · `P2pMerActListResource`

### P2P-184 · P2pMerActUserResource.get（用途待确认）

- 接口声明：`GET /user`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/p2p/mer_act.py:98` · `P2pMerActUserResource`

### P2P-185 · P2pMerActResource.get（用途待确认）

- 接口声明：`GET /<int:act_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/mer_act.py:147` · `P2pMerActResource`

### P2P-186 · P2pMerActUserDetailResource.get（用途待确认）

- 接口声明：`GET /user/<int:act_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/p2p/mer_act.py:162` · `P2pMerActUserDetailResource`

### P2P-187 · P2pMerActPointListResource.get（用途待确认）

- 接口声明：`GET /point/list/<int:act_id>`
- 输入字段：`date`, `side`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/mer_act.py:240` · `P2pMerActPointListResource`

### P2P-188 · P2pMerActUserPointResource.get（用途待确认）

- 接口声明：`GET /user/point/<int:act_id>`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/p2p/mer_act.py:321` · `P2pMerActUserPointResource`

### P2P-189 · P2pMerActUserRewardResource.get（用途待确认）

- 接口声明：`GET /user/reward/<int:act_id>`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/p2p/mer_act.py:359` · `P2pMerActUserRewardResource`

### P2P-190 · P2pMerActUserApplyResource.post（用途待确认）

- 接口声明：`POST /user/apply/<int:act_id>`
- 输入字段：`intro`, `other_link`, `image_keys`, `pdf_keys`
- 显式控制：require_p2p_permission(is_valid_mer=True)
- 代码依据：`app/api/frontend/p2p/mer_act.py:392` · `P2pMerActUserApplyResource`

### P2P-191 · 获取 P2P 订单列表；支持多条件筛选、仅看会话未读、以及导出 Excel。  export 为 true 时：响应体为 Excel 文件流，列为订单编号、创建时间、方向、币种、价格、总额、数量、 对手实名、支付方式、状态等（与 export_headers 一致）。   Returns:     orders (array): 当前页订单列表；元素为基础订

- 接口声明：`POST /list`
- 输入字段：`opponent_user_id`, `user_type`, `statuses`, `order_type`, `side`, `fiat`, `assets`, `order_id`, `start_time`, `end_time`, `has_unread`, `page`, `limit`, `export`
- 显式控制：require_p2p_permission()
- 代码依据：`app/api/frontend/p2p/order.py:161` · `P2pOrderListResource`

### P2P-192 · 获取订单详情。  Returns:     order_id (string): 订单编号。     created_at / finished_at (datetime): 订单创建/完成时间；未完成时 finished_at 为空。     base / quote (string): 数字货币与法币币种。     price (string): 下单单

- 接口声明：`GET /<string:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/order.py:302` · `P2pOrderDetailResource`

### P2P-193 · 创建订单

- 接口声明：`POST `
- 输入字段：`adv_id`, `price`, `base`, `quote`, `base_amount`, `quote_amount`, `amount_type`, `user_pay_channel_id`, `verify_items`
- 显式控制：require_p2p_permission(is_trading=True, is_kyc=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/order.py:343` · `P2pOrderResource`

### P2P-194 · 下单前预览：若非验证单广告或线下广告不符合条件则按需抛错或返回空列表。  Returns:     verify_items (array): 每条对应广告 verify_items 里的一项配置，         在 P2pVerifyOrderItems.to_dict(enum_to_name=True) 基础上含广告单快照中的 params，    

- 接口声明：`GET /verify/adv-items`
- 输入字段：`adv_id`, `base_amount`
- 显式控制：require_p2p_permission(is_trading=True, is_kyc=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/order.py:421` · `P2pOrderVerifyAdvItemsPreviewResource`

### P2P-195 · 先创建 P2P 专属活体流水和 token，后续复用通用 /kyc/liveness token 流程。  Returns:     history_id (int): LivenessCheckHistory 主键，用于排查本次邮件验证流水。     token (str): to_email 为 false 时返回，用于拉起通用 /kyc/livenes

- 接口声明：`POST /verify/liveness/token`
- 输入字段：`base`, `base_amount`, `to_email`, `toEmail`
- 显式控制：require_p2p_permission(is_trading=True, is_kyc=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/order.py:465` · `P2pVerifyLivenessEmailTokenResource`

### P2P-196 · 创建一条进行中的人脸核验记录并联调第三方；同一时间仅允许一单在途。  限频：10 分钟内 5 次、1 小时内 10 次、24 小时内 20 次（按用户计）。  Returns:     history_id (int): LivenessCheckHistory 主键；SDK 闭环后对同路径资源 GET/PATCH，以该 id 轮询状态并提交机审。     

- 接口声明：`POST /verify/liveness`
- 输入字段：`base`, `base_amount`
- 显式控制：require_p2p_permission(is_trading=True, is_kyc=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/order.py:513` · `P2pVerifyLivenessResource`

### P2P-197 · 路径参数 history_id：须与 POST /verify/liveness 返回的 history_id 相同，用于标识本轮 P2P 验证单关联的活体流水。  客户端轮询：必要时回源刷新 Sumsub action 状态并落库。  Returns:     status (str): 活体流水状态枚举名（如 CREATED、PASSED、REJECTE

- 接口声明：`GET /verify/liveness/<int:history_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_kyc=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/order.py:551` · `P2pVerifyLivenessSubmitResource`

### P2P-198 · 路径参数 history_id：须与 POST /verify/liveness 返回的 history_id 相同；SDK 活体闭环后调用本接口提交机审。  APP /SDK 活体完成后调用：将流水置为待审并触发 Sumsub action check。  Returns:     status (str): 同上。     reason (str): 同

- 接口声明：`PATCH /verify/liveness/<int:history_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_kyc=True); lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/order.py:566` · `P2pVerifyLivenessSubmitResource`

### P2P-199 · 仅验证单且订单仍为 CREATED（待审核）、验证状态为「已提交材料」时可改；仅买家本人。  Returns:     无 data 字段或空对象（以统一响应封装为准）。

- 接口声明：`PUT /<string:order_id>/verify/items`
- 输入字段：`items`
- 显式控制：require_p2p_permission; lock_request(with_user=True)
- 代码依据：`app/api/frontend/p2p/order.py:587` · `P2pOrderVerifyMaterialsUpdateResource`

### P2P-200 · 确认订单；验证单在材料已提交待审时，确认即审核通过并接单

- 接口声明：`PUT /<string:order_id>/confirm`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_merchant=True, is_trading=True)
- 代码依据：`app/api/frontend/p2p/order.py:615` · `P2pOrderConfirmResource`

### P2P-201 · 订单付款 

- 接口声明：`PUT /<string:order_id>/pay`
- 输入字段：`file_keys`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/p2p/order.py:631` · `P2pOrderPayResource`

### P2P-202 · 完成订单(放币) 

- 接口声明：`PUT /<string:order_id>/finish`
- 输入字段：`withdraw_password`
- 显式控制：require_p2p_permission(is_trading=True)
- 代码依据：`app/api/frontend/p2p/order.py:647` · `P2pOrderFinishResource`

### P2P-203 · 取消订单。

- 接口声明：`PUT /<string:order_id>/cancel`
- 输入字段：`reason`, `user_defined_reason`
- 显式控制：require_p2p_permission()
- 代码依据：`app/api/frontend/p2p/order.py:667` · `P2pOrderCancelResource`

### P2P-204 · 获取进行中的订单数量 申诉数量

- 接口声明：`GET /active_count`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/order.py:733` · `P2pOrderActiveOrderCountResource`

### P2P-205 · 获取订单状态（前端轮询使用） 

- 接口声明：`POST /status`
- 输入字段：`order_ids`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/order.py:766` · `P2pOrderStatusResource`

### P2P-206 · 获取当前用户参与的 P2P 订单申诉列表。  筛选项作用于关联订单（与申诉记录 join 的 p2p_order），分页按申诉记录 id 倒序。  Returns:     total (int): 满足当前筛选条件的申诉总数。     complaints (array): 当前页申诉列表；每项在关联订单的展示结构与「订单列表」单条订单一致，       

- 接口声明：`POST /complaint/list`
- 输入字段：`order_id`, `user_type`, `statuses`, `side`, `fiat`, `assets`, `order_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/order.py:834` · `P2pOrderComplaintListResource`

### P2P-207 · 创建订单申诉 

- 接口声明：`POST /<string:order_id>/complaint`
- 输入字段：`desc`, `reason`, `image_keys`, `video_keys`
- 显式控制：require_p2p_permission()
- 代码依据：`app/api/frontend/p2p/order.py:982` · `P2pOrderComplaintDetailResource`

### P2P-208 · 获取申诉详情 

- 接口声明：`GET /<string:order_id>/complaint`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/order.py:1007` · `P2pOrderComplaintDetailResource`

### P2P-209 · 增加申诉内容 

- 接口声明：`PUT /<string:order_id>/complaint`
- 输入字段：`desc`, `image_keys`, `video_keys`
- 显式控制：require_p2p_permission()
- 代码依据：`app/api/frontend/p2p/order.py:1030` · `P2pOrderComplaintDetailResource`

### P2P-210 · 取消申诉 

- 接口声明：`PUT /<string:order_id>/complaint/cancel`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission()
- 代码依据：`app/api/frontend/p2p/order.py:1073` · `P2pOrderComplaintResource`

### P2P-211 · P2pRelationResource.get（用途待确认）

- 接口声明：`GET /<string:biz_user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/relation.py:24` · `P2pRelationResource`

### P2P-212 · P2pRelationBlockListResource.get（用途待确认）

- 接口声明：`GET /block`
- 输入字段：`page`, `limit`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/relation.py:34` · `P2pRelationBlockListResource`

### P2P-213 · P2pRelationFollowListResource.get（用途待确认）

- 接口声明：`GET /follow`
- 输入字段：`page`, `limit`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/relation.py:48` · `P2pRelationFollowListResource`

### P2P-214 · P2pRelationBlockUpdateResource.post（用途待确认）

- 接口声明：`POST /block/<string:biz_user_id>`
- 输入字段：`is_block`, `reason`, `user_defined_reason`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/relation.py:62` · `P2pRelationBlockUpdateResource`

### P2P-215 · P2pRelationFollowUpdateResource.post（用途待确认）

- 接口声明：`POST /follow/<string:biz_user_id>`
- 输入字段：`is_follow`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/relation.py:85` · `P2pRelationFollowUpdateResource`

### P2P-216 · P2pRelationBlockReasonResource.get（用途待确认）

- 接口声明：`GET /block/reason`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/relation.py:101` · `P2pRelationBlockReasonResource`

### P2P-217 · P2pUserResource.get（用途待确认）

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:33` · `P2pUserResource`

### P2P-218 · 成为p2p用户

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/p2p/user.py:41` · `P2pUserResource`

### P2P-219 · 修改p2p用户昵称

- 接口声明：`PUT `
- 输入字段：`nickname`, `account_name`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:51` · `P2pUserResource`

### P2P-220 · P2pUserPayChanelResource.get（用途待确认）

- 接口声明：`GET /pay-channel`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:74` · `P2pUserPayChanelResource`

### P2P-221 · P2pUserPayChanelResource.post（用途待确认）

- 接口声明：`POST /pay-channel`
- 输入字段：`channel_id`, `form`, `alias`, `remark`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:85` · `P2pUserPayChanelResource`

### P2P-222 · P2pUserPayChanelResource.put（用途待确认）

- 接口声明：`PUT /pay-channel`
- 输入字段：`user_channel_id`, `form`, `alias`, `remark`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:104` · `P2pUserPayChanelResource`

### P2P-223 · P2pUserPayChanelResource.delete（用途待确认）

- 接口声明：`DELETE /pay-channel`
- 输入字段：`user_channel_id`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:124` · `P2pUserPayChanelResource`

### P2P-224 · P2pUserFeedbackChannelResource.post（用途待确认）

- 接口声明：`POST /feedback-channel`
- 输入字段：`channel_name`, `fiat_name`, `remark`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:140` · `P2pUserFeedbackChannelResource`

### P2P-225 · P2pOtherUserInfoResource.get（用途待确认）

- 接口声明：`GET /<string:biz_user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission_except_mobile
- 代码依据：`app/api/frontend/p2p/user.py:157` · `P2pOtherUserInfoResource`

### P2P-226 · P2pMerchantAdvertisingResource.get（用途待确认）

- 接口声明：`GET /<string:biz_user_id>/advertising`
- 输入字段：`page`, `limit`
- 显式控制：require_p2p_permission_except_mobile
- 代码依据：`app/api/frontend/p2p/user.py:172` · `P2pMerchantAdvertisingResource`

### P2P-227 · 获取当前商家工作台信息。  merchant_info 来自商家态的 get_self_info（P2pMerchantOption.get_self_info）， 比普通 P2P 用户 get_self_info 多返回店铺状态、商家状态、保证金状态、接单率、关注数、保证金信息、 商家功能开关等商家字段。  Returns:     merchant_in

- 接口声明：`GET /merchant`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/user.py:196` · `P2pMerchantResource`

### P2P-228 · 修改p2p商家的名称

- 接口声明：`PUT /merchant`
- 输入字段：`nickname`
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/user.py:260` · `P2pMerchantResource`

### P2P-229 · 开通商家权限

- 接口声明：`POST /merchant`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/p2p/user.py:273` · `P2pMerchantResource`

### P2P-230 · P2pMerchantSpotResource.put（用途待确认）

- 接口声明：`PUT /merchant/spot`
- 输入字段：`spot_status`
- 显式控制：require_p2p_permission(is_valid_mer=True)
- 代码依据：`app/api/frontend/p2p/user.py:284` · `P2pMerchantSpotResource`

### P2P-231 · P2pMerchantTradingDataResource.get（用途待确认）

- 接口声明：`GET /merchant/trading-data`
- 输入字段：`trading_date`
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/user.py:303` · `P2pMerchantTradingDataResource`

### P2P-232 · P2pNicknamesResource.post（用途待确认）

- 接口声明：`POST /nicknames`
- 输入字段：`im_user_ids`
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:331` · `P2pNicknamesResource`

### P2P-233 · P2pMarginPaymentResource.post（用途待确认）

- 接口声明：`POST /merchant/margin/payment`
- 输入字段：`amount`
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/user.py:365` · `P2pMarginPaymentResource`

### P2P-234 · P2pMerchantCancelResource.get（用途待确认）

- 接口声明：`GET /merchant/cancel`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/user.py:382` · `P2pMerchantCancelResource`

### P2P-235 · P2pMerchantCancelResource.post（用途待确认）

- 接口声明：`POST /merchant/cancel`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_merchant=True)
- 代码依据：`app/api/frontend/p2p/user.py:392` · `P2pMerchantCancelResource`

### P2P-236 · P2pTPlusNNotifyResource.post（用途待确认）

- 接口声明：`POST /t-plus-n/notify`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission
- 代码依据：`app/api/frontend/p2p/user.py:403` · `P2pTPlusNNotifyResource`

### P2P-237 · P2pActiveResource.post（用途待确认）

- 接口声明：`POST /active`
- 输入字段：`im_user_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/p2p/user.py:424` · `P2pActiveResource`

### P2P-238 · 开启｜关闭 收付款功能

- 接口声明：`PUT /enable-status`
- 输入字段：`opening_payment`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/payment.py:58` · `UserPaymentStatusResource`

### P2P-239 · 创建收款二维码

- 接口声明：`POST /receive/qrcode`
- 输入字段：`asset`, `amount`, `remark`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/payment.py:89` · `GenReceiveQrCodeResource`

### P2P-240 · 获取收款二维码信息

- 接口声明：`GET /receive/qrcode-info`
- 输入字段：`qrcode_key`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/payment.py:119` · `ReceiveQrCodeInfoResource`

### P2P-241 · 根据收款币种 获取可支持兑换的 付款币种列表 

- 接口声明：`GET /pay/quote/payable-assets`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/payment.py:142` · `PaymentQuotePayableAssetsResource`

### P2P-242 · （付款人）跨币种支付-询价

- 接口声明：`POST /pay/quote`
- 输入字段：`pay_asset`, `receive_asset`, `pay_amount`, `receive_amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/payment.py:165` · `PaymentQuoteResource`

### P2P-243 · （付款人）提交支付

- 接口声明：`POST /pay`
- 输入字段：`pay_asset`, `pay_amount`, `quote_id`, `receive_asset`, `receive_amount`, `receiver_id`, `withdraw_password`, `remark`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/payment.py:241` · `PaymentPayResource`

### P2P-244 · 付款历史

- 接口声明：`GET /pay-history`
- 输入字段：`asset`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/payment.py:346` · `PaymentPayHistoryResource`

### P2P-245 · 收款历史

- 接口声明：`GET /receive-history`
- 输入字段：`asset`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/payment.py:422` · `PaymentReceiveHistoryResource`

### P2P-246 · 最近收款付款历史

- 接口声明：`GET /recent-history`
- 输入字段：`limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/payment.py:490` · `PaymentRecentHistoryResource`

### P2P-247 · 获取每日付款额度

- 接口声明：`GET /pay/limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/payment.py:558` · `PaymentPayLimitResource`

### P2P-248 · 修改每日付款额度

- 接口声明：`POST /pay/limit`
- 输入字段：`daily_custom_limit_usd`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/payment.py:576` · `PaymentPayLimitResource`

### P2P-249 · 设置P2P店铺营业状态

- 接口声明：`POST /exchange-status`
- 输入字段：`status`
- 显式控制：require_p2p_permission(is_valid_mer=True, auth_method='API')
- 代码依据：`app/api/v2/p2p.py:111` · `P2pExchangeStatusResource`

### P2P-250 · 批量管理P2P广告

- 接口声明：`POST /manage-ads`
- 输入字段：`status`, `ad_ids`
- 显式控制：require_p2p_permission(is_valid_mer=True, auth_method='API')
- 代码依据：`app/api/v2/p2p.py:137` · `P2pManageAdsResource`

### P2P-251 · 获取用户广告列表（排除已删除）

- 接口声明：`GET /ads`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_p2p_permission(is_valid_mer=True, auth_method='API')
- 代码依据：`app/api/v2/p2p.py:182` · `P2pUserAdsResource`

### P2P-252 · 获取市场广告列表

- 接口声明：`GET /market/ads`
- 输入字段：`base_ccy`, `quote_ccy`, `order_side`, `target_quote_amount`, `sort_by`, `sort_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/p2p.py:201` · `P2pMarketAdsResource`

### P2P-253 · 获取P2P订单列表

- 接口声明：`GET /order`
- 输入字段：`start_time`, `end_time`, `ad_side`, `quote_ccy`, `status`, `page`, `limit`
- 显式控制：require_p2p_permission(is_trading=True, auth_method='API')
- 代码依据：`app/api/v2/p2p.py:240` · `P2pOrderResource`

### P2P-254 · 批量修改P2P广告价格

- 接口声明：`POST /modify-ads`
- 输入字段：`ads`, `ad_id`, `price`
- 显式控制：require_p2p_permission(is_valid_mer=True, auth_method='API')
- 代码依据：`app/api/v2/p2p.py:297` · `P2pModifyAdsResource`

### P2P-255 · 获取P2P市场深度数据

- 接口声明：`GET /market/depth`
- 输入字段：`base_ccy`, `quote_ccy`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/p2p.py:359` · `P2pMarketDepthResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/admin/test_fiat.py`
- `tests/api/admin/test_p2p_advertising.py`
- `tests/api/admin/test_p2p_config_country_pay_channel.py`
- `tests/api/admin/test_p2p_config_fiat.py`
- `tests/api/admin/test_p2p_config_settings.py`
- `tests/api/admin/test_p2p_margin_user_config.py`
- `tests/api/admin/test_p2p_merchant_function_whitelist.py`
- `tests/api/admin/test_p2p_merchant_resource.py`
- `tests/api/admin/test_p2p_order.py`
- `tests/api/admin/test_p2p_order_complaint.py`
- `tests/api/admin/test_user_fiat_data.py`
- `tests/api/frontend/test_direct_fiat_eur_offline.py`
- `tests/api/frontend/test_fiat.py`
- `tests/api/frontend/test_p2p_advertising_status.py`
- `tests/api/frontend/test_p2p_order_export.py`
- `tests/api/frontend/test_p2p_order_verify_liveness_items_api.py`
- `tests/api/frontend/test_p2p_user_pay_channel.py`
- `tests/api/frontend/test_p2p_verify_order.py`
- `tests/api/frontend/test_payment_withdraw_password.py`
- `tests/api/v2/test_p2p.py`
- `tests/business/p2p/test_advertising.py`
- `tests/business/p2p/test_complaint.py`
- `tests/business/p2p/test_country_fiat.py`
- `tests/business/p2p/test_fair_price.py`
- `tests/business/p2p/test_fiat.py`
- `tests/business/p2p/test_inner_order.py`
- `tests/business/p2p/test_margin.py`
- `tests/business/p2p/test_mer_act.py`
- `tests/business/p2p/test_new_user_permission.py`
- `tests/business/p2p/test_order.py`
- `tests/business/p2p/test_order_factor.py`
- `tests/business/p2p/test_order_summary.py`
- `tests/business/p2p/test_p2p_fiat_market.py`
- `tests/business/p2p/test_p2p_utils_merchant_and_search.py`
- `tests/business/p2p/test_pay_channel.py`
- `tests/business/p2p/test_permission.py`
- `tests/business/p2p/test_permission_api.py`
- `tests/business/p2p/test_report_fee_fields.py`
- `tests/business/p2p/test_server_api.py`
- `tests/business/p2p/test_state_machine.py`
- `tests/business/p2p/test_stock_biz.py`
- `tests/business/p2p/test_trans_biz.py`
- `tests/business/p2p/test_user.py`
- `tests/business/p2p/test_user_zero_margin.py`
- `tests/business/payment/test_pay.py`
- `tests/business/payment/test_quote.py`
- `tests/business/report/test_fiat.py`
- `tests/schedules/test_fiat.py`
- `tests/schedules/test_p2p_margin.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
