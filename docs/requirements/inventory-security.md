# 安全设置与风控 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### SECURITY-001 · 风控-羊毛党-黑名单列表

- 接口声明：`GET /risk-user`
- 输入字段：`user_id`, `start_at`, `end_at`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:40` · `AntiFraudRiskUserListResource`

### SECURITY-002 · 风控-羊毛党-增加黑名单

- 接口声明：`POST /risk-user`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:90` · `AntiFraudRiskUserListResource`

### SECURITY-003 · 风控-羊毛党-删除黑名单

- 接口声明：`DELETE /risk-user/<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:120` · `AntiFraudRiskUserDetailResource`

### SECURITY-004 · 风控-羊毛党-修改黑名单

- 接口声明：`PUT /risk-user/<int:user_id>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:132` · `AntiFraudRiskUserDetailResource`

### SECURITY-005 · 风控-羊毛党-下载黑名单模板

- 接口声明：`GET /risk-user/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:162` · `AntiFraudRiskUserTemplateResource`

### SECURITY-006 · 风控-羊毛党-批量导入黑名单

- 接口声明：`POST /risk-user/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:176` · `AntiFraudRiskUserImportResource`

### SECURITY-007 · 风控->反欺诈系统->特征列表

- 接口声明：`GET /feature`
- 输入字段：`feature_name`, `feature_type`, `identity_type`, `risk_model_name`, `page`, `limit`, `include_transformed`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:203` · `FeatureResource`

### SECURITY-008 · 风控->反欺诈系统->特征列表->修改特征描述

- 接口声明：`POST /feature`
- 输入字段：`feature_name`, `description`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:233` · `FeatureResource`

### SECURITY-009 · 风控->反欺诈系统->特征筛查->特征值分布 

- 接口声明：`GET /feature/distribution`
- 输入字段：`feature_name`, `start_time`, `end_time`, `value_path`, `identity`, `identity_type`, `bucket_count`, `top_n`, `max_docs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:255` · `FeatureDistributionResource`

### SECURITY-010 · 风控->反欺诈系统->特征值路径探测 

- 接口声明：`GET /feature/value-paths`
- 输入字段：`feature_name`, `start_time`, `end_time`, `identity`, `identity_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:276` · `FeatureValuePathsResource`

### SECURITY-011 · 风控->反欺诈系统->特征筛查->用户窗口已计算特征 

- 接口声明：`GET /feature/user/computed`
- 输入字段：`user_id`, `risk_model_name`, `cal_time`, `start_time`, `end_time`, `feature_names`, `transformed_feature_names`, `include_sources`, `scope`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:293` · `UserComputedFeatureResource`

### SECURITY-012 · 风控->反欺诈系统->特征筛查->转换后特征批量统计 

- 接口声明：`POST /feature/statistics`
- 输入字段：`user_ids`, `risk_model_name`, `cal_time`, `as_of_by_user`, `scope`, `transformed_feature_names`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:315` · `FeatureStatisticsResource`

### SECURITY-013 · 风控->反欺诈系统->特征筛查->特征校准（用户维度事实查询/差异对比） 

- 接口声明：`POST /feature/user/facts/query`
- 输入字段：`user_ids`, `risk_model_name`, `as_of_by_user`, `as_of_anchor`, `start_time_by_user`, `scopes`, `include_backend`, `include_local_raw_logs`, `include_current_features`, `include_relation_2y`, `sample_limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:333` · `UserFeatureFactsQueryResource`

### SECURITY-014 · 风控->反欺诈系统->特征筛查->as_of 锚点轻量解析 

- 接口声明：`POST /feature/user/facts/as-of/resolve`
- 输入字段：`user_ids`, `risk_model_name`, `as_of_by_user`, `as_of_anchor`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:357` · `UserFeatureFactsAsOfResolveResource`

### SECURITY-015 · 风控->反欺诈系统->特征筛查->特征回填（确认补充事实并定向重算） 

- 接口声明：`POST /feature/user/facts/supplement`
- 输入字段：`user_ids`, `risk_model_name`, `apply_items`, `as_of_by_user`, `as_of_anchor`, `reason`, `idempotency_key`, `feature_names`, `recalculate_features`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:373` · `UserFeatureFactsSupplementResource`

### SECURITY-016 · 风控->反欺诈系统->特征筛查->按 identity 批量补录 

- 接口声明：`POST /feature/identity/batch-supplement`
- 输入字段：`identity`, `identity_type`, `fact_type`, `as_of`, `window_days`, `risk_model_name`, `reason`, `dry_run`, `offset`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:409` · `FeatureIdentityBatchSupplementResource`

### SECURITY-017 · 风控->反欺诈系统->特征筛查->查询异步回填/补录任务列表 

- 接口声明：`GET /feature/supplement-jobs`
- 输入字段：`status`, `keyword`, `created_after`, `created_before`, `page`, `page_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:439` · `FeatureFactSupplementJobCollectionResource`

### SECURITY-018 · 风控->反欺诈系统->特征筛查->提交异步回填/补录任务 

- 接口声明：`POST /feature/supplement-jobs`
- 输入字段：`risk_model_name`, `apply_items`, `identity_items`, `as_of_by_user`, `as_of_anchor`, `reason`, `batch_name`, `idempotency_key`, `recalculate_features`, `identity_page_size`, `identity_concurrency`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:453` · `FeatureFactSupplementJobCollectionResource`

### SECURITY-019 · 风控->反欺诈系统->特征筛查->查询异步回填/补录任务 

- 接口声明：`GET /feature/supplement-jobs/<string:job_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:494` · `FeatureFactSupplementJobResource`

### SECURITY-020 · 风控->反欺诈系统->特征列表->特征配置列表

- 接口声明：`GET /feature/config`
- 输入字段：`feature_name`, `config_name`, `config_key`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:504` · `FeatureConfigResource`

### SECURITY-021 · 风控->反欺诈系统->特征列表->新增/修改特征配置

- 接口声明：`POST /feature/config`
- 输入字段：`feature_name`, `config_name`, `config_key`, `config_value`, `desc`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:576` · `FeatureConfigResource`

### SECURITY-022 · 风控->反欺诈系统->特征列表->删除特征配置

- 接口声明：`DELETE /feature/config`
- 输入字段：`feature_name`, `config_name`, `config_key`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:596` · `FeatureConfigResource`

### SECURITY-023 · 风控-羊毛党-批量导入特征配置模版

- 接口声明：`GET /feature/config/import`
- 输入字段：`feature_name`, `config_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:628` · `AntiFraudFeatureConfigImportResource`

### SECURITY-024 · 风控-羊毛党-批量导入特征配置

- 接口声明：`POST /feature/config/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:659` · `AntiFraudFeatureConfigImportResource`

### SECURITY-025 · 风控->反欺诈系统->特征列表->风险用户列表

- 接口声明：`GET /risk/user`
- 输入字段：`risk_model_name`, `cal_time`, `user_id`, `user_risk_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:731` · `RiskUserResource`

### SECURITY-026 · 风控->反欺诈系统->特征列表->修改风险用户描述

- 接口声明：`POST /risk/user`
- 输入字段：`risk_model_name`, `risk_user_id`, `description`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:816` · `RiskUserResource`

### SECURITY-027 · 风控->反欺诈系统->风险用户信息列表

- 接口声明：`GET /user-risk-info`
- 输入字段：`risk_model_name`, `start_time`, `end_time`, `user_id`, `manual_annotation`, `time_filter_field`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:866` · `UserRiskInfoResource`

### SECURITY-028 · 风控->反欺诈系统->人工标注

- 接口声明：`POST /user-risk-info`
- 输入字段：`risk_model_name`, `user_id`, `manual_annotation`, `manual_annotation_at`, `manual_annotation_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:932` · `UserRiskInfoResource`

### SECURITY-029 · 风控-羊毛党-下载导入标注模板

- 接口声明：`GET /user-risk-info/manual-annotation/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1144` · `UserRiskInfoManualAnnotationImportResource`

### SECURITY-030 · 风控->反欺诈系统->导入标注

- 接口声明：`POST /user-risk-info/manual-annotation/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1153` · `UserRiskInfoManualAnnotationImportResource`

### SECURITY-031 · 风控 - 反欺诈系统 - 页面小批量填写人工标注

- 接口声明：`POST /user-risk-info/manual-annotation/batch`
- 输入字段：`risk_model_name`, `user_ids`, `manual_annotation`, `manual_annotation_at`, `manual_annotation_reason`, `auto_complete_info`, `registration_offset_hours`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1392` · `UserRiskInfoManualAnnotationBatchResource`

### SECURITY-032 · 风控->反欺诈系统->导出风险用户信息

- 接口声明：`GET /user-risk-info/export`
- 输入字段：`risk_model_name`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1414` · `UserInfoRiskExportResource`

### SECURITY-033 · 风控->反欺诈系统-> 风险用户列表 -> 风险用户交叉对比指标

- 接口声明：`GET /user-risk-info/metrics`
- 输入字段：`risk_model_name`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1431` · `UserInfoRiskMetricsResource`

### SECURITY-034 · 风控->反欺诈系统->风险模型/风险类型选项

- 接口声明：`GET /risk/options`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1450` · `RiskOptionsResource`

### SECURITY-035 · 风控->反欺诈系统->风险模型列表

- 接口声明：`GET /risk/model/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1460` · `RiskModelListResource`

### SECURITY-036 · 风控->反欺诈系统->特征列表->修改风险模型描述

- 接口声明：`POST /risk/model`
- 输入字段：`risk_model_name`, `description`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1470` · `RiskModelResource`

### SECURITY-037 · 风控->反欺诈系统->模型管理->风险计算运行时配置

- 接口声明：`GET /risk-cal/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1490` · `RiskCalConfigResource`

### SECURITY-038 · 风控->反欺诈系统->模型管理->风险计算运行时配置->热更新

- 接口声明：`POST /risk-cal/config`
- 输入字段：`risk_model_concurrency`, `save_concurrency`, `batch_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1496` · `RiskCalConfigResource`

### SECURITY-039 · 风控->反欺诈系统->模型管理->风险模型计算进度

- 接口声明：`GET /risk-cal/progress`
- 输入字段：`risk_model_name`, `risk_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1528` · `RiskCalProgressResource`

### SECURITY-040 · 风控->反欺诈系统->模型管理->风险模型计算进度->向前跳游标

- 接口声明：`POST /risk-cal/progress`
- 输入字段：`risk_model_name`, `risk_type`, `next_cal_time`, `reason`, `dry_run`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1538` · `RiskCalProgressResource`

### SECURITY-041 · 风控->反欺诈系统->告警规则配置->列表

- 接口声明：`GET /risk-alert/rule`
- 输入字段：`risk_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1574` · `RiskAlertRuleResource`

### SECURITY-042 · 风控->反欺诈系统->告警规则配置->新增/修改

- 接口声明：`POST /risk-alert/rule`
- 输入字段：`risk_type`, `enabled`, `alert_mode`, `threshold`, `progressive_alert_enabled`, `progressive_increase_after_count`, `progressive_initial_interval_hours`, `progressive_max_interval_hours`, `hourly_alert_enabled`, `daily_alert_enabled`, `daily_send_limit`, `scheduled_hours`, `upload_risk_user_file`, `risk_user_file_ttl_days`, `desc`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1585` · `RiskAlertRuleResource`

### SECURITY-043 · 风控->反欺诈系统->告警规则配置->删除，恢复默认策略

- 接口声明：`DELETE /risk-alert/rule`
- 输入字段：`risk_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1616` · `RiskAlertRuleResource`

### SECURITY-044 · 风控->反欺诈系统->告警审核批次列表 

- 接口声明：`GET /risk-review/batch`
- 输入字段：`batch_id`, `risk_type`, `risk_model_name`, `alert_type`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1636` · `RiskReviewBatchResource`

### SECURITY-045 · 风控->反欺诈系统->告警审核批次指标 

- 接口声明：`GET /risk-review/batch/metrics`
- 输入字段：`batch_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1657` · `RiskReviewBatchMetricsResource`

### SECURITY-046 · 风控->反欺诈系统->告警审核批次上传风险用户

- 接口声明：`POST /risk-review/batch/upload-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:1673` · `RiskReviewBatchUploadUsersResource`

### SECURITY-047 · 风控->反欺诈系统->告警审核事件列表 

- 接口声明：`GET /risk-review/event`
- 输入字段：`batch_id`, `risk_type`, `risk_model_name`, `alert_type`, `review_status`, `manual_annotation`, `user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2012` · `RiskReviewEventResource`

### SECURITY-048 · 风控->反欺诈系统->提交告警审核事件 

- 接口声明：`POST /risk-review/event`
- 输入字段：`event_id`, `event_ids`, `batch_id`, `user_id`, `user_ids`, `manual_annotation`, `manual_annotation_at`, `manual_annotation_reason`, `auto_complete_info`, `manual_annotation_rule`, `manual_annotation_registration_offset_hours`, `registration_time`, `second_sms_send_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2038` · `RiskReviewEventResource`

### SECURITY-049 · 风控->反欺诈系统->模型管理->ML模型列表

- 接口声明：`GET /ml-model/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2088` · `MLModelListResource`

### SECURITY-050 · 风控->反欺诈系统->模型管理->ML模型信息

- 接口声明：`GET /ml-model/info`
- 输入字段：`model_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2098` · `MLModelInfoResource`

### SECURITY-051 · 风控->反欺诈系统->模型管理->重新加载ML模型

- 接口声明：`POST /ml-model/reload`
- 输入字段：`model_name`, `model_path`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2111` · `MLModelReloadResource`

### SECURITY-052 · 风控->反欺诈系统->模型管理->ML模型特征重要性

- 接口声明：`GET /ml-model/feature-importance`
- 输入字段：`model_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2132` · `MLModelFeatureImportanceResource`

### SECURITY-053 · 上传训练数据文件 风控->反欺诈系统->模型管理-> 数据管理 -> 上传训练数据

- 接口声明：`POST /ml-model/train-data/upload`
- 输入字段：`version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2147` · `MLModelTrainDataUploadResource`

### SECURITY-054 · 获取指定版本的训练数据信息

- 接口声明：`GET /ml-model/train-data`
- 输入字段：`version`, `action`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2196` · `MLModelTrainDataInfoResource`

### SECURITY-055 · 风控->反欺诈系统->模型管理-> 在线导出 -> 导出模型列表

- 接口声明：`GET /ml-model/train/export/models`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2214` · `MLModelTrainDataExportModelsResource`

### SECURITY-056 · 风控->反欺诈系统->模型管理-> 在线导出 -> 训练特征列表 

- 接口声明：`GET /ml-model/train/export/features`
- 输入字段：`model_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2226` · `MLModelTrainExportFeaturesResource`

### SECURITY-057 · 风控->反欺诈系统->模型管理-> 在线导出 -> 线上/导出特征组对比 

- 接口声明：`GET /ml-model/train/export/feature-comparison`
- 输入字段：`model_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2239` · `MLModelTrainExportFeatureComparisonResource`

### SECURITY-058 · 风控->反欺诈系统->模型管理-> 在线导出 -> 开始导出

- 接口声明：`POST /ml-model/train/export`
- 输入字段：`model_name`, `start_time`, `end_time`, `sample_base`, `user_ids`, `annotation_only`, `user_time_anchor`, `review_batch_id`, `review_event_ids`, `sampling_policy`, `sampling_config`, `plan_only`, `source_plan_task_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2256` · `MLModelTrianDataExportResource`

### SECURITY-059 · 风控->反欺诈系统->模型管理-> 在线导出 -> 查看任务

- 接口声明：`GET /ml-model/train/export`
- 输入字段：`task_id`, `action`, `limit`, `offset`, `review_batch_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2300` · `MLModelTrianDataExportResource`

### SECURITY-060 · 风控->反欺诈系统->模型管理-> 在线导出 -> 按名单补录事实

- 接口声明：`POST /ml-model/train/export/supplement-facts`
- 输入字段：`task_id`, `batch_size`, `max_concurrent_jobs`, `recalculate_features`, `reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2330` · `MLModelExportPlanSupplementResource`

### SECURITY-061 · 风控 -> 反欺诈系统 -> 模型管理 -> 上传历史训练数据重导

- 接口声明：`POST /ml-model/train/export/upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2360` · `MLModelTrainHistoricalDataExportResource`

### SECURITY-062 · 启动模型训练任务

- 接口声明：`POST /ml-model/train`
- 输入字段：`data_version`, `model_name`, `target_column`, `tune`, `tuning_method`, `n_trials`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2399` · `MLModelTrainResource`

### SECURITY-063 · 查询训练任务状态

- 接口声明：`GET /ml-model/train/status`
- 输入字段：`task_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2431` · `MLModelTrainStatusResource`

### SECURITY-064 · 获取训练任务列表

- 接口声明：`GET /ml-model/train/tasks`
- 输入字段：`status`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2446` · `MLModelTrainTasksResource`

### SECURITY-065 · 将模型提升到生产环境

- 接口声明：`POST /ml-model/promote`
- 输入字段：`model_name`, `version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2462` · `MLModelPromoteResource`

### SECURITY-066 · 风控->反欺诈系统->模型管理->上传模型

- 接口声明：`POST /ml-model/upload`
- 输入字段：`model_name`, `version`, `description`, `uploader`, `model_type`, `classification_threshold`, `performance_metrics`, `feature_importance`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/anti_fraud.py:2489` · `MLModelUploadResource`

### SECURITY-067 · 风控-Admin用户风控审核-列表

- 接口声明：`GET /admin-sensitive-operation-audits`
- 输入字段：`keyword`, `risk_start_time`, `risk_end_time`, `audit_start_time`, `audit_end_time`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:181` · `AdminSensitiveOperationAuditsResource`

### SECURITY-068 · 风控-Admin用户风控审核-详情

- 接口声明：`GET /admin-sensitive-operation-audits/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:218` · `AdminSensitiveOperationAuditResource`

### SECURITY-069 · 风控-Admin用户风控审核-审核

- 接口声明：`PUT /admin-sensitive-operation-audits/<int:id_>/audit`
- 输入字段：`status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:233` · `AdminSensitiveOperationAuditActionResource`

### SECURITY-070 · 风控-Admin用户风控审核-修改备注

- 接口声明：`PATCH /admin-sensitive-operation-audits/<int:id_>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:259` · `AdminSensitiveOperationAuditRemarkResource`

### SECURITY-071 · 风控-风控审核记录

- 接口声明：`GET /risk-infos`
- 输入字段：`keyword`, `reason`, `status`, `block_permissions`, `source`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：ns.use_kwargs(dict(keyword=fields.String, reason=ex_fields.EnumField(enum=RiskUser.Reason, enum_by_value=True), status=ex_fields.EnumField(enum=RiskUser.Status, enum_by_value=True)
- 代码依据：`app/api/admin/risk_control.py:536` · `RiskInfosResource`

### SECURITY-072 · 风控-风控账户列表-审核

- 接口声明：`POST /risk-infos`
- 输入字段：`ids`, `filter`, `status`, `prevent_seconds`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:658` · `RiskInfosResource`

### SECURITY-073 · 风控-风控账户审核

- 接口声明：`GET /risk-infos/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:777` · `RiskInfoResource`

### SECURITY-074 · 风控-系统风控审核

- 接口声明：`GET /risk-system-record`
- 输入字段：`market`, `reason`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:895` · `RiskRecordsResource`

### SECURITY-075 · 风控-用户风控事件审核

- 接口声明：`GET /risk-user-event-record`
- 输入字段：`source`, `reason`, `status`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1456` · `RiskUserEventRecordsResource`

### SECURITY-076 · 风控-用户风控事件审核-通过/拒绝

- 接口声明：`PATCH /risk-user-event-record/<int:id_>/audit`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1551` · `RiskUserEventRecordsAuditResource`

### SECURITY-077 · 风控-用户风控事件审核-修改备注

- 接口声明：`PATCH /risk-user-event-record/<int:id_>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1579` · `RiskUserEventRecordsRemarkResource`

### SECURITY-078 · 风控-用户风控事件-修改恢复时间

- 接口声明：`PATCH /risk-user-event-record/<int:id_>/resume-time`
- 输入字段：`resume_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1607` · `RiskUserEventRecordsResumeTimeResource`

### SECURITY-079 · 风控-强制KYC用户列表-列表

- 接口声明：`GET /mandatory-kyc-users`
- 输入字段：`user_id`, `kyc_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1679` · `MandatoryKycUsersResource`

### SECURITY-080 · 风控-强制KYC用户列表-新增

- 接口声明：`POST /mandatory-kyc-users`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1716` · `MandatoryKycUsersResource`

### SECURITY-081 · 风控-强制KYC用户列表-编辑备注

- 接口声明：`PATCH /mandatory-kyc-users/<int:user_id>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1762` · `MandatoryKycUserResource`

### SECURITY-082 · 风控-强制KYC用户列表-删除

- 接口声明：`DELETE /mandatory-kyc-users/<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1782` · `MandatoryKycUserResource`

### SECURITY-083 · 风控-强制KYC用户列表-模板下载

- 接口声明：`GET /mandatory-kyc-users/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1799` · `MandatoryKycUsersTemplateResource`

### SECURITY-084 · 风控-强制KYC用户列表-批量导入

- 接口声明：`POST /mandatory-kyc-users/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:1900` · `MandatoryKycUsersImportResource`

### SECURITY-085 · 风控-风控用户列表

- 接口声明：`GET /risk-users`
- 输入字段：`user`, `type`, `forbidden_status`, `remark`, `source`, `start`, `end`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2029` · `RiskUsersResource`

### SECURITY-086 · 风控-冻结用户列表-上传解析文件

- 接口声明：`POST /risk-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2207` · `RiskUsersResource`

### SECURITY-087 · 风控-风控用户列表-修改备注

- 接口声明：`PATCH /risk-users`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2219` · `RiskUsersResource`

### SECURITY-088 · 风控-风控用户列表-模板下载

- 接口声明：`GET /risk-users/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2406` · `RiskUsersTemplateResource`

### SECURITY-089 · 风控-风控用户列表-批量更新

- 接口声明：`POST /risk-users/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2425` · `RiskUsersTemplateResource`

### SECURITY-090 · 用户详情-风控信息

- 接口声明：`GET /users/<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2490` · `UserRiskInfoResource`

### SECURITY-091 · 风控-理财对账

- 接口声明：`GET /investment-balance-check`
- 输入字段：`asset`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2506` · `InvestmentBalanceCheckResource`

### SECURITY-092 · 风控-理财对账-对账

- 接口声明：`POST /investment-balance-check`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2569` · `InvestmentBalanceCheckResource`

### SECURITY-093 · 风控-理财对账-审核

- 接口声明：`PUT /investment-balance-check`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2579` · `InvestmentBalanceCheckResource`

### SECURITY-094 · 风控-理财对账-删除

- 接口声明：`DELETE /investment-balance-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2604` · `InvestmentBalanceCheckResource`

### SECURITY-095 · 风控-红包对账

- 接口声明：`GET /red-packet-check`
- 输入字段：`asset`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2630` · `RedPacketCheckResource`

### SECURITY-096 · 风控-红包对账-对账

- 接口声明：`POST /red-packet-check`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2689` · `RedPacketCheckResource`

### SECURITY-097 · 风控-红包对账-审核

- 接口声明：`PUT /red-packet-check`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2699` · `RedPacketCheckResource`

### SECURITY-098 · 风控-红包对账-删除

- 接口声明：`DELETE /red-packet-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2724` · `RedPacketCheckResource`

### SECURITY-099 · 风控-杠杆对账

- 接口声明：`GET /margin-loan-flat-check`
- 输入字段：`account_id`, `asset`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2750` · `MarginLoanFlatCheckResource`

### SECURITY-100 · 风控-杠杆对账-对账

- 接口声明：`POST /margin-loan-flat-check`
- 输入字段：`account_id`, `asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2823` · `MarginLoanFlatCheckResource`

### SECURITY-101 · 风控-杠杆对账-审核

- 接口声明：`PUT /margin-loan-flat-check`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2835` · `MarginLoanFlatCheckResource`

### SECURITY-102 · 风控-杠杆对账-删除

- 接口声明：`DELETE /margin-loan-flat-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2860` · `MarginLoanFlatCheckResource`

### SECURITY-103 · 风控-合约对账

- 接口声明：`GET /perpetual-balance-check`
- 输入字段：`asset`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2886` · `PerpetualBalanceCheckResource`

### SECURITY-104 · 风控-合约对账-对账

- 接口声明：`POST /perpetual-balance-check`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2957` · `PerpetualBalanceCheckResource`

### SECURITY-105 · 风控-合约对账-审核

- 接口声明：`PUT /perpetual-balance-check`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2967` · `PerpetualBalanceCheckResource`

### SECURITY-106 · 风控-合约对账-删除

- 接口声明：`DELETE /perpetual-balance-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:2992` · `PerpetualBalanceCheckResource`

### SECURITY-107 · 风控-矿池转入币种阈值配置

- 接口声明：`GET /viabtc-trans-threshold-conf`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3029` · `ViabtcTransThresholdConfsResource`

### SECURITY-108 · 风控-新增矿池转入币种阈值配置

- 接口声明：`POST /viabtc-trans-threshold-conf`
- 输入字段：`asset`, `threshold`, `risk_control_least_usd`, `remark`, `temp_threshold`, `temp_threshold_expire_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3104` · `ViabtcTransThresholdConfsResource`

### SECURITY-109 · 风控-修改币种风控阈值配置

- 接口声明：`PUT /viabtc-trans-threshold-conf/<int:id_>`
- 输入字段：`threshold`, `risk_control_least_usd`, `remark`, `temp_threshold`, `temp_threshold_expire_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3156` · `ViabtcTransThresholdConfResource`

### SECURITY-110 · 风控-取消币种风控阈值配置

- 接口声明：`DELETE /viabtc-trans-threshold-conf/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3185` · `ViabtcTransThresholdConfResource`

### SECURITY-111 · 风控-风控参数配置-特定币种制裁国家配置列表

- 接口声明：`GET /sanction-asset-country-configs`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3233` · `SanctionAssetCountryConfigsResource`

### SECURITY-112 · 风控-风控参数配置-新增特定币种制裁国家配置

- 接口声明：`POST /sanction-asset-country-configs`
- 输入字段：`asset`, `restricted_countries`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3258` · `SanctionAssetCountryConfigsResource`

### SECURITY-113 · 风控-风控参数配置-修改特定币种制裁国家配置

- 接口声明：`PUT /sanction-asset-country-configs/<int:id_>`
- 输入字段：`restricted_countries`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3303` · `SanctionAssetCountryConfigResource`

### SECURITY-114 · 风控-风控参数配置-删除特定币种制裁国家配置

- 接口声明：`DELETE /sanction-asset-country-configs/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3334` · `SanctionAssetCountryConfigResource`

### SECURITY-115 · 风控-修改风控参数配置

- 接口声明：`PUT /risk-config-setting`
- 输入字段：`config_data`, `group_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3366` · `RiskControlSettingResource`

### SECURITY-116 · 风控-获取所有风控参数配置

- 接口声明：`GET /risk-config-setting`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3408` · `RiskControlSettingResource`

### SECURITY-117 · 风控 - 异常穿仓多周期参数 - 获取配置

- 接口声明：`GET /liquidation-risk`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3456` · `LiquidationRiskConfigResource`

### SECURITY-118 · 风控 - 异常穿仓多周期参数 - 修改配置

- 接口声明：`PUT /liquidation-risk`
- 输入字段：`config_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3462` · `LiquidationRiskConfigResource`

### SECURITY-119 · 风控-Admin敏感操作风控配置-查看

- 接口声明：`GET /admin-sensitive-operation-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3645` · `AdminSensitiveOperationConfigResource`

### SECURITY-120 · 风控-Admin敏感操作风控配置-新增

- 接口声明：`POST /admin-sensitive-operation-config`
- 输入字段：`section`, `period_multiplier`, `abnormal_query_user_count`, `abnormal_query_sensitive_info_count`, `abnormal_export_doc_count`, `abnormal_export_doc_times`, `period_hours`, `call_count_threshold`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3659` · `AdminSensitiveOperationConfigResource`

### SECURITY-121 · 风控-Admin敏感操作风控配置-编辑

- 接口声明：`PUT /admin-sensitive-operation-config/<string:section>/<int:id_>`
- 输入字段：`period_multiplier`, `abnormal_query_user_count`, `abnormal_query_sensitive_info_count`, `abnormal_export_doc_count`, `abnormal_export_doc_times`, `period_hours`, `call_count_threshold`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3705` · `AdminSensitiveOperationConfigItemResource`

### SECURITY-122 · 风控-Admin敏感操作风控配置-删除

- 接口声明：`DELETE /admin-sensitive-operation-config/<string:section>/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3735` · `AdminSensitiveOperationConfigItemResource`

### SECURITY-123 · 风控-Admin敏感操作统计

- 接口声明：`GET /admin-sensitive-operation-stats`
- 输入字段：`admin_user_id`, `period_minutes`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3759` · `AdminSensitiveOperationStatsResource`

### SECURITY-124 · 风控-获取市场异常波动风控参数配置

- 接口声明：`GET /market-volatility-risk`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3804` · `MarketVolatilityRiskResource`

### SECURITY-125 · 风控-修改市场异常波动风控参数配置

- 接口声明：`PUT /market-volatility-risk`
- 输入字段：`config_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3810` · `MarketVolatilityRiskResource`

### SECURITY-126 · 风控-获取平台支出项告警参数配置

- 接口声明：`GET /platform-expense-risk`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3848` · `PlatformExpenseRiskResource`

### SECURITY-127 · 风控-修改平台支出项告警参数配置

- 接口声明：`PUT /platform-expense-risk`
- 输入字段：`config_name`, `config_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3870` · `PlatformExpenseRiskResource`

### SECURITY-128 · 风控-获取账户被盗风控参数配置

- 接口声明：`GET /account-theft-risk-control`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3915` · `AccountTheftRiskControlResource`

### SECURITY-129 · 风控-修改账户被盗风控参数配置

- 接口声明：`PUT /account-theft-risk-control`
- 输入字段：`config_name`, `config_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3933` · `AccountTheftRiskControlResource`

### SECURITY-130 · 风控-全站提现熔断阈值配置列表

- 接口声明：`GET /withdrawal-fuse-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:3974` · `WithdrawalFuseSettingsResource`

### SECURITY-131 · 风控-全站提现熔断阈值配置详情

- 接口声明：`GET /withdrawal-fuse-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4036` · `WithdrawalFuseSettingsManagementResource`

### SECURITY-132 · 风控-全站提现熔断阈值配置编辑

- 接口声明：`PUT /withdrawal-fuse-settings/<field>`
- 输入字段：`value`, `valid_from`, `valid_till`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4044` · `WithdrawalFuseSettingsManagementResource`

### SECURITY-133 · 风控-全站提现熔断阈值配置删除

- 接口声明：`DELETE /withdrawal-fuse-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4083` · `WithdrawalFuseSettingsManagementResource`

### SECURITY-134 · 风控-全站充值熔断阈值配置列表

- 接口声明：`GET /deposit-fuse-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4106` · `DepositFuseSettingsResource`

### SECURITY-135 · 风控-全站充值熔断阈值配置详情

- 接口声明：`GET /deposit-fuse-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4156` · `DepositFuseSettingsManagementResource`

### SECURITY-136 · 风控-全站充值熔断阈值配置编辑

- 接口声明：`PUT /deposit-fuse-settings/<field>`
- 输入字段：`value`, `valid_from`, `valid_till`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4164` · `DepositFuseSettingsManagementResource`

### SECURITY-137 · 风控-全站充值熔断阈值配置删除

- 接口声明：`DELETE /deposit-fuse-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4203` · `DepositFuseSettingsManagementResource`

### SECURITY-138 · 风控-币种累计充值阈值配置

- 接口声明：`GET /accumulated-deposit-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4226` · `AccumulatedDepositThresholdConfResource`

### SECURITY-139 · 风控-币种累计充值阈值档位配置

- 接口声明：`POST /accumulated-deposit-conf`
- 输入字段：`ranks`, `removes`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4250` · `AccumulatedDepositThresholdConfResource`

### SECURITY-140 · 风控-币种累计充值阈值档位配置-详情配置

- 接口声明：`PUT /accumulated-deposit-conf/<int:id_>`
- 输入字段：`deposit_threshold`, `user_deposit_threshold`, `limit_count_threshold`, `limit_amount_threshold`, `temp_limit_count_threshold`, `temp_limit_amount_threshold`, `temp_limit_expire_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4327` · `AccumulatedDepositThresholdDetailConfResource`

### SECURITY-141 · 风控-特殊币种累计充值阈值配置

- 接口声明：`GET /accumulated-deposit-special-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4370` · `AccumulatedDepositThresholdSpecialConfResource`

### SECURITY-142 · 风控-特殊币种累计充值阈值档位配置-详情配置

- 接口声明：`PUT /accumulated-deposit-special-conf/<int:id_>`
- 输入字段：`asset`, `deposit_threshold`, `user_deposit_threshold`, `limit_count_threshold`, `limit_amount_threshold`, `temp_limit_count_threshold`, `temp_limit_amount_threshold`, `temp_limit_expire_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4395` · `AccumulatedDepositThresholdSpecialDetailConfResource`

### SECURITY-143 · 风控-特殊币种累计充值阈值档位配置-关闭

- 接口声明：`PATCH /accumulated-deposit-special-conf/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4446` · `AccumulatedDepositThresholdSpecialDetailConfResource`

### SECURITY-144 · 风控-币种累计充值阈值配置（流通量占比）

- 接口声明：`GET /accumulated-deposit-proportion-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4467` · `AccumulatedDepositThresholdProportionConfResource`

### SECURITY-145 · 风控-币种累计充值阈值档位配置（流通量占比）

- 接口声明：`POST /accumulated-deposit-proportion-conf`
- 输入字段：`ranks`, `removes`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4491` · `AccumulatedDepositThresholdProportionConfResource`

### SECURITY-146 · 风控-币种累计充值阈值档位配置（流通量占比）-详情配置

- 接口声明：`PUT /accumulated-deposit-proportion-conf/<int:id_>`
- 输入字段：`user_period_dp`, `asset_period`, `asset_period_dp`, `user_deposit_threshold`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4568` · `AccumulatedDepositThresholdDetailProportionConfResource`

### SECURITY-147 · 风控-特殊币种累计充值阈值配置（流通量占比）

- 接口声明：`GET /accumulated-deposit-special-proportion-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4605` · `AccumulatedDepositThresholdSpecialProportionConfResource`

### SECURITY-148 · 风控-特殊币种累计充值阈值档位配置（流通量占比）-详情配置

- 接口声明：`PUT /accumulated-deposit-special-proportion-conf/<int:id_>`
- 输入字段：`asset`, `user_period`, `user_period_dp`, `user_single_dp`, `asset_period`, `asset_period_dp`, `user_deposit_threshold`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4630` · `AccumulatedDepositThresholdSpecialDetailProportionConfResource`

### SECURITY-149 · 风控-特殊币种累计充值阈值档位配置（流通量占比）-关闭

- 接口声明：`PATCH /accumulated-deposit-special-proportion-conf/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4674` · `AccumulatedDepositThresholdSpecialDetailProportionConfResource`

### SECURITY-150 · 风控-币种累计提现阈值配置

- 接口声明：`GET /accumulated-withdrawal-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4695` · `AccumulatedWithdrawalThresholdConfResource`

### SECURITY-151 · 风控-币种累计提现阈值档位配置

- 接口声明：`POST /accumulated-withdrawal-conf`
- 输入字段：`circulations`, `removes`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4719` · `AccumulatedWithdrawalThresholdConfResource`

### SECURITY-152 · 风控-币种累计提现阈值档位配置-详情配置

- 接口声明：`PUT /accumulated-withdrawal-conf/<int:id_>`
- 输入字段：`withdrawal_threshold`, `user_withdrawal_threshold`, `limit_amount_threshold`, `temp_limit_amount_threshold`, `temp_limit_expire_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4793` · `AccumulatedWithdrawalThresholdDetailConfResource`

### SECURITY-153 · 风控-特殊币种累计提现阈值配置

- 接口声明：`GET /accumulated-withdrawal-special-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4832` · `AccumulatedWithdrwalThresholdSpecialConfResource`

### SECURITY-154 · 风控-特殊币种累计提现阈值档位配置-详情配置

- 接口声明：`PUT /accumulated-withdrawal-special-conf/<int:id_>`
- 输入字段：`asset`, `withdrawal_threshold`, `limit_amount_threshold`, `user_withdrawal_threshold`, `temp_limit_amount_threshold`, `temp_limit_expire_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4857` · `AccumulatedWithdrawalThresholdSpecialDetailConfResource`

### SECURITY-155 · 风控-特殊币种累计提现阈值档位配置-关闭

- 接口声明：`PATCH /accumulated-withdrawal-special-conf/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4902` · `AccumulatedWithdrawalThresholdSpecialDetailConfResource`

### SECURITY-156 · 风控-p2p对账

- 接口声明：`GET /p2p-balance-check`
- 输入字段：`asset`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4923` · `P2pBalanceCheckResource`

### SECURITY-157 · 风控-p2p对账-对账

- 接口声明：`POST /p2p-balance-check`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4981` · `P2pBalanceCheckResource`

### SECURITY-158 · 风控-p2p对账-审核

- 接口声明：`PUT /p2p-balance-check`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:4991` · `P2pBalanceCheckResource`

### SECURITY-159 · 风控-p2p对账-删除

- 接口声明：`DELETE /p2p-balance-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5016` · `P2pBalanceCheckResource`

### SECURITY-160 · 风控-预测市场对账

- 接口声明：`GET /pre-trading-settle-check`
- 输入字段：`asset`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5042` · `PreTadingSettleCheckResource`

### SECURITY-161 · 风控-预测市场对账-对账

- 接口声明：`POST /pre-trading-settle-check`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5104` · `PreTadingSettleCheckResource`

### SECURITY-162 · 风控-预测市场对账-审核

- 接口声明：`PUT /pre-trading-settle-check`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5114` · `PreTadingSettleCheckResource`

### SECURITY-163 · 风控-预测市场对账-删除

- 接口声明：`DELETE /pre-trading-settle-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5139` · `PreTadingSettleCheckResource`

### SECURITY-164 · 风控-资产负债风控币种

- 接口声明：`GET /forbid-withdrawals`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5165` · `ForbidWithdrawalsResource`

### SECURITY-165 · 风控-商务上币风控阈值配置(市场)

- 接口声明：`GET /bus-online-coin-by-market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5206` · `BusOnlineCoinByMarketResource`

### SECURITY-166 · 风控-商务上币风控阈值配置(市场)-新增/编辑

- 接口声明：`POST /bus-online-coin-by-market`
- 输入字段：`market`, `period_by_min`, `decrease_threshold`, `sell_volume_usd_threshold`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5222` · `BusOnlineCoinByMarketResource`

### SECURITY-167 · 风控-商务上币风控阈值配置(市场)-删除

- 接口声明：`DELETE /bus-online-coin-by-market`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5276` · `BusOnlineCoinByMarketResource`

### SECURITY-168 · 风控-国家短信区号风控列表

- 接口声明：`GET /country-sms`
- 输入字段：`mobile_country_code`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5304` · `CountrySmsResource`

### SECURITY-169 · 风控-修改国家短信区号风控

- 接口声明：`PATCH /country-sms`
- 输入字段：`id`, `days`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5336` · `CountrySmsResource`

### SECURITY-170 · 风控-获取现货市场防对敲参数配置

- 接口声明：`GET /wash-sale-risk`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5368` · `WashSaleRiskResource`

### SECURITY-171 · 风控-修改现货市场防对敲风控参数配置

- 接口声明：`PUT /wash-sale-risk`
- 输入字段：`config_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5374` · `WashSaleRiskResource`

### SECURITY-172 · 风控-价格保护机制参数设置列表

- 接口声明：`GET /price-verify-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5412` · `PriceVerifySettingsResource`

### SECURITY-173 · 风控-价格保护机制参数设置编辑

- 接口声明：`PUT /price-verify-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5443` · `PriceVerifySettingsManagementResource`

### SECURITY-174 · 风控-价格保护机制参数设置置删除

- 接口声明：`DELETE /price-verify-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5464` · `PriceVerifySettingsManagementResource`

### SECURITY-175 · 风控-币种异常增发配置

- 接口声明：`GET /abnormal-issuance-conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5486` · `AssetAbnormalIssuanceConfResource`

### SECURITY-176 · 风控-币种异常增发档位配置

- 接口声明：`POST /abnormal-issuance-conf`
- 输入字段：`ranks`, `removes`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5529` · `AssetAbnormalIssuanceConfResource`

### SECURITY-177 · 风控-币种异常增发配置-详情配置

- 接口声明：`PUT /abnormal-issuance-conf/<int:id_>`
- 输入字段：`issuance_threshold`, `issuance_usd_threshold`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5600` · `AssetAbnormalIssuanceDetailConfResource`

### SECURITY-178 · 风控-风控电话告警列表-列表详情

- 接口声明：`GET /mobile-notice-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5634` · `MobileNoticeConfigResource`

### SECURITY-179 · 风控-风控电话告警-创建/编辑

- 接口声明：`POST /mobile-notice-config`
- 输入字段：`event_type`, `mobile_details`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5681` · `MobileNoticeConfigResource`

### SECURITY-180 · 风控-风控电话告警-删除

- 接口声明：`DELETE /mobile-notice-config`
- 输入字段：`event_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5737` · `MobileNoticeConfigResource`

### SECURITY-181 · 风控-风控关闭充提币种列表

- 接口声明：`GET /deposit-withdrawal-switch`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5761` · `DepositWithdrawalSwitchResource`

### SECURITY-182 · 风控-风控关闭充提币种列表-编辑备注

- 接口声明：`PATCH /deposit-withdrawal-switch`
- 输入字段：`asset`, `chain`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5832` · `DepositWithdrawalSwitchResource`

### SECURITY-183 · 风控-借贷对账

- 接口声明：`GET /pledge-loan-flat-check`
- 输入字段：`asset`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5857` · `PledgeLoanFlatCheckResource`

### SECURITY-184 · 风控-借贷对账-对账

- 接口声明：`POST /pledge-loan-flat-check`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5922` · `PledgeLoanFlatCheckResource`

### SECURITY-185 · 风控-杠杆对账-审核

- 接口声明：`PUT /pledge-loan-flat-check`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5932` · `PledgeLoanFlatCheckResource`

### SECURITY-186 · 风控-杠杆对账-删除

- 接口声明：`DELETE /pledge-loan-flat-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5957` · `PledgeLoanFlatCheckResource`

### SECURITY-187 · 风控-防干扰列表

- 接口声明：`GET /user-prevent-risk-control-config`
- 输入字段：`reason`, `user_id`, `start_created_ts`, `source`, `end_created_ts`, `start_expired_ts`, `end_expired_ts`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:5995` · `UserPreventRiskControlConfigResource`

### SECURITY-188 · 风控-防干扰列表-修改

- 接口声明：`PATCH /user-prevent-risk-control-config`
- 输入字段：`id`, `expired_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6124` · `UserPreventRiskControlConfigResource`

### SECURITY-189 · 风控-风控黑名单-设备ID黑名单-列表 

- 接口声明：`GET /device-id-blacklist`
- 输入字段：`device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6474` · `DeviceIDBlacklistResource`

### SECURITY-190 · 风控-风控黑名单-设备ID黑名单-新增 

- 接口声明：`POST /device-id-blacklist`
- 输入字段：`device_id`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6480` · `DeviceIDBlacklistResource`

### SECURITY-191 · 风控-风控黑名单-设备ID黑名单-编辑

- 接口声明：`PATCH /device-id-blacklist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6487` · `DeviceIDBlacklistResource`

### SECURITY-192 · 风控-风控黑名单-设备ID黑名单-删除 

- 接口声明：`DELETE /device-id-blacklist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6494` · `DeviceIDBlacklistResource`

### SECURITY-193 · 风控-风控黑名单-设备ID黑名单-批量导入

- 接口声明：`POST /device-id-blacklist/batch-import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6506` · `DeviceIDBlacklistBatchImportResource`

### SECURITY-194 · 风控-风控黑名单-IP地址黑名单-列表 

- 接口声明：`GET /ip-blacklist`
- 输入字段：`ip`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6540` · `IPBlacklistResource`

### SECURITY-195 · 风控-风控黑名单-IP地址黑名单-新增 

- 接口声明：`POST /ip-blacklist`
- 输入字段：`ip`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6546` · `IPBlacklistResource`

### SECURITY-196 · 风控-风控黑名单-IP地址黑名单-编辑

- 接口声明：`PATCH /ip-blacklist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6553` · `IPBlacklistResource`

### SECURITY-197 · 风控-风控黑名单-IP地址黑名单-删除

- 接口声明：`DELETE /ip-blacklist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6560` · `IPBlacklistResource`

### SECURITY-198 · 风控-风控黑名单-IP地址黑名单-批量导入

- 接口声明：`POST /ip-blacklist/batch-import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6571` · `IPBlacklistBatchImportResource`

### SECURITY-199 · 风控-风控黑名单-邮箱域名黑名单-列表

- 接口声明：`GET /email-domain-blacklist`
- 输入字段：`email_domain`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6598` · `EmailDomainBlacklistResource`

### SECURITY-200 · 风控-风控黑名单-邮箱域名黑名单-新增

- 接口声明：`POST /email-domain-blacklist`
- 输入字段：`email_domain`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6604` · `EmailDomainBlacklistResource`

### SECURITY-201 · 风控-风控黑名单-邮箱域名黑名单-编辑

- 接口声明：`PATCH /email-domain-blacklist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6611` · `EmailDomainBlacklistResource`

### SECURITY-202 · 风控-风控黑名单-邮箱域名黑名单-删除

- 接口声明：`DELETE /email-domain-blacklist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6618` · `EmailDomainBlacklistResource`

### SECURITY-203 · 风控-风控黑名单-邮箱域名黑名单-批量导入

- 接口声明：`POST /email-domain-blacklist/batch-import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6628` · `EmailDomainBlacklistBatchImportResource`

### SECURITY-204 · 风控-AWS邮件抑制名单-查询

- 接口声明：`GET /aws-suppressed-destination`
- 输入字段：`email`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6650` · `AWSSuppressedDestinationResource`

### SECURITY-205 · 风控-AWS邮件抑制名单-删除

- 接口声明：`DELETE /aws-suppressed-destination`
- 输入字段：`email`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/risk_control.py:6666` · `AWSSuppressedDestinationResource`

### SECURITY-206 · 风控-风控黑名单-下载模板

- 接口声明：`GET /blacklist/template`
- 输入字段：`black_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6698` · `BlacklistTemplateResource`

### SECURITY-207 · 反洗钱风控-获取高风险配置

- 接口声明：`GET /aml-config/high`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6765` · `AmlConfigHighResource`

### SECURITY-208 · 反洗钱风控-更新高风险配置

- 接口声明：`PUT /aml-config/high`
- 输入字段：`register_days`, `inactive_user_days`, `immediate_withdrawal`, `deposit_frequency`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6777` · `AmlConfigHighResource`

### SECURITY-209 · 反洗钱风控-删除高风险配置-充提频率异常

- 接口声明：`DELETE /aml-config/high/deposit-frequency`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6825` · `AmlConfigHighDepositFrequencyResource`

### SECURITY-210 · 反洗钱风控-获取中风险配置

- 接口声明：`GET /aml-config/medium`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6850` · `AmlConfigMediumResource`

### SECURITY-211 · 反洗钱风控-更新中风险配置

- 接口声明：`PUT /aml-config/medium`
- 输入字段：`kyt_pending`, `match_aml_risk_count`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6859` · `AmlConfigMediumResource`

### SECURITY-212 · 反洗钱风控-获取正常用户配置

- 接口声明：`GET /aml-config/normal`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6893` · `AmlConfigNormalResource`

### SECURITY-213 · 反洗钱风控-更新正常用户基础配置

- 接口声明：`PUT /aml-config/normal`
- 输入字段：`spot_market_count`, `recent_average_asset_value`, `security_tool_count`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6902` · `AmlConfigNormalResource`

### SECURITY-214 · 疑似被盗用户列表

- 接口声明：`GET /account-theft-self-verification`
- 输入字段：`keyword`, `status`, `has_valid_kyc`, `review_type`, `start_id`, `start_time`, `end_time`, `audited_start_time`, `audited_end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:6969` · `AccountTheftSelfVerificationResource`

### SECURITY-215 · 账户被盗-自助验证-备注

- 接口声明：`PATCH /account-theft-self-verification`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:7071` · `AccountTheftSelfVerificationResource`

### SECURITY-216 · 账户被盗-自助验证详情

- 接口声明：`GET /account-theft-self-verification/details`
- 输入字段：`risk_record_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:7102` · `AccountTheftSelfVerificationDetailResource`

### SECURITY-217 · 钱包管理-账户被盗-自助验证详情-审核流转

- 接口声明：`PUT /account-theft-self-verification/details`
- 输入字段：`risk_record_id`, `status`, `reject_reason`, `is_custom_reason`, `rejection_reason`, `custom_rejection_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:7303` · `AccountTheftSelfVerificationDetailResource`

### SECURITY-218 · 钱包管理-账户被盗-自助验证备注

- 接口声明：`PATCH /account-theft-self-verification/details`
- 输入字段：`risk_record_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:7389` · `AccountTheftSelfVerificationDetailResource`

### SECURITY-219 · 风控-异常注册参数配置

- 接口声明：`GET /registration-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:7532` · `RegistrationConfigResource`

### SECURITY-220 · 风控-修改异常注册参数配置

- 接口声明：`PUT /registration-config`
- 输入字段：`device_id_account_count_threshold`, `email_domain_age_threshold`, `device_id_registration_frequency`, `ip_registration_frequency`, `email_domain_registration_frequency`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:7537` · `RegistrationConfigResource`

### SECURITY-221 · 风控-合约负值账户

- 接口声明：`GET /perpetual-negative-balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_control.py:7597` · `PerpetualNegativeBalanceResource`

### SECURITY-222 · 运营>风险筛查>个人列表 

- 接口声明：`GET /individual/cases`
- 输入字段：`start`, `end`, `user_id`, `country`, `status`, `rating`, `audit_type`, `start_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:54` · `IndividualCaseListResource`

### SECURITY-223 · 运营>风险筛查>查看个人筛查详情 

- 接口声明：`GET /individual/screen-result`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:614` · `IndividualCasecreenResultResource`

### SECURITY-224 · 运营>风险筛查>同步匹配风险信息 

- 接口声明：`POST /individual/screen-result/sync-profile`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:711` · `IndividualCasecreenSyncProfileResource`

### SECURITY-225 · 运营>风险筛查>个人详情-修改个人筛查信息 

- 接口声明：`PUT /individual/case-edit/<int:case_row_id>`
- 输入字段：`country`, `name`, `gender`, `date_of_birth`, `sync_screen_result`, `force_sync_screen_result`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:727` · `IndividualCaseEditResource`

### SECURITY-226 · 运营>风险筛查>个人详情-审核操作 

- 接口声明：`POST /individual/case-audit/<int:case_row_id>`
- 输入字段：`audit_status`, `rejection_reason`, `is_custom_reason`, `custom_reject_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:840` · `IndividualCaseAuditResource`

### SECURITY-227 · 运营>风险筛查>个人详情-更新当前审核人 

- 接口声明：`POST /individual/case-auditors/<int:case_row_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:907` · `IndividualCaseAuditorsResource`

### SECURITY-228 · 运营>风险筛查>解析操作 

- 接口声明：`PUT /case-resolution`
- 输入字段：`case_id`, `ids`, `status_id`, `risk_id`, `reason_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:960` · `CaseResolutionResource`

### SECURITY-229 · 运营>风险筛查>设置评级 

- 接口声明：`PUT /case-rating`
- 输入字段：`id`, `rating`, `rating_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/risk_screen.py:1030` · `CaseRatingResource`

### SECURITY-230 · WebAuthnResource.get（用途待确认）

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/webauthn.py:35` · `WebAuthnResource`

### SECURITY-231 · 通行密钥-修改名称

- 接口声明：`PUT `
- 输入字段：`id`, `name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/webauthn.py:64` · `WebAuthnResource`

### SECURITY-232 · WebAuthnPreAuthResource.get（用途待确认）

- 接口声明：`GET /pre-auth`
- 输入字段：`operation_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/webauthn.py:92` · `WebAuthnPreAuthResource`

### SECURITY-233 · WebAuthnRegistration.get（用途待确认）

- 接口声明：`GET /registration`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/webauthn.py:109` · `WebAuthnRegistration`

### SECURITY-234 · WebAuthnRegistration.post（用途待确认）

- 接口声明：`POST /registration`
- 输入字段：`credential`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/webauthn.py:128` · `WebAuthnRegistration`

### SECURITY-235 · WebAuthnAuthentication.get（用途待确认）

- 接口声明：`GET /authentication`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/webauthn.py:149` · `WebAuthnAuthentication`

### SECURITY-236 · WebAuthnAuthentication.post（用途待确认）

- 接口声明：`POST /authentication`
- 输入字段：`credential`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/webauthn.py:160` · `WebAuthnAuthentication`

## 相关测试文件（路径归类，未执行）

- `tests/api/admin/test_anti_fraud_manual_annotation_import.py`
- `tests/api/admin/test_anti_fraud_supplement_jobs.py`
- `tests/api/admin/test_risk_users.py`
- `tests/api/frontend/test_security_reset_liveness.py`
- `tests/business/clients/test_anti_fraud.py`
- `tests/business/risk_control/__init__.py`
- `tests/business/risk_control/test_aml.py`
- `tests/business/risk_control/test_base.py`
- `tests/business/risk_control/test_country_sms.py`
- `tests/business/test_anti_fraud_user_facts.py`
- `tests/business/test_security_withdraw_password.py`
- `tests/business/test_withdraw_password.py`
- `tests/schedules/test_risk_report.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
