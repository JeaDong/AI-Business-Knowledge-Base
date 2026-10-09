# 资产、充值与提现 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### ASSETS-001 · 运营>充值找回>订单管理-列表 

- 接口声明：`GET /list`
- 输入字段：`start_time`, `end_time`, `user_id`, `id`, `asset`, `chain`, `tx_id`, `type`, `status`, `sort_name`, `sort_type`, `is_high_total_usd`, `auditor_id`, `next`, `cur_id`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:120` · `AbnormalDepositApplicationsResource`

### ASSETS-002 · 运营>充值找回>订单管理-编辑备注、审核页面-编辑币种、数目、公链 

- 接口声明：`PATCH /list`
- 输入字段：`id`, `remark`, `jump_url`, `asset`, `chain`, `asset_rate`, `tx_amount`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:331` · `AbnormalDepositApplicationsResource`

### ASSETS-003 · 运营>充值找回>审核详情 

- 接口声明：`GET /detail/<int:application_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:525` · `AbnormalDepositApplicationDetailResource`

### ASSETS-004 · 运营-充值找回-获取充值地址详情

- 接口声明：`GET /deposit-address`
- 输入字段：`user_id`, `chain`, `address`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:685` · `DepositAddresse`

### ASSETS-005 · 运营-充值找回-获取异常充值详情

- 接口声明：`GET /abnormal-deposit`
- 输入字段：`tx_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:709` · `AbnormalDepositResorce`

### ASSETS-006 · 运营-充值找回-更新当前编辑者

- 接口声明：`POST /<int:id_>/auditors`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:726` · `AbnormalDepositResource`

### ASSETS-007 · 运营>充值找回>审核详情-设置类型 

- 接口声明：`POST /edit-type/<int:application_id>`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:747` · `AbnormalDepositApplicationEditTypeResource`

### ASSETS-008 · 运营>充值找回>审核详情-编辑手续费 

- 接口声明：`POST /edit-expect-fee`
- 输入字段：`id`, `expect_fee_amount`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:819` · `AbnormalDepositApplyEditExpectFeeResource`

### ASSETS-009 · 运营>充值找回>审核详情-初审 

- 接口声明：`POST /audit/<int:application_id>`
- 输入字段：`audit_status`, `rejection_reason`, `is_custom_reason`, `custom_reject_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:877` · `AbnormalDepositApplicationAuditResource`

### ASSETS-010 · " 运营>充值找回>审核详情-复审（小于1W刀） 

- 接口声明：`POST /check/<int:application_id>`
- 输入字段：`audit_status`, `rejection_reason`, `is_custom_reason`, `custom_reject_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:978` · `AbnormalDepositApplicationCheckResource`

### ASSETS-011 · " 运营>充值找回>审核详情-复审（大于1W刀） 

- 接口声明：`POST /super-check/<int:application_id>`
- 输入字段：`audit_status`, `rejection_reason`, `is_custom_reason`, `custom_reject_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1213` · `AbnormalDepositApplicationSuperCheckResource`

### ASSETS-012 · " 运营>充值找回>审核详情-三审 

- 接口声明：`POST /double-check/<int:application_id>`
- 输入字段：`audit_status`, `rejection_reason`, `is_custom_reason`, `custom_reject_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1231` · `AbnormalDepositApplicationDoubleCheckResource`

### ASSETS-013 · 运营>充值找回>审核详情-资产变更重试 

- 接口声明：`POST /retry-asset-change/<int:application_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1351` · `AbnormalDepositApplicationRetryAssetChangeResource`

### ASSETS-014 · 运营>充值找回>批量资产变更重试 

- 接口声明：`POST /batch-retry-asset-change`
- 输入字段：`application_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1385` · `AbnormalDepositApplicationBatchRetryAssetChangeResource`

### ASSETS-015 · 运营>充值找回>批量分配审核人

- 接口声明：`POST /auditors`
- 输入字段：`auditor_ids`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1425` · `AbnormalDepositApplicationAssignAuditorsResource`

### ASSETS-016 · 运营>充值找回>批量解绑审核人

- 接口声明：`PATCH /auditors`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1461` · `AbnormalDepositApplicationAssignAuditorsResource`

### ASSETS-017 · 运营>充值找回>变更记录-列表 

- 接口声明：`GET /change-log`
- 输入字段：`start_time`, `end_time`, `user_id`, `admin_user_id`, `application_id`, `change_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1493` · `AbnormalDepositApplicationChangeLogResource`

### ASSETS-018 · 运营>充值找回>批量自动拒绝 

- 接口声明：`POST /auto-reject`
- 输入字段：`application_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1563` · `AbnormalDepositApplicationAutoRejectResource`

### ASSETS-019 · 运营>充值找回>提醒补充手续费 

- 接口声明：`POST /send-notice`
- 输入字段：`application_id`, `notice_type`, `rejection_reason`, `is_custom_reason`, `custom_reject_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/abnormal_deposit_application.py:1669` · `AbnormalDepositApplicationSendNoticeResource`

### ASSETS-020 · 运营-活动-充值福利-列表 

- 接口声明：`GET /activity`
- 输入字段：`id`, `name`, `status`, `active_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:210` · `DepositBonusActivityResource`

### ASSETS-021 · 运营-活动-充值福利-添加活动 

- 接口声明：`POST /activity`
- 输入字段：`start_time`, `end_time`, `zendesk_url`, `asset`, `chains`, `threshold`, `cover`, `configs`, `details`, `risk_settings`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:399` · `DepositBonusActivityResource`

### ASSETS-022 · 运营-活动-充值福利-编辑活动 

- 接口声明：`PUT /activity`
- 输入字段：`id`, `start_time`, `end_time`, `zendesk_url`, `asset`, `chains`, `threshold`, `cover`, `configs`, `details`, `risk_settings`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:559` · `DepositBonusActivityResource`

### ASSETS-023 · 运营-活动-充值福利-操作上下架/删除/提交审核 

- 接口声明：`PATCH /activity`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:797` · `DepositBonusActivityResource`

### ASSETS-024 · 运营-活动-充值福利-审核 

- 接口声明：`POST /activity/<int:id_>/audit`
- 输入字段：`status`, `remark`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/activity/deposit_bonus.py:853` · `DepositBonusActivityAuditResource`

### ASSETS-025 · 运营-活动-充值福利-活动详情

- 接口声明：`GET /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:910` · `DepositBonusActivityDetailResource`

### ASSETS-026 · 运营-活动-充值福利-参与详情统计 

- 接口声明：`GET /activity/statistics`
- 输入字段：`activity_id`, `config_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1079` · `DepositBonusActivityStatisticsResource`

### ASSETS-027 · 运营-活动-充值福利-参与详情 

- 接口声明：`GET /activity/history`
- 输入字段：`activity_id`, `config_id`, `status`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1212` · `DepositBonusActivityHistoryResource`

### ASSETS-028 · 运营-活动-充值福利-报名用户状态修改

- 接口声明：`PUT /activity/history`
- 输入字段：`user_id`, `id`, `activity_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1457` · `DepositBonusActivityHistoryResource`

### ASSETS-029 · 运营-活动-充值福利-参与详情用户校验

- 接口声明：`PATCH /activity/history`
- 输入字段：`activity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1494` · `DepositBonusActivityHistoryResource`

### ASSETS-030 · 运营-活动-充值福利-派奖

- 接口声明：`POST /activity/history`
- 输入字段：`activity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1604` · `DepositBonusActivityHistoryResource`

### ASSETS-031 · 运营-活动-充值福利-参与详情-异步下载

- 接口声明：`GET /activity/history/async-download`
- 输入字段：`activity_id`, `config_id`, `status`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1676` · `DepositBonusActivityHistoryReportAsyncDownloadResource`

### ASSETS-032 · 运营-活动-充值福利-参与详情-模版下载

- 接口声明：`GET /activity/history/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1746` · `DepositBonusActivityHistoryTemplateResource`

### ASSETS-033 · 运营-活动-充值福利-参与详情-批量导入

- 接口声明：`POST /activity/history/import`
- 输入字段：`activity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/deposit_bonus.py:1760` · `DepositBonusActivityHistoryImportResource`

### ASSETS-034 · 运营-活动-资产证明-快照列表

- 接口声明：`GET /snapshots`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/merkle_balance.py:17` · `MerkleSnapshotsResource`

### ASSETS-035 · 运营-活动-资产证明-查询

- 接口声明：`GET /snapshot`
- 输入字段：`snapshot`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/merkle_balance.py:32` · `MerkleSnapshotResource`

### ASSETS-036 · 现货-碎币兑换-订单

- 接口声明：`GET /history`
- 输入字段：`user_id`, `asset`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/asset_conversion.py:48` · `AssetConversionHistoryResource`

### ASSETS-037 · 现货-碎币兑换-排名

- 接口声明：`GET /rank`
- 输入字段：`type`, `time_period`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/asset_conversion.py:116` · `AssetConversionRankResource`

### ASSETS-038 · 币种列表

- 接口声明：`GET `
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/asset_identity.py:15` · `AssetIdentityResource`

### ASSETS-039 · 钱包-资产变更-模板

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/asset_update.py:49` · `AssetUpdateTemplateResource`

### ASSETS-040 · 钱包-资产变更-列表

- 接口声明：`GET /`
- 输入字段：`asset`, `status`, `type`, `remark`, `user_id`, `export`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/asset_update.py:97` · `AssetUpdateListResource`

### ASSETS-041 · 钱包-资产变更-批量上传

- 接口声明：`POST /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:166` · `AssetUpdateListResource`

### ASSETS-042 · 钱包-资产变更-批量初审

- 接口声明：`POST /batch-audit`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:194` · `AssetUpdateBatchAuditResource`

### ASSETS-043 · 钱包-资产变更-批量复审

- 接口声明：`POST /batch-check`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:237` · `AssetUpdateBatchCheckResource`

### ASSETS-044 · 钱包-资产变更-批量删除

- 接口声明：`POST /batch-delete`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:318` · `AssetUpdateBatchDeleteResource`

### ASSETS-045 · 钱包-小额资产恢复-列表

- 接口声明：`GET /cleaned-resume`
- 输入字段：`user_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/asset_update.py:355` · `CleanedAssetResumeResource`

### ASSETS-046 · 钱包-小额资产恢复-添加

- 接口声明：`POST /cleaned-resume`
- 输入字段：`user_id`, `asset`, `amount`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:405` · `CleanedAssetResumeResource`

### ASSETS-047 · 钱包-小额资产恢复-审核

- 接口声明：`PATCH /cleaned-resume`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:488` · `CleanedAssetResumeResource`

### ASSETS-048 · 钱包-小额资产恢复-删除

- 接口声明：`DELETE /cleaned-resume`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:542` · `CleanedAssetResumeResource`

### ASSETS-049 · 钱包-小额资产恢复-下载模板

- 接口声明：`GET /cleaned-resume-batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/asset_update.py:573` · `CleanedAssetResumeBatchResource`

### ASSETS-050 · 钱包-小额资产恢复-批量上传

- 接口声明：`POST /cleaned-resume-batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/asset_update.py:586` · `CleanedAssetResumeBatchResource`

### ASSETS-051 · 币种列表

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:29` · `AssetsResource`

### ASSETS-052 · 币种配置

- 接口声明：`GET /<asset>/configs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:53` · `AssetChainConfigsResource`

### ASSETS-053 · 币种配置单项设置

- 接口声明：`PUT /<asset>/configs/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:72` · `AssetConfigManagementResource`

### ASSETS-054 · 币种配置单项重置

- 接口声明：`DELETE /<asset>/configs/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:101` · `AssetConfigManagementResource`

### ASSETS-055 · 币种-链信息列表

- 接口声明：`GET /to-chains`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:126` · `AssetChainsResource`

### ASSETS-056 · 币种-链配置信息

- 接口声明：`GET /<asset>/chain-configs/<chain>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:145` · `AssetChainConfigResource`

### ASSETS-057 · 币种链配置单项设置

- 接口声明：`PUT /<asset>/chain-configs/<chain>/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:161` · `AssetChainConfigManagementResource`

### ASSETS-058 · 币种链配置单项重置

- 接口声明：`DELETE /<asset>/chain-configs/<chain>/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:195` · `AssetChainConfigManagementResource`

### ASSETS-059 · web钱包管理-Coinex Wallet 公链映射-查看信息

- 接口声明：`GET /coinex_wallet_support`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:232` · `CoinexWalletSupportMapResource`

### ASSETS-060 · web钱包管理-Coinex Wallet 公链映射-修改映射

- 接口声明：`PUT /coinex_wallet_support`
- 输入字段：`chain_map`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/assets.py:256` · `CoinexWalletSupportMapResource`

### ASSETS-061 · 钱包-提成发放-模版下载

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/commission_pay.py:40` · `CommissionPayTemplateResource`

### ASSETS-062 · 钱包-提成发放-列表

- 接口声明：`GET /list`
- 输入字段：`asset`, `status`, `type`, `remark`, `user_id`, `export`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/commission_pay.py:84` · `CommissionPayListResource`

### ASSETS-063 · 钱包-提成发放-批量上传

- 接口声明：`POST /list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/commission_pay.py:155` · `CommissionPayListResource`

### ASSETS-064 · 钱包-提成发放-批量初审

- 接口声明：`POST /batch-audit`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/commission_pay.py:182` · `CommissionPayBatchAuditResource`

### ASSETS-065 · 钱包-提成发放-批量复审

- 接口声明：`POST /batch-check`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/commission_pay.py:227` · `CommissionPayBatchCheckResource`

### ASSETS-066 · 钱包-提成发放-批量删除

- 接口声明：`POST /batch-delete`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/commission_pay.py:281` · `CommissionPayBatchDeleteResource`

### ASSETS-067 · 钱包-web 充提-充提排名

- 接口声明：`GET /rank`
- 输入字段：`time_type`, `asset`, `user_type`, `sort`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposit_withdrawal.py:36` · `DepositWithdrawalRankResource`

### ASSETS-068 · 统计-资产统计-充提耗时统计

- 接口声明：`GET /latency`
- 输入字段：`scope`, `time_range`, `asset`, `chain`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposit_withdrawal.py:93` · `DepositWithdrawalLatencyResource`

### ASSETS-069 · 风控-反洗钱-全站/制裁地区用户充提排名-查询列表

- 接口声明：`GET /user-rank`
- 输入字段：`rank_type`, `period_days`, `sort_name`, `sort_type`, `report_date`, `country`, `region`, `user_type`, `clear_status`, `is_kyc`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposit_withdrawal.py:166` · `UserDepositWithdrawalRankResource`

### ASSETS-070 · 风控-反洗钱-全站/制裁地区用户充提排名-资产详情

- 接口声明：`GET /user-rank/<int:user_id>/asset-detail`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposit_withdrawal.py:462` · `UserDepositWithdrawalRankAssetDetailResource`

### ASSETS-071 · 风控-反洗钱-全站/制裁地区用户充提排名-导出

- 接口声明：`GET /user-rank/export`
- 输入字段：`rank_type`, `period_days`, `sort_name`, `sort_type`, `report_date`, `country`, `region`, `user_type`, `clear_status`, `is_kyc`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposit_withdrawal.py:522` · `UserDepositWithdrawalRankExportResource`

### ASSETS-072 · 充值记录

- 接口声明：`GET `
- 输入字段：`id`, `asset`, `chain`, `type`, `status`, `audit_type`, `start`, `end`, `user`, `tx_id`, `address`, `min_amount`, `max_amount`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:202` · `DepositsResource`

### ASSETS-073 · 充值审核列表

- 接口声明：`GET /audit`
- 输入字段：`asset`, `chain`, `review_status`, `material_status`, `auditor_id`, `type`, `risk_level`, `keyword`, `tx_id`, `deposit_id`, `start_time`, `end_time`, `audited_start_time`, `audited_end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:438` · `DepositsAuditResource`

### ASSETS-074 · 充值审核-备注

- 接口声明：`PATCH /audit`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:705` · `DepositsAuditResource`

### ASSETS-075 · 充值审核-关联 EDD

- 接口声明：`PUT /audit`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:728` · `DepositsAuditResource`

### ASSETS-076 · 充值审核-批量分配审核人

- 接口声明：`POST /audit/auditors`
- 输入字段：`auditor_ids`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:778` · `DepositAuditAssignAuditorsResource`

### ASSETS-077 · 充值审核-批量取消分配

- 接口声明：`PATCH /audit/auditors`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:807` · `DepositAuditAssignAuditorsResource`

### ASSETS-078 · 风控-充值审核-下载Excel批量审核模板

- 接口声明：`GET /batch-audit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:839` · `DepositsBatchAuditResource`

### ASSETS-079 · 风控-充值审核-Excel批量审核

- 接口声明：`POST /batch-audit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:848` · `DepositsBatchAuditResource`

### ASSETS-080 · 反洗钱系统-充值审核-发起或切换退回

- 接口声明：`PUT /audit/<int:audit_id>/refund`
- 输入字段：`refund_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:933` · `DepositRefundResource`

### ASSETS-081 · 反洗钱系统-充值审核-审核退回地址并提交钱包

- 接口声明：`PUT /audit/<int:audit_id>/refund/review`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:970` · `DepositRefundReviewResource`

### ASSETS-082 · 风控-充值审核-下载批量提交钱包退回模板

- 接口声明：`GET /audit/refunds/batch-review`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:996` · `DepositRefundBatchReviewResource`

### ASSETS-083 · 风控-充值审核-按审核 ID 批量提交钱包退回

- 接口声明：`POST /audit/refunds/batch-review`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:1005` · `DepositRefundBatchReviewResource`

### ASSETS-084 · EDD 列表

- 接口声明：`GET /edd-audit`
- 输入字段：`keyword`, `created_by`, `source`, `review_status`, `material_status`, `tx_id`, `start_time`, `end_time`, `audited_start_time`, `audited_end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:1130` · `EDDAuditResource`

### ASSETS-085 · EDD-创建 EDD 验证

- 接口声明：`POST /edd-audit`
- 输入字段：`user_id`, `txid`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:1322` · `EDDAuditResource`

### ASSETS-086 · EDD-备注

- 接口声明：`PATCH /edd-audit`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:1375` · `EDDAuditResource`

### ASSETS-087 · 钱包管理-web钱包管理-充值审核/EDD详情

- 接口声明：`GET /edd-audit/details`
- 输入字段：`audit_id`, `edd_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:1430` · `EDDDetailResource`

### ASSETS-088 · 钱包管理-web钱包管理-充值审核/EDD详情-审核流转

- 接口声明：`PUT /edd-audit/details`
- 输入字段：`audit_id`, `edd_id`, `reject_reason`, `is_custom_reason`, `custom_reject_reason`, `module_codes`, `reason_codes`, `custom_reason`, `action`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:1704` · `EDDDetailResource`

### ASSETS-089 · 钱包管理-充值管理-充值风险评估备注

- 接口声明：`PATCH /edd-audit/details`
- 输入字段：`edd_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2025` · `EDDDetailResource`

### ASSETS-090 · 币种管理>充提弹窗配置-列表 

- 接口声明：`GET /deposit-withdraw-popup-windows`
- 输入字段：`page`, `limit`, `asset`, `chain`, `status`, `platform`, `offline_type`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2053` · `DepositWithdrawalPopupWindowsResource`

### ASSETS-091 · 币种管理>充提弹窗配置-新增弹窗 

- 接口声明：`POST /deposit-withdraw-popup-windows`
- 输入字段：`name`, `asset`, `chain`, `started_at`, `ended_at`, `platform`, `filter_type`, `whitelist_enabled`, `user_whitelist`, `groups`, `trigger_page`, `frequency`, `offline_type`, `jump_page_enabled`, `jump_type`, `jump_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2152` · `DepositWithdrawalPopupWindowsResource`

### ASSETS-092 · 币种管理>充提弹窗配置-弹窗详情

- 接口声明：`GET /deposit-withdraw-popup-windows/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2245` · `DepositWithdrawalPopupWindowResource`

### ASSETS-093 · 币种管理>充提弹窗配置-编辑弹窗 

- 接口声明：`PUT /deposit-withdraw-popup-windows/<int:id_>`
- 输入字段：`name`, `started_at`, `ended_at`, `platform`, `filter_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `trigger_page`, `frequency`, `offline_type`, `jump_page_enabled`, `jump_type`, `jump_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2298` · `DepositWithdrawalPopupWindowResource`

### ASSETS-094 · 币种管理>充提弹窗配置-编辑排序 

- 接口声明：`PATCH /deposit-withdraw-popup-windows/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2356` · `DepositWithdrawalPopupWindowResource`

### ASSETS-095 · 币种管理>充提弹窗配置-删除弹窗 

- 接口声明：`DELETE /deposit-withdraw-popup-windows/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2379` · `DepositWithdrawalPopupWindowResource`

### ASSETS-096 · 币种管理>充提弹窗配置-下架弹窗

- 接口声明：`PUT /deposit-withdraw-popup-windows/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2401` · `DepositWithdrawalPopupWindowOfflineResource`

### ASSETS-097 · 币种管理>充提弹窗配置-编辑弹窗语言

- 接口声明：`GET /deposit-withdraw-popup-windows/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2431` · `DepositWithdrawalPopupWindowLangResource`

### ASSETS-098 · 运营-通知栏-编辑内容

- 接口声明：`PUT /deposit-withdraw-popup-windows/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2445` · `DepositWithdrawalPopupWindowLangResource`

### ASSETS-099 · 币种管理>充提关闭列表 

- 接口声明：`GET /deposit-withdraw-disable-info`
- 输入字段：`page`, `limit`, `asset`, `chain`, `type`, `is_visible`, `order_type`, `operator_email`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2605` · `DepositWithdrawalDisableInfosResource`

### ASSETS-100 · 币种管理>充提关闭列表-原因配置 

- 接口声明：`PUT /deposit-withdraw-disable-info`
- 输入字段：`asset`, `chain`, `type`, `disable_at`, `reason`, `url`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2751` · `DepositWithdrawalDisableInfosResource`

### ASSETS-101 · 钱包管理-充值管理-充值风险评估审核列表

- 接口声明：`GET /kyt/audit`
- 输入字段：`keyword`, `assess_object`, `chain`, `tx_id`, `status`, `risk_level`, `start_time`, `end_time`, `updated_start_time`, `updated_end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2821` · `KYTDepositsAuditResource`

### ASSETS-102 · 钱包管理-充值管理-充值风险评估审核详情

- 接口声明：`GET /kyt/audit/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:2982` · `KYTDetailResource`

### ASSETS-103 · 钱包管理-充值管理-充值风险评估审核流转

- 接口声明：`PUT /kyt/audit/<int:id_>`
- 输入字段：`reject_reason`, `is_custom_reason`, `custom_reject_reason`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:3091` · `KYTDetailResource`

### ASSETS-104 · 钱包管理-充值管理-充值风险评估备注

- 接口声明：`PATCH /kyt/audit/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/deposits.py:3172` · `KYTDetailResource`

### ASSETS-105 · 资产锁定列表

- 接口声明：`GET /`
- 输入字段：`sort`, `asset`, `status`, `user_id`, `business`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/lock.py:43` · `LockConfigListResource`

### ASSETS-106 · 钱包-资产-资产解锁

- 接口声明：`PUT /`
- 输入字段：`user_id`, `business_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/lock.py:83` · `LockConfigListResource`

### ASSETS-107 · 钱包-资产-流动性锁定

- 接口声明：`GET /liquidity`
- 输入字段：`market`, `status`, `user_id`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/lock.py:119` · `LiquidityLockResource`

### ASSETS-108 · 钱包-资产-新增流动性锁定

- 接口声明：`POST /liquidity`
- 输入字段：`market`, `user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/lock.py:165` · `LiquidityLockResource`

### ASSETS-109 · 钱包-资产-流动性解锁

- 接口声明：`PUT /liquidity`
- 输入字段：`market`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/lock.py:207` · `LiquidityLockResource`

### ASSETS-110 · 用户-特殊配置-仅支持提现用户列表 

- 接口声明：`GET `
- 输入字段：`balance_level`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/only_withdrawal.py:36` · `OnlyWithdrawalListUsersResource`

### ASSETS-111 · 用户-特殊配置-仅支持提现用户-新增 

- 接口声明：`POST `
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/only_withdrawal.py:107` · `OnlyWithdrawalListUsersResource`

### ASSETS-112 · 用户-特殊配置-仅支持提现用户-编辑 

- 接口声明：`PATCH `
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/only_withdrawal.py:156` · `OnlyWithdrawalListUsersResource`

### ASSETS-113 · 用户-特殊配置-仅支持提现用户-删除 

- 接口声明：`DELETE `
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/only_withdrawal.py:198` · `OnlyWithdrawalListUsersResource`

### ASSETS-114 · 钱包 - 币种价格

- 接口声明：`GET `
- 输入字段：`asset`, `start`, `end`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/prices.py:27` · `AssetPricesResource`

### ASSETS-115 · SalaryPayTemplateResource.get（用途待确认）

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/salary_pay.py:42` · `SalaryPayTemplateResource`

### ASSETS-116 · 钱包-薪资发放-列表

- 接口声明：`GET /`
- 输入字段：`asset`, `status`, `type`, `remark`, `user_id`, `export`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/salary_pay.py:87` · `SalaryPayListResource`

### ASSETS-117 · 钱包-薪资发放-批量上传

- 接口声明：`POST /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/salary_pay.py:155` · `SalaryPayListResource`

### ASSETS-118 · 钱包-薪资发放-批量初审

- 接口声明：`POST /batch-audit`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/salary_pay.py:180` · `SalaryPayBatchAuditResource`

### ASSETS-119 · 钱包-薪资发放-批量复审

- 接口声明：`POST /batch-check`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/salary_pay.py:223` · `SalaryPayBatchCheckResource`

### ASSETS-120 · 钱包-薪资发放-批量删除

- 接口声明：`POST /batch-delete`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/asset/salary_pay.py:279` · `SalaryPayBatchDeleteResource`

### ASSETS-121 · 钱包-划转记录-杠杆账户

- 接口声明：`GET /margin`
- 输入字段：`asset`, `status`, `transfer_type`, `start`, `end`, `user`, `source_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/transfer_history.py:19` · `TransferHistoryMarginResource`

### ASSETS-122 · 钱包-划转记录-合约账户

- 接口声明：`GET /perpetual`
- 输入字段：`asset`, `status`, `transfer_type`, `start`, `end`, `user`, `source_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/transfer_history.py:77` · `TransferHistoryPerpetualResource`

### ASSETS-123 · 钱包-划转记录-理财账户

- 接口声明：`GET /investment`
- 输入字段：`asset`, `status`, `transfer_type`, `start`, `end`, `user`, `source_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/transfer_history.py:134` · `TransferHistoryInvestmentResource`

### ASSETS-124 · 钱包-划转记录-子账户

- 接口声明：`GET /sub_account`
- 输入字段：`asset`, `status`, `start`, `end`, `main_user_id`, `source_user_id`, `target_user_id`, `source_id`, `source_account_type`, `target_account_type`, `cursor`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/transfer_history.py:191` · `TransferHistorySubAccountResource`

### ASSETS-125 · 矿池转账记录

- 接口声明：`GET /orders`
- 输入字段：`asset`, `chain`, `status`, `start`, `end`, `order_at_start`, `order_at_end`, `user`, `pool_user_id`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/viabtc_pool.py:26` · `ViaBTCPoolOrdersResource`

### ASSETS-126 · 矿池转账订单编辑

- 接口声明：`PUT /order/<int:order_id>`
- 输入字段：`status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/viabtc_pool.py:113` · `EditViaBTCPoolOrdersResource`

### ASSETS-127 · 提现白名单列表

- 接口声明：`GET `
- 输入字段：`user`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:172` · `WhiteListResource`

### ASSETS-128 · 提现白名单添加

- 接口声明：`POST `
- 输入字段：`user`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:182` · `WhiteListResource`

### ASSETS-129 · 提现白名单编辑

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:199` · `WhiteListUserResource`

### ASSETS-130 · 提现白名单删除

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:207` · `WhiteListUserResource`

### ASSETS-131 · 免风控审核列表

- 接口声明：`GET /no-delay-list`
- 输入字段：`user`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:219` · `NoDelayUserList`

### ASSETS-132 · 免风控审核添加

- 接口声明：`POST /no-delay-list`
- 输入字段：`user`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:229` · `NoDelayUserList`

### ASSETS-133 · 免风控审核编辑

- 接口声明：`PATCH /no-delay-list/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:245` · `NoDelayUserDetail`

### ASSETS-134 · 免风控审核删除

- 接口声明：`DELETE /no-delay-list/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_whitelist.py:253` · `NoDelayUserDetail`

### ASSETS-135 · 提现记录列表

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:193` · `WithdrawalHistoryResource`

### ASSETS-136 · 提现记录编辑

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`status`, `tx_id`, `tx_fee`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:502` · `WithdrawalHistoryItemResource`

### ASSETS-137 · 批量获取浏览器地址

- 接口声明：`POST /explorer-addresses-url`
- 输入字段：`addresses`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:562` · `ExplorerAddressUrlResource`

### ASSETS-138 · 批量获取交易id浏览器地址

- 接口声明：`POST /explorer-txs-url`
- 输入字段：`txs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:579` · `ExplorerTxsUrlResource`

### ASSETS-139 · 提现多人审核列表

- 接口声明：`GET /approvers`
- 输入字段：`user_id`, `account`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:595` · `WithdrawalApproversResource`

### ASSETS-140 · 风控-风控参数配置-提现地址黑名单-列表 

- 接口声明：`GET /address-blacklist`
- 输入字段：`chain`, `address`, `memo`, `limit_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:687` · `WithdrawalAddressBlacklistResource`

### ASSETS-141 · 风控-风控参数配置-提现地址黑名单-新增 

- 接口声明：`POST /address-blacklist`
- 输入字段：`chain`, `address`, `memo`, `remark`, `limit_type`
- 显式控制：lock_request('withdrawal_address_blacklist_create')
- 代码依据：`app/api/admin/asset/withdrawals.py:749` · `WithdrawalAddressBlacklistResource`

### ASSETS-142 · 风控-风控参数配置-提现地址黑名单-编辑 

- 接口声明：`PATCH /address-blacklist`
- 输入字段：`id`, `chain`, `address`, `memo`, `remark`, `limit_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:803` · `WithdrawalAddressBlacklistResource`

### ASSETS-143 · 风控-风控参数配置-提现地址黑名单-删除 

- 接口声明：`DELETE /address-blacklist`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:838` · `WithdrawalAddressBlacklistResource`

### ASSETS-144 · 风控-风控参数配置-提现地址黑名单-批量上传 

- 接口声明：`POST /address-blacklist/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request('withdrawal_address_blacklist_create')
- 代码依据：`app/api/admin/asset/withdrawals.py:865` · `BatchUploadWithdrawalAddressBlacklistResource`

### ASSETS-145 · 钱包-WEB钱包管理-提现取消记录列表

- 接口声明：`GET /cancels`
- 输入字段：`id`, `asset`, `chain`, `type`, `user`, `cancel_type`, `cancel_user`, `address`, `start`, `end`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:1005` · `WithdrawalCancelsResource`

### ASSETS-146 · 风控-反洗钱系统-提现审核列表

- 接口声明：`GET /audits`
- 输入字段：`withdrawal_id`, `user_id`, `chain`, `asset`, `review_status`, `material_status`, `auditor_id`, `risk_level`, `type`, `start_time`, `end_time`, `audit_start_time`, `audit_end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:1183` · `WithdrawalAuditResource`

### ASSETS-147 · 风控-反洗钱系统-提现审核-备注

- 接口声明：`PATCH /audits`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:1356` · `WithdrawalAuditResource`

### ASSETS-148 · 提现审核-批量分配审核人

- 接口声明：`POST /audits/auditors`
- 输入字段：`auditor_ids`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:1394` · `WithdrawalAuditAssignAuditorsResource`

### ASSETS-149 · 提现审核-批量取消分配

- 接口声明：`PATCH /audits/auditors`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:1423` · `WithdrawalAuditAssignAuditorsResource`

### ASSETS-150 · 风控-反洗钱系统-提现审核详情

- 接口声明：`GET /audit/detail`
- 输入字段：`audit_id`, `edd_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:1479` · `WithdrawalAuditDetailResource`

### ASSETS-151 · 风控-反洗钱系统-提现审核流转

- 接口声明：`PUT /audit/detail`
- 输入字段：`audit_id`, `edd_id`, `action`, `reject_reason`, `is_custom_reason`, `custom_reject_reason`, `module_codes`, `reason_codes`, `custom_reason`, `cancel_reason`, `is_custom_cancel_reason`, `custom_cancel_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:1594` · `WithdrawalAuditDetailResource`

### ASSETS-152 · 风控-反洗钱系统-提现 EDD 列表

- 接口声明：`GET /edd-audit`
- 输入字段：`edd_id`, `withdrawal_id`, `user_id`, `chain`, `asset`, `review_status`, `material_status`, `type`, `start_time`, `end_time`, `audit_start_time`, `audit_end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:2024` · `WithdrawalEDDAuditResource`

### ASSETS-153 · 风控-用户风控审核-提现 EDD 备注

- 接口声明：`PATCH /edd-audit`
- 输入字段：`edd_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:2149` · `WithdrawalEDDAuditResource`

### ASSETS-154 · 风控-反洗钱系统-提现 EDD 详情

- 接口声明：`GET /edd-audit/detail`
- 输入字段：`edd_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawals.py:2176` · `WithdrawalEDDAuditDetailResource`

### ASSETS-155 · 触达管理-币种维护-列表

- 接口声明：`GET `
- 输入字段：`asset`, `platform`, `maintain_type`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:166` · `AssetMaintainResource`

### ASSETS-156 · 运营-币种维护-新增

- 接口声明：`POST `
- 输入字段：`assets`, `platform`, `started_at`, `ended_at`, `jump_page_enabled`, `jump_type`, `jump_id`, `maintain_type`, `tag_pages`, `tip_pages`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:259` · `AssetMaintainResource`

### ASSETS-157 · 运营-币种维护-详情

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:329` · `AssetMaintainDetailResource`

### ASSETS-158 · 运营-币种维护-编辑

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`asset`, `platform`, `started_at`, `ended_at`, `jump_page_enabled`, `jump_type`, `jump_id`, `maintain_type`, `tag_pages`, `tip_pages`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:395` · `AssetMaintainDetailResource`

### ASSETS-159 · 运营-币种维护-删除

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:453` · `AssetMaintainDetailResource`

### ASSETS-160 · 运营-币种维护-编辑内容

- 接口声明：`PUT /<int:id_>/langs/<lang>`
- 输入字段：`content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:477` · `AssetMaintainContentResource`

### ASSETS-161 · 运营-币种维护-批量应用模板

- 接口声明：`POST /batch-asset-maintain-content`
- 输入字段：`ids`, `template_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:528` · `BatchAssetMaintainContentResource`

### ASSETS-162 · 运营-触达管理-币种维护-提交审核

- 接口声明：`PATCH /<int:id_>/created`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:603` · `AssetMaintainCreated`

### ASSETS-163 · 运营-触达管理-币种维护-审核

- 接口声明：`PATCH /<int:id_>/audit`
- 输入字段：`status`, `auditor_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:638` · `AssetMaintainAudit`

### ASSETS-164 · 运营-触达管理-币种维护-下架

- 接口声明：`PATCH /<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/asset_maintain.py:694` · `AssetMaintainOfflineResource`

### ASSETS-165 · 运营-coinex_wallet-运营位管理-列表

- 接口声明：`GET /traffic/list`
- 输入字段：`show_page`, `display_status`, `name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/coinex_wallet.py:114` · `TrafficListResource`

### ASSETS-166 · 运营-coinex_wallet-运营位管理-创建

- 接口声明：`POST /traffic/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/coinex_wallet.py:145` · `TrafficListResource`

### ASSETS-167 · 运营-coinex_wallet-运营位管理-详情

- 接口声明：`GET /traffic/<string:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/coinex_wallet.py:170` · `TrafficResource`

### ASSETS-168 · 运营-coinex_wallet-运营位管理-编辑

- 接口声明：`PUT /traffic/<string:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/coinex_wallet.py:182` · `TrafficResource`

### ASSETS-169 · 运营-coinex_wallet-运营位管理-上/下架

- 接口声明：`PATCH /traffic/<string:id_>`
- 输入字段：`display_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/coinex_wallet.py:202` · `TrafficResource`

### ASSETS-170 · 报表-资产报表

- 接口声明：`GET `
- 输入字段：`start_date`, `end_date`, `account_type`, `asset`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/balance.py:55` · `UserBalanceResource`

### ASSETS-171 · 报表-资产报表-异步下载

- 接口声明：`GET /async-download`
- 输入字段：`start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/balance.py:175` · `UserBalanceAsyncDownloadResource`

### ASSETS-172 · 报表-资产报表-业务转化报表

- 接口声明：`GET /business`
- 输入字段：`report_type`, `asset`, `order_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/balance.py:272` · `AssetBusinessTransitionReportResource`

### ASSETS-173 · 报表-资产报表-用户关注报表

- 接口声明：`GET /visit`
- 输入字段：`report_type`, `user_type`, `lang`, `duration`, `asset`, `order_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/balance.py:437` · `AssetUserVisitReportResource`

### ASSETS-174 · 报表-资产报表-用户关注报表-异步下载

- 接口声明：`GET /visit-async-download`
- 输入字段：`report_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/balance.py:530` · `AssetUserVisitReportAsyncDownloadResource`

### ASSETS-175 · 报表-资产报表-币种曝光报表

- 接口声明：`GET /exposure`
- 输入字段：`user_type`, `lang`, `duration`, `asset`, `order_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/balance.py:571` · `AssetUserExposureReportResource`

### ASSETS-176 · 报表-资产报表-币种曝光报表-异步下载

- 接口声明：`GET /exposure-async-download`
- 输入字段：`start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/balance.py:632` · `AssetUserExposureReportAsyncDownloadResource`

### ASSETS-177 · 统计-资产统计-资金充足率统计

- 接口声明：`GET `
- 输入字段：`asset`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/asset_adequacy.py:39` · `AssetAdequacyResource`

### ASSETS-178 · 统计-资产统计-市场数据综合统计

- 接口声明：`GET /synthetic`
- 输入字段：`tab`, `name`, `time_type`, `trading_area`, `is_margin`, `is_perpetual`, `is_amm`, `export`, `sort_name`, `sort_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:40` · `SyntheticResource`

### ASSETS-179 · 统计-资产统计-市场数据综合统计-统计曲线

- 接口声明：`GET /synthetic-series`
- 输入字段：`tab`, `name`, `time_type`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:392` · `SyntheticSeriesResource`

### ASSETS-180 · 统计-资产统计-Investment持仓统计-AMM持仓统计

- 接口声明：`GET /sp-investment/amm`
- 输入字段：`asset`, `market`, `sort_by`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:508` · `SpInvestmentAMMStatsResource`

### ASSETS-181 · 统计-资产统计-Investment持仓统计-AMM持仓统计-AMM市场详情表

- 接口声明：`GET /sp-investment/amm/market`
- 输入字段：`market`, `sort_by`, `sort_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:668` · `SpInvestmentAMMMarketStatsResource`

### ASSETS-182 · 统计-资产统计-Investment持仓统计-AMM持仓统计-修改AMM市场备注

- 接口声明：`POST /sp-investment/amm/remark`
- 输入字段：`market`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:750` · `SpInvestmentAMMRemarkResource`

### ASSETS-183 · 统计-资产统计-Investment持仓统计-现货持仓统计

- 接口声明：`GET /sp-investment/spot`
- 输入字段：`asset`, `sort_by`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:813` · `SpInvestmentSpotStatsResource`

### ASSETS-184 · 统计-资产统计-Investment持仓统计-现货持仓统计-设置购买均价

- 接口声明：`POST /sp-investment/spot/<int:id_>`
- 输入字段：`avg_price`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:922` · `SpInvestmentSpotStatsDetailResource`

### ASSETS-185 · 统计-资产统计-Investment持仓统计-现货持仓统计-币种详情表

- 接口声明：`GET /sp-investment/spot/asset`
- 输入字段：`asset`, `start_date`, `end_date`, `sort_by`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:965` · `SpInvestmentSpotAssetStatsResource`

### ASSETS-186 · 统计-资产统计-Investment持仓统计-现货持仓统计-修改备注

- 接口声明：`POST /sp-investment/spot/remark`
- 输入字段：`asset`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance.py:1042` · `SpInvestmentSpotRemarkResource`

### ASSETS-187 · 统计-资产排名

- 接口声明：`GET `
- 输入字段：`account_balance_type`, `asset`, `search_keyword`, `date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance_rank.py:37` · `UserBalanceRankResource`

### ASSETS-188 · 统计-资产排名-币种资产全量导出

- 接口声明：`GET /export`
- 输入字段：`asset`, `date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/balance_rank.py:179` · `UserBalanceRankExportResource`

### ASSETS-189 · 统计-资产统计-量化站外资产统计列表

- 接口声明：`GET `
- 输入字段：`asset`, `is_alert_enabled`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:59` · `QuantificationExternalAssetResource`

### ASSETS-190 · 统计-资产统计-量化站外资产占比阈值-档位列表

- 接口声明：`GET /threshold-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:222` · `QuantificationExternalAssetThresholdConfResource`

### ASSETS-191 · 统计-资产统计-量化站外资产占比阈值-档位配置

- 接口声明：`POST /threshold-conf`
- 输入字段：`tiers`, `removes`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:248` · `QuantificationExternalAssetThresholdConfResource`

### ASSETS-192 · 统计-资产统计-量化站外资产占比阈值-档位详情配置

- 接口声明：`PUT /threshold-conf/<int:id_>`
- 输入字段：`market_alert_threshold`, `ratio_alert_threshold`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:325` · `QuantificationExternalAssetThresholdDetailConfResource`

### ASSETS-193 · 统计-资产统计-量化站外资产占比阈值-特殊币种配置列表

- 接口声明：`GET /special-threshold-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:360` · `QuantificationExternalAssetSpecialThresholdConfResource`

### ASSETS-194 · 统计-资产统计-量化站外资产占比阈值-特殊币种详情配置

- 接口声明：`PUT /special-threshold-conf/<int:id_>`
- 输入字段：`asset`, `market_alert_threshold`, `ratio_alert_threshold`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:385` · `QuantificationExternalAssetSpecialThresholdDetailConfResource`

### ASSETS-195 · 统计-资产统计-量化站外资产占比阈值-特殊币种配置-关闭

- 接口声明：`PATCH /special-threshold-conf/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:434` · `QuantificationExternalAssetSpecialThresholdDetailConfResource`

### ASSETS-196 · 统计-资产统计-量化站外资产监控配置-开关更新

- 接口声明：`PUT /monitor-conf`
- 输入字段：`asset`, `is_alert_enabled`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/quantification_external_asset.py:458` · `QuantificationExternalAssetMonitorConfResource`

### ASSETS-197 · 统计-资产负债

- 接口声明：`GET `
- 输入字段：`asset`, `min_usd`, `page`, `start_time`, `end_time`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/system_asset_liability.py:47` · `SystemAssetLiabilityResource`

### ASSETS-198 · 统计-资产负债-修改备注 

- 接口声明：`PUT `
- 输入字段：`id_`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/system_asset_liability.py:147` · `SystemAssetLiabilityResource`

### ASSETS-199 · 统计-资产负债-重新对账

- 接口声明：`PATCH `
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/system_asset_liability.py:171` · `SystemAssetLiabilityResource`

### ASSETS-200 · 异常充值申请-配置信息 

- 接口声明：`GET /application/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/abnormal_deposit.py:43` · `AbnormalDepositApplicationConfigResource`

### ASSETS-201 · 异常充值申请-提交 

- 接口声明：`POST /application`
- 输入字段：`asset`, `chain`, `address`, `amount`, `tx_id`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/abnormal_deposit.py:183` · `AbnormalDepositApplicationResource`

### ASSETS-202 · 异常充值申请-列表 

- 接口声明：`GET /application`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/abnormal_deposit.py:343` · `AbnormalDepositApplicationResource`

### ASSETS-203 · 异常充值申请-处理中的数目 

- 接口声明：`GET /application/processing/total`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/abnormal_deposit.py:378` · `AbnormalDepositApplicationProcTotalResource`

### ASSETS-204 · 异常充值申请-详情 

- 接口声明：`GET /application/<int:application_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/abnormal_deposit.py:410` · `AbnormalDepositApplicationDetailResource`

### ASSETS-205 · 异常充值申请-提交补充资料 

- 接口声明：`PUT /application/<int:application_id>`
- 输入字段：`transfer_out_screenshots`, `send_address_screenshots`, `merge_screenshots`, `refund_address_screenshots`, `refund_address`, `refund_memo`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/abnormal_deposit.py:467` · `AbnormalDepositApplicationDetailResource`

### ASSETS-206 · 异常充值申请-提交额外补充资料 

- 接口声明：`PATCH /application/<int:application_id>`
- 输入字段：`append_screenshots`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/abnormal_deposit.py:582` · `AbnormalDepositApplicationDetailResource`

### ASSETS-207 · 异常充值申请-取消申请 

- 接口声明：`DELETE /application/<int:application_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/abnormal_deposit.py:642` · `AbnormalDepositApplicationDetailResource`

### ASSETS-208 · AssetsResource.get（用途待确认）

- 接口声明：`GET /assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:134` · `AssetsResource`

### ASSETS-209 · 获取充提币种受限列表

- 接口声明：`GET /assets/restricted`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:163` · `RestrictedAssetsResource`

### ASSETS-210 · AssetConfigsResource.get（用途待确认）

- 接口声明：`GET /asset/configs`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:176` · `AssetConfigsResource`

### ASSETS-211 · 用于添加提现地址时获取地址配置

- 接口声明：`GET /address/config`
- 输入字段：`chain`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:205` · `AddressConfigResource`

### ASSETS-212 · WalletFeeResource.get（用途待确认）

- 接口声明：`GET /fee`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:227` · `WalletFeeResource`

### ASSETS-213 · 用于提现时判断是不是合约地址及CoinEx地址

- 接口声明：`POST /address/validation`
- 输入字段：`chain`, `address`, `memo`, `extra`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:291` · `AddressValidationResource`

### ASSETS-214 · 用于提现时判断是否重复提交过

- 接口声明：`POST /address/withdrawal/validation`
- 输入字段：`chain`, `address`, `asset`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:344` · `AddressWithdrawalValidationResource`

### ASSETS-215 · DepositsResource.get（用途待确认）

- 接口声明：`GET /deposits`
- 输入字段：`asset`, `type`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:396` · `DepositsResource`

### ASSETS-216 · DepositResource.get（用途待确认）

- 接口声明：`GET /deposit/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:610` · `DepositResource`

### ASSETS-217 · 获取充值退回确认页详情，包括退回类型、原路地址和当前版本。

- 接口声明：`GET /deposit/<int:id_>/refund`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:673` · `DepositRefundDetailResource`

### ASSETS-218 · 用户通过 2FA 确认退回信息，并将退回流程推进到退回待审核。

- 接口声明：`PUT /deposit/<int:id_>/refund`
- 输入字段：`refund_address`, `refund_memo`, `version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:692` · `DepositRefundDetailResource`

### ASSETS-219 · WithdrawalsPreScreeningResource.post（用途待确认）

- 接口声明：`POST /withdrawals/pre-screening`
- 输入字段：`type`, `asset`, `chain`, `address`, `memo`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:717` · `WithdrawalsPreScreeningResource`

### ASSETS-220 · WithdrawalsPreScreeningResource.patch（用途待确认）

- 接口声明：`PATCH /withdrawals/pre-screening`
- 输入字段：`id`, `agreed`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:744` · `WithdrawalsPreScreeningResource`

### ASSETS-221 · WithdrawalsResource.get（用途待确认）

- 接口声明：`GET /withdrawals`
- 输入字段：`asset`, `type`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:778` · `WithdrawalsResource`

### ASSETS-222 · WithdrawalsResource.post（用途待确认）

- 接口声明：`POST /withdrawals`
- 输入字段：`type`, `asset`, `chain`, `address`, `memo`, `amount`, `extra`, `remark`, `withdraw_password`, `fee_asset`, `screen_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:821` · `WithdrawalsResource`

### ASSETS-223 · WithdrawalResource.get（用途待确认）

- 接口声明：`GET /withdrawal/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1064` · `WithdrawalResource`

### ASSETS-224 · WithdrawalResource.put（用途待确认）

- 接口声明：`PUT /withdrawal/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1078` · `WithdrawalResource`

### ASSETS-225 · WithdrawalResource.delete（用途待确认）

- 接口声明：`DELETE /withdrawal/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1095` · `WithdrawalResource`

### ASSETS-226 · WithdrawalConfirmationResource.get（用途待确认）

- 接口声明：`GET /withdrawal/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1106` · `WithdrawalConfirmationResource`

### ASSETS-227 · WithdrawalConfirmationResource.post（用途待确认）

- 接口声明：`POST /withdrawal/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1154` · `WithdrawalConfirmationResource`

### ASSETS-228 · WithdrawalConfirmationResource.delete（用途待确认）

- 接口声明：`DELETE /withdrawal/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1258` · `WithdrawalConfirmationResource`

### ASSETS-229 · WithdrawableAmountResource.get（用途待确认）

- 接口声明：`GET /withdrawal/amount`
- 输入字段：`asset`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1298` · `WithdrawableAmountResource`

### ASSETS-230 · WithdrawalLimitResource.get（用途待确认）

- 接口声明：`GET /withdrawal/limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1318` · `WithdrawalLimitResource`

### ASSETS-231 · 自定义提现手续费-可选币种列表 

- 接口声明：`GET /withdrawal/fee/custom-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1330` · `WithdrawalCustomFeeAssetsResource`

### ASSETS-232 · 自定义提现手续费币种-手续费数目 

- 接口声明：`GET /withdrawal/fee/custom-amounts`
- 输入字段：`asset`, `fee_asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1342` · `WithdrawalCustomFeeAmountsResource`

### ASSETS-233 · DepositAddressesResource.get（用途待确认）

- 接口声明：`GET /deposit/addresses`
- 输入字段：`asset`, `chain`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1363` · `DepositAddressesResource`

### ASSETS-234 · DepositAddressResource.get（用途待确认）

- 接口声明：`GET /deposit/address`
- 输入字段：`asset`, `chain`
- 显式控制：require_login(allow_sub_account=False); lock_request('deposit_address_renewal', with_user=True)
- 代码依据：`app/api/frontend/wallet.py:1395` · `DepositAddressResource`

### ASSETS-235 · 充值-使用新地址 

- 接口声明：`PUT /deposit/address`
- 输入字段：`asset`, `chain`
- 显式控制：require_login(allow_sub_account=False); lock_request('deposit_address_renewal', with_user=True)
- 代码依据：`app/api/frontend/wallet.py:1422` · `DepositAddressResource`

### ASSETS-236 · WithdrawalAddressesResource.get（用途待确认）

- 接口声明：`GET /withdrawal/addresses`
- 输入字段：`asset`, `chain`, `type`, `search_key`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1454` · `WithdrawalAddressesResource`

### ASSETS-237 · WithdrawalAddressesResource.post（用途待确认）

- 接口声明：`POST /withdrawal/addresses`
- 输入字段：`asset`, `chain`, `address`, `memo`, `extra`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1497` · `WithdrawalAddressesResource`

### ASSETS-238 · WithdrawalAddressesResource.delete（用途待确认）

- 接口声明：`DELETE /withdrawal/addresses`
- 输入字段：`ids`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1560` · `WithdrawalAddressesResource`

### ASSETS-239 · WithdrawalAddressesBatchCheckResource.post（用途待确认）

- 接口声明：`POST /withdrawal/addresses/batch/check`
- 输入字段：`items`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1614` · `WithdrawalAddressesBatchCheckResource`

### ASSETS-240 · WithdrawalAddressesBatchResource.post（用途待确认）

- 接口声明：`POST /withdrawal/addresses/batch`
- 输入字段：`items`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1670` · `WithdrawalAddressesBatchResource`

### ASSETS-241 · 该接口类似获取充值地址列表，但不分页

- 接口声明：`GET /withdrawal/address/book`
- 输入字段：`asset`, `chain`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1744` · `WithdrawalAddressBookResource`

### ASSETS-242 · WithdrawalAddressResource.put（用途待确认）

- 接口声明：`PUT /withdrawal/address/<int:id_>`
- 输入字段：`remark`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1779` · `WithdrawalAddressResource`

### ASSETS-243 · LocalWithdrawalAddressesResource.get（用途待确认）

- 接口声明：`GET /local/withdrawal/addresses`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1805` · `LocalWithdrawalAddressesResource`

### ASSETS-244 · LocalWithdrawalAddressesResource.post（用途待确认）

- 接口声明：`POST /local/withdrawal/addresses`
- 输入字段：`address`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1814` · `LocalWithdrawalAddressesResource`

### ASSETS-245 · LocalWithdrawalAddressesResource.delete（用途待确认）

- 接口声明：`DELETE /local/withdrawal/addresses`
- 输入字段：`ids`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1857` · `LocalWithdrawalAddressesResource`

### ASSETS-246 · LocalWithdrawalAddressesBatchCheckResource.post（用途待确认）

- 接口声明：`POST /local/withdrawal/addresses/batch/check`
- 输入字段：`items`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:1892` · `LocalWithdrawalAddressesBatchCheckResource`

### ASSETS-247 · LocalWithdrawalAddressesBatchResource.post（用途待确认）

- 接口声明：`POST /local/withdrawal/addresses/batch`
- 输入字段：`items`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:1943` · `LocalWithdrawalAddressesBatchResource`

### ASSETS-248 · LocalWithdrawalAddressResource.put（用途待确认）

- 接口声明：`PUT /local/withdrawal/address/<int:id_>`
- 输入字段：`remark`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2010` · `LocalWithdrawalAddressResource`

### ASSETS-249 · 由提现记录快捷添加提现地址簿

- 接口声明：`POST /withdrawal/address/quickly`
- 输入字段：`withdrawal_id`, `type`, `remark`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2035` · `WithdrawalAddressQuickly`

### ASSETS-250 · ApiWithdrawalAddressesCheckResource.post（用途待确认）

- 接口声明：`POST /api/withdrawal/addresses/check`
- 输入字段：`type`, `items`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2132` · `ApiWithdrawalAddressesCheckResource`

### ASSETS-251 · ApiWithdrawalAddressesCheckResource.put（用途待确认）

- 接口声明：`PUT /api/withdrawal/addresses/check`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2146` · `ApiWithdrawalAddressesCheckResource`

### ASSETS-252 · ApiWithdrawalAddressesResource.get（用途待确认）

- 接口声明：`GET /api/withdrawal/addresses`
- 输入字段：`asset`, `chain`, `kind`, `type`, `search_key`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2353` · `ApiWithdrawalAddressesResource`

### ASSETS-253 · ApiWithdrawalAddressesResource.post（用途待确认）

- 接口声明：`POST /api/withdrawal/addresses`
- 输入字段：`type`, `asset`, `chain`, `address`, `memo`, `extra`, `remark`, `withdraw_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2401` · `ApiWithdrawalAddressesResource`

### ASSETS-254 · ApiWithdrawalAddressesResource.delete（用途待确认）

- 接口声明：`DELETE /api/withdrawal/addresses`
- 输入字段：`ids`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2475` · `ApiWithdrawalAddressesResource`

### ASSETS-255 · ApiWithdrawalAddressesResource.put（用途待确认）

- 接口声明：`PUT /api/withdrawal/addresses`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2537` · `ApiWithdrawalAddressesResource`

### ASSETS-256 · ApiWithdrawalAddressesBatchResource.post（用途待确认）

- 接口声明：`POST /api/withdrawal/addresses/batch`
- 输入字段：`type`, `items`, `withdraw_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2596` · `ApiWithdrawalAddressesBatchResource`

### ASSETS-257 · ApiWithdrawalAddressRequestsResource.get（用途待确认）

- 接口声明：`GET /api/withdrawal/address/requests`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2622` · `ApiWithdrawalAddressRequestsResource`

### ASSETS-258 · ApiWithdrawalAddressRequestResource.get（用途待确认）

- 接口声明：`GET /api/withdrawal/address/request/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2641` · `ApiWithdrawalAddressRequestResource`

### ASSETS-259 · ApiWithdrawalAddressRequestResource.put（用途待确认）

- 接口声明：`PUT /api/withdrawal/address/request/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2665` · `ApiWithdrawalAddressRequestResource`

### ASSETS-260 · ApiWithdrawalAddressConfirmationResource.get（用途待确认）

- 接口声明：`GET /api/withdrawal/address/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2701` · `ApiWithdrawalAddressConfirmationResource`

### ASSETS-261 · ApiWithdrawalAddressConfirmationResource.post（用途待确认）

- 接口声明：`POST /api/withdrawal/address/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2729` · `ApiWithdrawalAddressConfirmationResource`

### ASSETS-262 · ApiWithdrawalAddressConfirmationResource.delete（用途待确认）

- 接口声明：`DELETE /api/withdrawal/address/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2794` · `ApiWithdrawalAddressConfirmationResource`

### ASSETS-263 · WithdrawalApproversResource.get（用途待确认）

- 接口声明：`GET /withdrawal/approvers`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2829` · `WithdrawalApproversResource`

### ASSETS-264 · WithdrawalApproversResource.post（用途待确认）

- 接口声明：`POST /withdrawal/approvers`
- 输入字段：`approvers`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2854` · `WithdrawalApproversResource`

### ASSETS-265 · WithdrawalApproverResource.put（用途待确认）

- 接口声明：`PUT /withdrawal/approver/<int:id_>`
- 输入字段：`name`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2919` · `WithdrawalApproverResource`

### ASSETS-266 · WithdrawalApproverResource.delete（用途待确认）

- 接口声明：`DELETE /withdrawal/approver/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:2951` · `WithdrawalApproverResource`

### ASSETS-267 · WithdrawalApproverConfirmationResource.get（用途待确认）

- 接口声明：`GET /withdrawal/approver/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:2985` · `WithdrawalApproverConfirmationResource`

### ASSETS-268 · 确认添加审核人

- 接口声明：`POST /withdrawal/approver/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3003` · `WithdrawalApproverConfirmationResource`

### ASSETS-269 · 重发确认邮件

- 接口声明：`PUT /withdrawal/approver/confirmation`
- 输入字段：`request_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3056` · `WithdrawalApproverConfirmationResource`

### ASSETS-270 · 撤销添加审核人

- 接口声明：`DELETE /withdrawal/approver/confirmation`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3071` · `WithdrawalApproverConfirmationResource`

### ASSETS-271 · WithdrawalApproverJoinResource.get（用途待确认）

- 接口声明：`GET /withdrawal/approver/join`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3095` · `WithdrawalApproverJoinResource`

### ASSETS-272 · 加入提现审核人

- 接口声明：`POST /withdrawal/approver/join`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3112` · `WithdrawalApproverJoinResource`

### ASSETS-273 · 拒绝加入提现审核人

- 接口声明：`DELETE /withdrawal/approver/join`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3143` · `WithdrawalApproverJoinResource`

### ASSETS-274 · WithdrawalApproverLeaveResource.get（用途待确认）

- 接口声明：`GET /withdrawal/approver/leave`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3169` · `WithdrawalApproverLeaveResource`

### ASSETS-275 · 确认退出提现审核人

- 接口声明：`POST /withdrawal/approver/leave`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3186` · `WithdrawalApproverLeaveResource`

### ASSETS-276 · WalletBroadcastResource.get（用途待确认）

- 接口声明：`GET /broadcast`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3221` · `WalletBroadcastResource`

### ASSETS-277 · KYTProofResource.get（用途待确认）

- 接口声明：`GET /kyt/proof`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3245` · `KYTProofResource`

### ASSETS-278 · KYTProofResource.put（用途待确认）

- 接口声明：`PUT /kyt/proof`
- 输入字段：`token`, `files`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/wallet.py:3269` · `KYTProofResource`

### ASSETS-279 · EDDProofResource.get（用途待确认）

- 接口声明：`GET /edd/proof`
- 输入字段：`id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3354` · `EDDProofResource`

### ASSETS-280 · EDDProofResource.put（用途待确认）

- 接口声明：`PUT /edd/proof`
- 输入字段：`id`, `module_payload`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3396` · `EDDProofResource`

### ASSETS-281 · 提现-获取EDD信息

- 接口声明：`GET /withdrawal/edd/proof`
- 输入字段：`id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3523` · `WithdrawalEDDProofResource`

### ASSETS-282 · 提现-提交EDD资料

- 接口声明：`PUT /withdrawal/edd/proof`
- 输入字段：`id`, `module_payload`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3576` · `WithdrawalEDDProofResource`

### ASSETS-283 · 获取账户被盗解除提交页面信息

- 接口声明：`GET /account-theft/unlock`
- 输入字段：`id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3755` · `AccountTheftUnlockResource`

### ASSETS-284 · 提交账户被盗解除验证资料

- 接口声明：`PUT /account-theft/unlock`
- 输入字段：`files`, `id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/wallet.py:3799` · `AccountTheftUnlockResource`

### ASSETS-285 · CreditAssetsResource.get（用途待确认）

- 接口声明：`GET /credit/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:58` · `CreditAssetsResource`

### ASSETS-286 · CreditUserAssetsResource.get（用途待确认）

- 接口声明：`GET /credit/user/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:101` · `CreditUserAssetsResource`

### ASSETS-287 · DepositsResource.post（用途待确认）

- 接口声明：`POST /deposits, /deposits/<int:id_>`
- 输入字段：`id`, `user_id`, `type`, `asset`, `chain`, `address`, `memo`, `amount`, `tx_id`, `vout`, `confirmations`, `status`, `signature`, `senders`, `attachment`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:138` · `DepositsResource`

### ASSETS-288 · DepositsResource.patch（用途待确认）

- 接口声明：`PATCH /deposits, /deposits/<int:id_>`
- 输入字段：`confirmations`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:169` · `DepositsResource`

### ASSETS-289 · 钱包完成充值退回后的结果回调。

- 接口声明：`PUT /deposits/<int:wallet_deposit_id>/refund`
- 输入字段：`id`, `status`, `amount`, `tx_id`, `sent_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:196` · `DepositRefundCallbackResource`

### ASSETS-290 · 用于钱包组手动修正充值记录，目前只有已取消的提现修正为处理中这一个场景

- 接口声明：`POST /deposit/fix`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:213` · `DepositFixResource`

### ASSETS-291 · PoolWalletHistory.get（用途待确认）

- 接口声明：`GET /history/pool`
- 输入字段：`last_id`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:233` · `PoolWalletHistory`

### ASSETS-292 · SystemAssetLiabilityResource.get（用途待确认）

- 接口声明：`GET /assets/liability`
- 输入字段：`assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:271` · `SystemAssetLiabilityResource`

### ASSETS-293 · WithdrawalResource.get（用途待确认）

- 接口声明：`GET /withdrawal`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:294` · `WithdrawalResource`

### ASSETS-294 · WithdrawalFeeResource.get（用途待确认）

- 接口声明：`GET /withdrawal/fee`
- 输入字段：`assets`, `start`, `end`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:318` · `WithdrawalFeeResource`

### ASSETS-295 · AssetStatisticPriceResource.get（用途待确认）

- 接口声明：`GET /assets/statistic/price`
- 输入字段：`search_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:361` · `AssetStatisticPriceResource`

### ASSETS-296 · LogAbnormalIssuanceResource.post（用途待确认）

- 接口声明：`POST /log/abnormal-issuance`
- 输入字段：`asset`, `chain`, `cur_issue_amount`, `his_issue_amount`, `create_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:378` · `LogAbnormalIssuanceResource`

### ASSETS-297 · SettingsResource.get（用途待确认）

- 接口声明：`GET /settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:401` · `SettingsResource`

### ASSETS-298 · AssetSettingsResource.get（用途待确认）

- 接口声明：`GET /assets/<asset>/<chain>/settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:414` · `AssetSettingsResource`

### ASSETS-299 · SignPreResources.post（用途待确认）

- 接口声明：`POST /sign-pre`
- 输入字段：`group`, `chain`, `sender`, `message`, `commitment`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:426` · `SignPreResources`

### ASSETS-300 · SignResources.post（用途待确认）

- 接口声明：`POST /sign`
- 输入字段：`group`, `type`, `wwid`, `chain`, `sender`, `recipients`, `raw_data`, `signer`, `message`, `sign_func`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:442` · `SignResources`

### ASSETS-301 · WhitelistAddressResource.get（用途待确认）

- 接口声明：`GET /address/whitelist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:473` · `WhitelistAddressResource`

### ASSETS-302 · 用户充值检查用户是否需要强制kyt

- 接口声明：`GET /deposit/sender/kyt`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:485` · `DepositRiskCheckResources`

### ASSETS-303 · 提现待打币种数量 

- 接口声明：`GET /withdrawal/pending-amounts`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:498` · `AssetPendingWithdrawalAmountResources`

### ASSETS-304 · 通过钱包 id，并依据 KYT 来判断是否可以通知钱包侧转热钱包

- 接口声明：`POST /kyt/deposit/safe`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:520` · `KYTDepositSafeResources`

### ASSETS-305 · 通过钱包 (chain, tx_id) ，获取web自助找回记录状态

- 接口声明：`POST /abnormal-deposits/status`
- 输入字段：`data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:587` · `AbnormalDepositsResources`

### ASSETS-306 · WalletOnchainTxResource.post（用途待确认）

- 接口声明：`POST /onchain/tx`
- 输入字段：`request_id`, `tx_id`, `received_amount`, `status`, `confirmations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:671` · `WalletOnchainTxResource`

### ASSETS-307 · WithdrawalSmallAmountRiskEventSiteResource.post（用途待确认）

- 接口声明：`POST /risk/withdrawal/small-amount/site`
- 输入字段：`event_time`, `recent_withdrawal_value`, `average_withdrawal_value`, `withdrawal_threshold`, `threshold_multiple`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:697` · `WithdrawalSmallAmountRiskEventSiteResource`

### ASSETS-308 · WithdrawalSmallAmountRiskEventAssetResource.post（用途待确认）

- 接口声明：`POST /risk/withdrawal/small-amount/asset`
- 输入字段：`asset`, `event_time`, `recent_withdrawal_amount`, `wallet_amount`, `recent_withdrawal_value`, `withdrawal_threshold`, `threshold_multiple`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:725` · `WithdrawalSmallAmountRiskEventAssetResource`

### ASSETS-309 · SendDepositWithdrawalResumesEmail.post（用途待确认）

- 接口声明：`POST /send-deposit-withdraw-resume-email`
- 输入字段：`asset`, `chain`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/wallet.py:755` · `SendDepositWithdrawalResumesEmail`

### ASSETS-310 · AssetInformationResource.get（用途待确认）

- 接口声明：`GET /info`
- 输入字段：`ccy`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/assets/assets.py:67` · `AssetInformationResource`

### ASSETS-311 · AssetTransferResource.post（用途待确认）

- 接口声明：`POST /transfer`
- 输入字段：`from_account_type`, `to_account_type`, `ccy`, `market`, `amount`
- 显式控制：require_api_v2_auth(require_trading_permission=True)
- 代码依据：`app/api/v2/assets/assets.py:177` · `AssetTransferResource`

### ASSETS-312 · AssetTransferHistoryResource.get（用途待确认）

- 接口声明：`GET /transfer-history`
- 输入字段：`transfer_type`, `ccy`, `market`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/assets/assets.py:346` · `AssetTransferHistoryResource`

### ASSETS-313 · AssetConfigResource.get（用途待确认）

- 接口声明：`GET /deposit-withdraw-config`
- 输入字段：`ccy`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/assets/assets.py:377` · `AssetConfigResource`

### ASSETS-314 · AllAssetConfigResource.get（用途待确认）

- 接口声明：`GET /all-deposit-withdraw-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/assets/assets.py:404` · `AllAssetConfigResource`

### ASSETS-315 · DepositAddressResource.get（用途待确认）

- 接口声明：`GET /deposit-address`
- 输入字段：`ccy`, `chain`
- 显式控制：require_api_v2_auth(allow_sub_account=False); lock_request('deposit_address_renewal', with_user=True)
- 代码依据：`app/api/v2/assets/assets.py:437` · `DepositAddressResource`

### ASSETS-316 · 充值-使用新地址 

- 接口声明：`POST /renewal-deposit-address`
- 输入字段：`ccy`, `chain`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_trading_permission=True); lock_request('deposit_address_renewal', with_user=True)
- 代码依据：`app/api/v2/assets/assets.py:469` · `RenewDepositAddressResource`

### ASSETS-317 · DepositHistoryResource.get（用途待确认）

- 接口声明：`GET /deposit-history`
- 输入字段：`ccy`, `tx_id`, `type`, `status`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/assets/assets.py:500` · `DepositHistoryResource`

### ASSETS-318 · WithdrawalResource.get（用途待确认）

- 接口声明：`GET /withdraw`
- 输入字段：`ccy`, `withdraw_id`, `type`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/assets/assets.py:563` · `WithdrawalResource`

### ASSETS-319 · WithdrawalResource.post（用途待确认）

- 接口声明：`POST /withdraw`
- 输入字段：`ccy`, `chain`, `to_address`, `withdraw_method`, `memo`, `amount`, `fee_ccy`, `extra`, `remark`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_withdrawal_permission=True)
- 代码依据：`app/api/v2/assets/assets.py:627` · `WithdrawalResource`

### ASSETS-320 · CancelWithdrawResource.post（用途待确认）

- 接口声明：`POST /cancel-withdraw`
- 输入字段：`withdraw_id`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_withdrawal_permission=True)
- 代码依据：`app/api/v2/assets/assets.py:692` · `CancelWithdrawResource`

### ASSETS-321 · AssetRateResource.get（用途待确认）

- 接口声明：`GET /rate`
- 输入字段：`date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/assets/assets.py:706` · `AssetRateResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/admin/activity/test_deposit_bonus.py`
- `tests/api/admin/asset/test_audit_dual_status.py`
- `tests/api/admin/operation/test_asset_maintain.py`
- `tests/api/frontend/test_wallet.py`
- `tests/api/v2/test_assets.py`
- `tests/business/asset/test_new_asset.py`
- `tests/business/asset/test_sync_assets.py`
- `tests/business/clients/test_wallet.py`
- `tests/business/onchain/test_balance.py`
- `tests/business/report/test_asset_biz.py`
- `tests/business/test_wallet.py`
- `tests/business/test_wallet_withdrawable_amount.py`
- `tests/caches/test_deposit_popup_windows.py`
- `tests/consumer/test_kafka_balance_update.py`
- `tests/schedules/reports/test_deposit_withdrawal_kyt_usage.py`
- `tests/schedules/wallet/__init__.py`
- `tests/schedules/wallet/test_assets.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
