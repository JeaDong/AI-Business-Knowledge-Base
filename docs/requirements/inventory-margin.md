# 杠杆与借贷 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### MARGIN-001 · 钱包-授信-授信账号列表

- 接口声明：`GET /user`
- 输入字段：`user_type`, `credit_grade`, `search_keyword`, `can_withdraw`, `trading_limited`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:77` · `CreditUserResource`

### MARGIN-002 · 钱包-授信-添加授信账号

- 接口声明：`POST /user`
- 输入字段：`email`, `withdraw_rate`, `credit_grade`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/credit.py:201` · `CreditUserResource`

### MARGIN-003 · 钱包-授信-编辑授信账号

- 接口声明：`PUT /user`
- 输入字段：`id`, `email`, `user_id`, `withdraw_rate`, `credit_grade`, `trading_limited`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/credit.py:283` · `CreditUserResource`

### MARGIN-004 · 钱包-授信-删除授信账号

- 接口声明：`DELETE /user`
- 输入字段：`id`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/credit.py:341` · `CreditUserResource`

### MARGIN-005 · 钱包-授信-授信用户排名

- 接口声明：`GET /ranking`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:387` · `CreditUserRankingResource`

### MARGIN-006 · 钱包-授信-授信审核列表

- 接口声明：`GET /records`
- 输入字段：`user_type`, `credit_grade`, `search_keyword`, `asset`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:465` · `RecordResource`

### MARGIN-007 · 钱包-授信-创建授信审核

- 接口声明：`POST /records`
- 输入字段：`asset`, `email`, `amount`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:599` · `RecordResource`

### MARGIN-008 · 钱包-授信-编辑授信审核

- 接口声明：`PUT /records`
- 输入字段：`id`, `operation`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/credit.py:652` · `RecordResource`

### MARGIN-009 · 钱包-授信-授信审核确认弹窗信息

- 接口声明：`POST /records/audit-preview`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:762` · `RecordAuditPreviewResource`

### MARGIN-010 · 钱包-授信-授信审核模板

- 接口声明：`GET /batch/records`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:828` · `BatchRecordResource`

### MARGIN-011 · 钱包-授信-上传批量授信审核

- 接口声明：`POST /batch/records`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/credit.py:842` · `BatchRecordResource`

### MARGIN-012 · 钱包-授信-批量授信审核

- 接口声明：`PUT /batch/records`
- 输入字段：`ids`, `operation`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/credit.py:933` · `BatchRecordResource`

### MARGIN-013 · 钱包-授信-授信流水

- 接口声明：`GET /history`
- 输入字段：`user_type`, `credit_grade`, `search_keyword`, `credit_type`, `status`, `asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:993` · `RecordHistoryResource`

### MARGIN-014 · 钱包-授信-授信待还

- 接口声明：`GET /account`
- 输入字段：`user_id`, `search_keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1126` · `AccountResource`

### MARGIN-015 · 钱包-授信-授信还币

- 接口声明：`POST /account`
- 输入字段：`user_id`, `asset`, `amount`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/credit.py:1205` · `AccountResource`

### MARGIN-016 · 钱包-授信管理-授信币种利率-币种利率配置列表 

- 接口声明：`GET /asset-rate`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1232` · `CreditAssetRateResource`

### MARGIN-017 · 钱包-授信管理-授信币种利率-新建币种利率配置 

- 接口声明：`POST /asset-rate`
- 输入字段：`asset`, `day_rate`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1262` · `CreditAssetRateResource`

### MARGIN-018 · 钱包-授信管理-授信币种利率-编辑币种利率配置 

- 接口声明：`PUT /asset-rate`
- 输入字段：`id`, `day_rate`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1302` · `CreditAssetRateResource`

### MARGIN-019 · 钱包-授信管理-授信币种利率-删除币种利率配置 

- 接口声明：`DELETE /asset-rate`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1334` · `CreditAssetRateResource`

### MARGIN-020 · 钱包-授信管理-授信用户利率-授信用户利率列表 

- 接口声明：`GET /asset-user-rate`
- 输入字段：`asset`, `expired_start_date`, `expired_end_date`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1366` · `CreditAssetUserRateResource`

### MARGIN-021 · 钱包-授信管理-授信用户利率-新增用户授信利率 

- 接口声明：`POST /asset-user-rate`
- 输入字段：`user_id`, `rate_configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1427` · `CreditAssetUserRateResource`

### MARGIN-022 · 钱包-授信管理-授信用户利率-编辑用户授信利率 

- 接口声明：`PUT /asset-user-rate`
- 输入字段：`id`, `day_rate`, `expired_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1536` · `CreditAssetUserRateResource`

### MARGIN-023 · 钱包-授信管理-授信用户利率-删除用户授信利率 

- 接口声明：`DELETE /asset-user-rate`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/credit.py:1574` · `CreditAssetUserRateResource`

### MARGIN-024 · 杠杆-市场配置

- 接口声明：`GET `
- 输入字段：`name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:32` · `AccountListResource`

### MARGIN-025 · 杠杆-添加市场配置

- 接口声明：`POST `
- 输入字段：`details`, `status`, `name`, `leverage`, `order_period`, `increase_period`, `warning_rate`, `base_precision`, `max_liquidation_rate`, `max_precision`, `increase_precision`, `base_asset_max_loan`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:86` · `AccountListResource`

### MARGIN-026 · 杠杆-编辑市场配置

- 接口声明：`PUT /<int:account_id>`
- 输入字段：`details`, `status`, `name`, `leverage`, `order_period`, `increase_period`, `warning_rate`, `base_precision`, `max_liquidation_rate`, `max_precision`, `increase_precision`, `base_asset_max_loan`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:191` · `EditAccountResource`

### MARGIN-027 · 杠杆-开关市场配置

- 接口声明：`PATCH /<int:account_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:274` · `EditAccountResource`

### MARGIN-028 · 支持特殊杠杆市场借币配置自动填充

- 接口声明：`GET /info`
- 输入字段：`name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:312` · `MarginAccountInfoResource`

### MARGIN-029 · 用户-特殊配置-特殊市场借币额度配置->列表 

- 接口声明：`GET /user-rules`
- 输入字段：`market`, `user_id`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:332` · `UserMarginAccountRuleResource`

### MARGIN-030 · 用户-特殊配置-特殊市场借币额度配置->新增 

- 接口声明：`POST /user-rules`
- 输入字段：`user_id`, `market`, `base_asset_max_loan`, `quote_asset_max_loan`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:386` · `UserMarginAccountRuleResource`

### MARGIN-031 · 用户-特殊配置-特殊市场借币额度配置->编辑 

- 接口声明：`PUT /user-rules`
- 输入字段：`id`, `user_id`, `market`, `base_asset_max_loan`, `quote_asset_max_loan`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:460` · `UserMarginAccountRuleResource`

### MARGIN-032 · 用户-特殊配置-特殊市场借币额度配置->删除 

- 接口声明：`DELETE /user-rules`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/accounts.py:519` · `UserMarginAccountRuleResource`

### MARGIN-033 · 杠杆-借币配置

- 接口声明：`GET /rules`
- 输入字段：`asset`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:45` · `MarginAssetRuleResource`

### MARGIN-034 · 杠杆-借币配置-添加借币配置

- 接口声明：`POST /rules`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:110` · `MarginAssetRuleResource`

### MARGIN-035 · 杠杆-借币配置-编辑借币配置

- 接口声明：`PUT /rules`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:156` · `MarginAssetRuleResource`

### MARGIN-036 · 支持特殊杠杆借币配置自动填充

- 接口声明：`GET /info`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:191` · `MarginAssetInfoResource`

### MARGIN-037 · 用户-特殊配置-特殊杠杆借币额度->列表 

- 接口声明：`GET /user-rules`
- 输入字段：`asset`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:210` · `UserMarginAssetRuleResource`

### MARGIN-038 · 用户-特殊配置-特殊杠杆借币额度->新增 

- 接口声明：`POST /user-rules`
- 输入字段：`user_id`, `asset`, `max_loan`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:252` · `UserMarginAssetRuleResource`

### MARGIN-039 · 用户-特殊配置-特殊杠杆借币额度->编辑 

- 接口声明：`PUT /user-rules`
- 输入字段：`id`, `user_id`, `asset`, `max_loan`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:327` · `UserMarginAssetRuleResource`

### MARGIN-040 · 用户-特殊配置-特殊杠杆借币额度->删除 

- 接口声明：`DELETE /user-rules`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/assets.py:380` · `UserMarginAssetRuleResource`

### MARGIN-041 · 币币-杠杆-强平记录列表

- 接口声明：`GET `
- 输入字段：`market_type`, `status`, `reason`, `id`, `user_id`, `start_time`, `end_time`, `loan_type`, `sort_name`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/burst.py:94` · `BurstResource`

### MARGIN-042 · 币币-杠杆配置-合成指数配置列表

- 接口声明：`GET `
- 输入字段：`name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/composite.py:24` · `ComposeIndexResource`

### MARGIN-043 · 币币-杠杆配置-新建合成指数配置

- 接口声明：`POST `
- 输入字段：`name`, `compose_method`, `price_precision`, `first_market`, `second_market`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/composite.py:74` · `ComposeIndexResource`

### MARGIN-044 · 币币-杠杆配置-合成指数设置

- 接口声明：`PUT /<int:index_id>`
- 输入字段：`name`, `compose_method`, `price_precision`, `first_market`, `second_market`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/composite.py:156` · `ComposeIndexIdResource`

### MARGIN-045 · 币币-杠杆配置-合成指数状态设置

- 接口声明：`PATCH /<int:index_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/composite.py:204` · `ComposeIndexIdResource`

### MARGIN-046 · 用户-特殊配置-特殊杠杆日息->列表 

- 接口声明：`GET /day-rate`
- 输入字段：`keyword`, `start_expired_time`, `end_expired_time`, `page`, `limit`, `active_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/fee.py:35` · `UserMarginDayRateResource`

### MARGIN-047 · 用户-特殊配置-特殊杠杆日息->新增 

- 接口声明：`POST /day-rate`
- 输入字段：`user_id`, `day_rate`, `expired_time`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/fee.py:94` · `UserMarginDayRateResource`

### MARGIN-048 · 用户-特殊配置-特殊杠杆日息->编辑 

- 接口声明：`PUT /day-rate`
- 输入字段：`user_id`, `day_rate`, `expired_time`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/fee.py:152` · `UserMarginDayRateResource`

### MARGIN-049 · 用户-特殊配置-特殊杠杆日息->删除 

- 接口声明：`DELETE /day-rate`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/fee.py:196` · `UserMarginDayRateResource`

### MARGIN-050 · 币币-杠杆-还币记录

- 接口声明：`GET `
- 输入字段：`market_type`, `flat_type`, `status`, `coin_type`, `search_keyword`, `margin_flat_history_id`, `margin_loan_order_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/flat.py:19` · `FlatResource`

### MARGIN-051 · 币币-杠杆-基金余额

- 接口声明：`GET /balance`
- 输入字段：`page`, `limit`, `asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/fund.py:19` · `FundBalanceResource`

### MARGIN-052 · 币币-杠杆-基金流水

- 接口声明：`GET /history`
- 输入字段：`start_time`, `end_time`, `asset`, `history_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/fund.py:74` · `FundHistoryResource`

### MARGIN-053 · 币币-杠杆配置-普通指数配置

- 接口声明：`GET `
- 输入字段：`market`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/index.py:52` · `MarginIndexResource`

### MARGIN-054 · 币币-杠杆配置-普通指数配置-添加普通指数配置

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/index.py:125` · `MarginIndexResource`

### MARGIN-055 · 币币-杠杆配置-普通指数配置-编辑普通指数配置

- 接口声明：`PUT `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/index.py:159` · `MarginIndexResource`

### MARGIN-056 · 杠杆-指数价格-特殊币种映射配置修改

- 接口声明：`POST /special-asset/mapping`
- 输入字段：`exchange_name`, `old`, `new`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/index.py:222` · `MarginSpecialIndexMappingResource`

### MARGIN-057 · 杠杆-指数价格-特殊币种映射配置删除

- 接口声明：`DELETE /special-asset/mapping`
- 输入字段：`exchange_name`, `old`, `new`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/index.py:243` · `MarginSpecialIndexMappingResource`

### MARGIN-058 · 杠杆-通知更新杠杆指数配置

- 接口声明：`PUT /update-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/index.py:269` · `UpdateConfigResource`

### MARGIN-059 · 币币-杠杆-借币记录

- 接口声明：`GET `
- 输入字段：`market_type`, `status`, `coin_type`, `order_type`, `search_keyword`, `margin_loan_order_id`, `margin_liquidation_history_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/loan.py:36` · `LoanResource`

### MARGIN-060 · 币币-杠杆-借币排名

- 接口声明：`GET /rank`
- 输入字段：`coin_type`, `market_type`, `search_keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/loan.py:136` · `LoanRankResource`

### MARGIN-061 · 币币-杠杆-杠杆持仓

- 接口声明：`GET `
- 输入字段：`market_type`, `user_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/margin/position.py:36` · `PositionResource`

### MARGIN-062 · 借贷-借币配置列表 

- 接口声明：`GET /loan-assets`
- 输入字段：`asset`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:93` · `LoanAssetsResource`

### MARGIN-063 · 借贷-新增借币配置 

- 接口声明：`POST /loan-assets`
- 输入字段：`asset`, `max_loan_amount`, `initial_ltv`, `warning_ltv`, `min_liquidation_ltv`, `status`, `liq_rates`
- 显式控制：lock_request()
- 代码依据：`app/api/admin/pledge.py:225` · `LoanAssetsResource`

### MARGIN-064 · 借贷-编辑借币配置 

- 接口声明：`PUT /loan-assets`
- 输入字段：`asset`, `max_loan_amount`, `initial_ltv`, `warning_ltv`, `min_liquidation_ltv`, `status`, `liq_rates`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:293` · `LoanAssetsResource`

### MARGIN-065 · 借贷-借币配置开关 

- 接口声明：`PATCH /loan-assets`
- 输入字段：`asset`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:373` · `LoanAssetsResource`

### MARGIN-066 · 借贷-质押币档位配置列表 

- 接口声明：`GET /pledge-asset-stages`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:406` · `PledgeAssetStagesResource`

### MARGIN-067 · 借贷-新增质押币档位配置 

- 接口声明：`POST /pledge-asset-stages`
- 输入字段：`stage`, `collateral_ratio`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:428` · `PledgeAssetStagesResource`

### MARGIN-068 · 借贷-修改质押币档位配置 

- 接口声明：`PUT /pledge-asset-stages`
- 输入字段：`stage`, `collateral_ratio`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:456` · `PledgeAssetStagesResource`

### MARGIN-069 · 借贷-质押币配置列表 

- 接口声明：`GET /pledge-assets`
- 输入字段：`asset`, `status`, `stage`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:486` · `PledgeAssetResource`

### MARGIN-070 · 借贷-新增质押币配置 

- 接口声明：`POST /pledge-assets`
- 输入字段：`asset`, `stage`, `max_pledge_usd`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:538` · `PledgeAssetResource`

### MARGIN-071 · 借贷-修改质押币配置 

- 接口声明：`PUT /pledge-assets`
- 输入字段：`asset`, `stage`, `max_pledge_usd`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:578` · `PledgeAssetResource`

### MARGIN-072 · 借贷-质押币配置开关 

- 接口声明：`PATCH /pledge-assets`
- 输入字段：`asset`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:618` · `PledgeAssetResource`

### MARGIN-073 · 用户-特殊配置-特殊借贷费率->列表 

- 接口声明：`GET /user-rates`
- 输入字段：`asset`, `user_id`, `page`, `limit`, `active_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:680` · `LoanAssetUserRatesResource`

### MARGIN-074 · 用户-特殊配置-特殊借贷费率->新增 

- 接口声明：`POST /user-rates`
- 输入字段：`user_id`, `asset`, `day_rate`, `expired_time`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:748` · `LoanAssetUserRatesResource`

### MARGIN-075 · 用户-特殊配置-特殊借贷费率->编辑 

- 接口声明：`PUT /user-rates`
- 输入字段：`id`, `day_rate`, `expired_time`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:792` · `LoanAssetUserRatesResource`

### MARGIN-076 · 用户-特殊配置-特殊借贷费率->删除 

- 接口声明：`DELETE /user-rates`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:828` · `LoanAssetUserRatesResource`

### MARGIN-077 · 用户-特殊配置-借贷特殊配置-特殊借贷上限-列表

- 接口声明：`GET /user-limits`
- 输入字段：`asset`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:855` · `LoanAssetUserLimitsResource`

### MARGIN-078 · 用户-特殊配置-借贷特殊配置-特殊借贷上限-新增

- 接口声明：`POST /user-limits`
- 输入字段：`user_id`, `asset`, `max_loan_amount`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:902` · `LoanAssetUserLimitsResource`

### MARGIN-079 · 用户-特殊配置-借贷特殊配置-特殊借贷上限-编辑

- 接口声明：`PUT /user-limits`
- 输入字段：`id`, `max_loan_amount`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:952` · `LoanAssetUserLimitsResource`

### MARGIN-080 · 用户-特殊配置-借贷特殊配置-特殊借贷上限-删除

- 接口声明：`DELETE /user-limits`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:995` · `LoanAssetUserLimitsResource`

### MARGIN-081 · 借贷-清算白名单列表 

- 接口声明：`GET /liq-whitelist`
- 输入字段：`user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1034` · `PledgeLiqWhitelistUserResource`

### MARGIN-082 · 借贷-清算白名单-新增 

- 接口声明：`POST /liq-whitelist`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1070` · `PledgeLiqWhitelistUserResource`

### MARGIN-083 · 借贷-清算白名单-编辑 

- 接口声明：`PUT /liq-whitelist`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1107` · `PledgeLiqWhitelistUserResource`

### MARGIN-084 · 借贷-清算白名单-删除 

- 接口声明：`DELETE /liq-whitelist`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1138` · `PledgeLiqWhitelistUserResource`

### MARGIN-085 · 用户详情-借贷账户 

- 接口声明：`GET /user-accounts`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1181` · `UserPledgeAccountsResource`

### MARGIN-086 · 借贷-借币记录列表（仓位） 

- 接口声明：`GET /positions`
- 输入字段：`asset`, `user_id`, `position_id`, `status`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1271` · `PledgePositionsResource`

### MARGIN-087 · 借贷-借币详情 

- 接口声明：`GET /position-detail`
- 输入字段：`position_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1412` · `PledgePositionDetailResource`

### MARGIN-088 · 借贷-借贷持仓-仓位质押币明细 

- 接口声明：`GET /position-pledge-assets`
- 输入字段：`position_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1486` · `PledgePosPledgeAssetsResource`

### MARGIN-089 · 借贷-借币详情-相关记录 

- 接口声明：`GET /position/relation-history`
- 输入字段：`history_type`, `asset`, `user_id`, `position_id`, `start`, `end`, `repay_status`, `transfer_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1548` · `PledgePositionRelationHisResource`

### MARGIN-090 · 借贷-强平记录列表 

- 接口声明：`GET /liq-list`
- 输入字段：`asset`, `user_id`, `position_id`, `status`, `has_fund_pay`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1614` · `PledgeLiqListResource`

### MARGIN-091 · 借贷-兑换订单列表 

- 接口声明：`GET /exchange-order-list`
- 输入字段：`exchange_id`, `market`, `side`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1716` · `PledgeExchangeOrderListResource`

### MARGIN-092 · 借贷-质押币持仓详情 

- 接口声明：`GET /active-position-detail`
- 输入字段：`user_id`, `loan_asset`, `pledge_asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1810` · `PledgeActivePositionDetailResource`

### MARGIN-093 · 借贷-质押币持仓 

- 接口声明：`GET /active-position-summary`
- 输入字段：`loan_asset`, `pledge_asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1892` · `PledgeActivePositionSummaryResource`

### MARGIN-094 · 借贷-借币记录列表（订单） 

- 接口声明：`GET /loan-order-list`
- 输入字段：`loan_order_id`, `user_id`, `position_id`, `asset`, `status`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:1939` · `PledgeLoanOrderListResource`

### MARGIN-095 · 借贷-借币订单详情 

- 接口声明：`GET /loan-order-detail`
- 输入字段：`loan_order_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:2018` · `PledgeLoanOrderDetailResource`

### MARGIN-096 · 借贷-借币订单详情-相关记录 

- 接口声明：`GET /loan-order/relation-history`
- 输入字段：`history_type`, `asset`, `user_id`, `position_id`, `loan_order_id`, `start`, `end`, `repay_type`, `renew_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:2064` · `PledgeLoanOrderRelationHisResource`

### MARGIN-097 · 借贷-还币记录（借币订单） 

- 接口声明：`GET /loan-order/repay-history`
- 输入字段：`history_id`, `loan_order_id`, `user_id`, `position_id`, `asset`, `type`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pledge.py:2121` · `PledgeLoanOrderRepayHistoryResource`

### MARGIN-098 · 报表-杠杆-全站

- 接口声明：`GET /deals`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:51` · `DailyMarginDealsResource`

### MARGIN-099 · 报表-杠杆-币种

- 接口声明：`GET /assets`
- 输入字段：`report_type`, `start_date`, `end_date`, `asset`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:150` · `DailyMarginAssetResource`

### MARGIN-100 · 报表-杠杆-币种-异步下载

- 接口声明：`GET /assets-async-download`
- 输入字段：`report_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:235` · `DailyMarginAssetAsyncDownloadResource`

### MARGIN-101 · 报表-杠杆报表-币种详情 

- 接口声明：`GET /asset-detail`
- 输入字段：`report_type`, `report_date`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:262` · `DailyMarginAssetDetailResource`

### MARGIN-102 · 报表-杠杆-市场

- 接口声明：`GET /markets`
- 输入字段：`report_type`, `start_date`, `end_date`, `market`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:350` · `DailyMarginMarketResource`

### MARGIN-103 · 报表-杠杆报表-市场详情 

- 接口声明：`GET /market-detail`
- 输入字段：`report_type`, `report_date`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:425` · `DailyMarginMarketDetailResource`

### MARGIN-104 · 报表-杠杆-爆仓

- 接口声明：`GET /liquidation`
- 输入字段：`report_type`, `start_date`, `end_date`, `market`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:511` · `MarginLiquidationResource`

### MARGIN-105 · 报表-杠杆-爆仓聚合统计

- 接口声明：`GET /liquidation-summary`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:565` · `MarginLiquidationSummaryResource`

### MARGIN-106 · 报表-杠杆-保险基金

- 接口声明：`GET /margin-fund`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `asset`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/margin.py:654` · `MarginFundReportResource`

### MARGIN-107 · 报表-质押报表-全站报表 

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `asset`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/pledge.py:58` · `PledgeSiteReportResource`

### MARGIN-108 · 报表-质押报表-爆仓全站报表 

- 接口声明：`GET /liq/site-report`
- 输入字段：`report_type`, `asset`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/pledge.py:181` · `PledgeLiqSiteReportResource`

### MARGIN-109 · 借贷报表-币种-质押币详情 

- 接口声明：`GET /pledge-asset-report`
- 输入字段：`report_type`, `loan_asset`, `pledge_asset`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/pledge.py:273` · `PledgeAssetReportResource`

### MARGIN-110 · 借贷报表-爆仓-币种详情 

- 接口声明：`GET /liq/pledge-asset-report`
- 输入字段：`report_type`, `loan_asset`, `pledge_asset`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/pledge.py:347` · `PledgeLiqAssetReportResource`

### MARGIN-111 · CreditInfo.get（用途待确认）

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/credit.py:33` · `CreditInfo`

### MARGIN-112 · CreditStatistic.get（用途待确认）

- 接口声明：`GET /statistic`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/credit.py:63` · `CreditStatistic`

### MARGIN-113 · CreditHistoryResource.get（用途待确认）

- 接口声明：`GET /history`
- 输入字段：`asset`, `credit_type`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/credit.py:109` · `CreditHistoryResource`

### MARGIN-114 · CreditFlatInfo.get（用途待确认）

- 接口声明：`GET /flat/info`
- 输入字段：`coin_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/credit.py:150` · `CreditFlatInfo`

### MARGIN-115 · CreditToFlat.post（用途待确认）

- 接口声明：`POST /to/flat`
- 输入字段：`coin_type`, `flat_amount`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/credit.py:189` · `CreditToFlat`

### MARGIN-116 · AccountListResource.get（用途待确认）

- 接口声明：`GET /account/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:50` · `AccountListResource`

### MARGIN-117 · IndexResource.get（用途待确认）

- 接口声明：`GET /index`
- 输入字段：`market_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/margin.py:67` · `IndexResource`

### MARGIN-118 · TransferResource.post（用途待确认）

- 接口声明：`POST /transfer`
- 输入字段：`from_account`, `to_account`, `coin_type`, `amount`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.MARGIN])
- 代码依据：`app/api/frontend/margin.py:122` · `TransferResource`

### MARGIN-119 · TransferListResource.get（用途待确认）

- 接口声明：`GET /transfer/history`
- 输入字段：`page`, `limit`, `op`
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:162` · `TransferListResource`

### MARGIN-120 · UserStatusResource.get（用途待确认）

- 接口声明：`GET /enable/status`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:213` · `UserStatusResource`

### MARGIN-121 · UserStatusResource.post（用途待确认）

- 接口声明：`POST /enable/status`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:221` · `UserStatusResource`

### MARGIN-122 · MarketDetailResource.get（用途待确认）

- 接口声明：`GET /market/detail`
- 输入字段：`market_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/margin.py:254` · `MarketDetailResource`

### MARGIN-123 · MarginAssetDayRateResource.get（用途待确认）

- 接口声明：`GET /asset/day-rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/margin.py:299` · `MarginAssetDayRateResource`

### MARGIN-124 · MarketLeverageResource.get（用途待确认）

- 接口声明：`GET /market/leverage`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/margin.py:310` · `MarketLeverageResource`

### MARGIN-125 · InsuranceResource.get（用途待确认）

- 接口声明：`GET /fund/history`
- 输入字段：`page`, `limit`, `coin_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/margin.py:352` · `InsuranceResource`

### MARGIN-126 · InsuranceChartResource.get（用途待确认）

- 接口声明：`GET /fund/chart`
- 输入字段：`coin_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/margin.py:397` · `InsuranceChartResource`

### MARGIN-127 · LoanResource.post（用途待确认）

- 接口声明：`POST /loan`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.MARGIN]); lock_request()
- 代码依据：`app/api/frontend/margin.py:446` · `LoanResource`

### MARGIN-128 · LoanResource.get（用途待确认）

- 接口声明：`GET /loan`
- 输入字段：`account_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:465` · `LoanResource`

### MARGIN-129 · LoanHistoryResource.get（用途待确认）

- 接口声明：`GET /loan/history`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:520` · `LoanHistoryResource`

### MARGIN-130 · LoanRenewResource.post（用途待确认）

- 接口声明：`POST /loan/renew`
- 输入字段：`loan_id`, `renew`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.MARGIN])
- 代码依据：`app/api/frontend/margin.py:540` · `LoanRenewResource`

### MARGIN-131 · FlatResource.post（用途待确认）

- 接口声明：`POST /flat`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:573` · `FlatResource`

### MARGIN-132 · LoanOrderFlatHistoryResource.get（用途待确认）

- 接口声明：`GET /flat/history/<int:loan_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:625` · `LoanOrderFlatHistoryResource`

### MARGIN-133 · FlatHistoryResource.get（用途待确认）

- 接口声明：`GET /flat/history`
- 输入字段：`page`, `limit`, `market`, `flat_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:645` · `FlatHistoryResource`

### MARGIN-134 · MarginLoanUnflatAmountResource.get（用途待确认）

- 接口声明：`GET /unflat`
- 输入字段：`account_id`, `market_type`, `side`, `price`
- 显式控制：require_login
- 代码依据：`app/api/frontend/margin.py:695` · `MarginLoanUnflatAmountResource`

### MARGIN-135 · 可借币种的列表 

- 接口声明：`GET /loanable-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/pledge.py:58` · `LoanableAssetsResource`

### MARGIN-136 · 可质押币种的列表 

- 接口声明：`GET /collateral-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/pledge.py:84` · `PledgeAssetsResource`

### MARGIN-137 · 质押账户列表 

- 接口声明：`GET /accounts`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:96` · `PledgeAccountsResource`

### MARGIN-138 · 获取剩余最大借币数 

- 接口声明：`POST /loan/amount`
- 输入字段：`asset`, `pledge_assets`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pledge.py:158` · `LoanAmountResource`

### MARGIN-139 · 提交借币 

- 接口声明：`POST /loan`
- 输入字段：`asset`, `amount`, `pledge_assets`, `is_renew`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pledge.py:191` · `PledgeLoanResource`

### MARGIN-140 · 增加质押币 

- 接口声明：`POST /position/collateral/add`
- 输入字段：`position_id`, `pledge_assets`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pledge.py:282` · `PositionAddCollateralResource`

### MARGIN-141 · 获取可减少质押币的数目 

- 接口声明：`GET /position/collateral/remove`
- 输入字段：`position_id`, `asset`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:340` · `PositionRemoveCollateralResource`

### MARGIN-142 · 减少质押币 

- 接口声明：`POST /position/collateral/remove`
- 输入字段：`position_id`, `asset`, `amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pledge.py:362` · `PositionRemoveCollateralResource`

### MARGIN-143 · 还币(用借币币种) 

- 接口声明：`POST /position/repay`
- 输入字段：`position_id`, `amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pledge.py:397` · `PositionRepayResource`

### MARGIN-144 · 还币(用质押币种) / 平仓 

- 接口声明：`POST /position/close`
- 输入字段：`position_id`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pledge.py:444` · `PositionCloseResource`

### MARGIN-145 · 仓位详情 

- 接口声明：`GET /position/<int:position_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:489` · `PositionDetailResource`

### MARGIN-146 · 仓位历史记录 

- 接口声明：`GET /position/history`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:554` · `PositionHistoryResource`

### MARGIN-147 · 仓位的借币记录 

- 接口声明：`GET /position/loan/history`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:613` · `PositionLoanHistoryResource`

### MARGIN-148 · 仓位的还币记录 

- 接口声明：`GET /position/repay/history`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:670` · `PositionRepayHistoryResource`

### MARGIN-149 · 仓位的质押记录 

- 接口声明：`GET /position/collateral/history`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:736` · `PositionCollateralHistoryResource`

### MARGIN-150 · 仓位的利息记录 

- 接口声明：`GET /position/interest/history`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:784` · `PositionInterestHistoryResource`

### MARGIN-151 · 借币订单记录 

- 接口声明：`GET /order/history`
- 输入字段：`loan_asset`, `status`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:831` · `LoanOrderHistoryResource`

### MARGIN-152 · 借币订单-修改续借开关 

- 接口声明：`POST /order/renew`
- 输入字段：`loan_order_id`, `is_renew`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:899` · `LoanOrderRenewResource`

### MARGIN-153 · 借币订单-还币历史 

- 接口声明：`GET /order/repay/history`
- 输入字段：`loan_order_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:930` · `LoanOrderRepayHistoryResource`

### MARGIN-154 · 借币订单-利息历史 

- 接口声明：`GET /order/interest/history`
- 输入字段：`loan_order_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:994` · `LoanOrderInterestHistoryResource`

### MARGIN-155 · 借币订单-续借历史 

- 接口声明：`GET /order/renew/history`
- 输入字段：`loan_order_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/pledge.py:1101` · `LoanOrderRenewHistoryResource`

### MARGIN-156 · CreditInfoResource.get（用途待确认）

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/assets/credit.py:24` · `CreditInfoResource`

### MARGIN-157 · CreditBalanceResource.get（用途待确认）

- 接口声明：`GET /balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/credit.py:50` · `CreditBalanceResource`

### MARGIN-158 · MarginConfigResource.get（用途待确认）

- 接口声明：`GET /interest-limit`
- 输入字段：`market`, `ccy`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/margin.py:51` · `MarginConfigResource`

### MARGIN-159 · MarginBorrowHistoryResource.get（用途待确认）

- 接口声明：`GET /borrow-history`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/margin.py:99` · `MarginBorrowHistoryResource`

### MARGIN-160 · BorrowResource.post（用途待确认）

- 接口声明：`POST /borrow`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth; require_user_permission(sub_account_permissions=[SubAccountPermission.MARGIN]); api_permission_deco(check_trade=True); lock_request(with_user=True)
- 代码依据：`app/api/v2/assets/margin.py:157` · `BorrowResource`

### MARGIN-161 · RepayResource.post（用途待确认）

- 接口声明：`POST /repay`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth; api_permission_deco(check_trade=True)
- 代码依据：`app/api/v2/assets/margin.py:201` · `RepayResource`

### MARGIN-162 · BalanceResource.get（用途待确认）

- 接口声明：`GET /balance`
- 输入字段：`market`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/margin.py:245` · `BalanceResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/admin/margin/__init__.py`
- `tests/api/admin/margin/test_burst.py`
- `tests/api/frontend/test_margin.py`
- `tests/business/margin/__init__.py`
- `tests/business/margin/test_helper.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
