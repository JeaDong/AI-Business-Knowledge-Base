# 平台与其他能力 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### PLATFORM-001 · 用户-特殊配置-用户Tag标签管理-用户标签列表 

- 接口声明：`GET /category`
- 输入字段：`page`, `limit`, `tag_id`, `status`, `start`, `end`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:28` · `AdminTagCategoryResource`

### PLATFORM-002 · 用户-特殊配置-用户Tag标签管理-用户Tag标签管理-编辑标签状态 

- 接口声明：`POST /category/status`
- 输入字段：`tag_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:96` · `AdminTagCategoryStatusResource`

### PLATFORM-003 · 用户-特殊配置-用户Tag标签管理-标签用户详情 

- 接口声明：`GET /users`
- 输入字段：`page`, `tag_id`, `user_id`, `status`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:204` · `AdminTagUsersResource`

### PLATFORM-004 · 用户-特殊配置-用户Tag标签管理-标签用户详情-添加用户 

- 接口声明：`POST /users`
- 输入字段：`tag_id`, `user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:218` · `AdminTagUsersResource`

### PLATFORM-005 · 用户-特殊配置-用户Tag标签管理-标签用户详情-编辑用户备注 

- 接口声明：`PUT /users`
- 输入字段：`tag_id`, `user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:251` · `AdminTagUsersResource`

### PLATFORM-006 · 用户-特殊配置-用户Tag标签管理-标签用户详情-导出 

- 接口声明：`GET /users/export`
- 输入字段：`page`, `tag_id`, `user_id`, `status`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:285` · `AdminTagUsersExportResource`

### PLATFORM-007 · 用户-特殊配置-用户Tag标签管理-标签用户详情-编辑用户状态 

- 接口声明：`POST /users/status`
- 输入字段：`tag_id`, `user_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:305` · `AdminTagUsersStatusResource`

### PLATFORM-008 · 用户-特殊配置-用户Tag标签管理-标签用户详情-批量生效/失效 

- 接口声明：`POST /users/status/batch`
- 输入字段：`tag_id`, `ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:350` · `AdminTagUsersStatusBatchResource`

### PLATFORM-009 · 用户-特殊配置-用户Tag标签管理-标签用户详情-上传 

- 接口声明：`POST /users/upload/<int:tag_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/admin_tag.py:394` · `AdminTagUsersBatchResource`

### PLATFORM-010 · 系统 - AI任务查询 - 币种研报分析列表

- 接口声明：`GET /records`
- 输入字段：`asset`, `start_time`, `end_time`, `page`, `page_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_analysis.py:67` · `AIAnalysisListResource`

### PLATFORM-011 · 系统 - AI任务查询 - 币种研报分析详情

- 接口声明：`GET /<int:analysis_id>/contents`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_analysis.py:127` · `AIAnalysisContentResource`

### PLATFORM-012 · 查询AI任务

- 接口声明：`GET /tasks/search`
- 输入字段：`task_type`, `execution_mode`, `start_time`, `end_time`, `business`, `business_id`, `status`, `page`, `page_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_analytics.py:33` · `AITaskSearchResource`

### PLATFORM-013 · 从 AI 服务获取其支持的任务类型。

- 接口声明：`GET /task-types`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_analytics.py:201` · `AITaskTypesResource`

### PLATFORM-014 · 查询所有AI任务的成本统计

- 接口声明：`GET /costs`
- 输入字段：`start_date`, `end_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_analytics.py:214` · `AICostsResource`

### PLATFORM-015 · 同步翻译

- 接口声明：`POST /sync`
- 输入字段：`source`, `target`, `content`, `term`, `business`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_translation.py:31` · `SyncTranslationResource`

### PLATFORM-016 · 异步翻译

- 接口声明：`POST /async`
- 输入字段：`source`, `target`, `content`, `business`, `business_id`, `business_info`, `term`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_translation.py:54` · `AsyncTranslationResource`

### PLATFORM-017 · 获取翻译结果

- 接口声明：`GET /tasks`
- 输入字段：`business`, `business_id`, `task_id`, `business_info`, `with_content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_translation.py:87` · `TranslationTaskResource`

### PLATFORM-018 · 删除翻译结果（软删除）

- 接口声明：`DELETE /tasks`
- 输入字段：`business`, `business_id`, `target_langs`, `business_info`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_translation.py:130` · `TranslationTaskResource`

### PLATFORM-019 · 获取详细翻译结果

- 接口声明：`GET /task/<string:id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_translation.py:177` · `TranslationTaskDetailResource`

### PLATFORM-020 · 系统-AI任务查询-流式翻译

- 接口声明：`POST /stream`
- 输入字段：`target`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ai_translation.py:201` · `StreamTranslateResource`

### PLATFORM-021 · 用户-大使-信息

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:70` · `AmbassadorInfoResource`

### PLATFORM-022 · 用户-大使-大使列表

- 接口声明：`GET `
- 输入字段：`status`, `level`, `type`, `user_id`, `agent_id`, `location_code`, `page`, `limit`, `export`, `sort_name`, `source`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:139` · `AmbassadorListResource`

### PLATFORM-023 · 用户-大使-变更记录 

- 接口声明：`GET /change-history`
- 输入字段：`search_keyword`, `change_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:516` · `AmbassadorChangeLogResource`

### PLATFORM-024 · 用户-大使-大使推荐列表

- 接口声明：`GET /referral`
- 输入字段：`user_id`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:659` · `AmbassadorReferralResource`

### PLATFORM-025 · 用户-大使-大使风采列表

- 接口声明：`GET /stars`
- 输入字段：`user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:753` · `AmbassadorStarListResource`

### PLATFORM-026 · 用户-大使-新建大使风采

- 接口声明：`POST /stars`
- 输入字段：`user_id`, `name`, `intro_cn`, `intro_en`, `intro_tc`, `file_id`, `continent`, `country`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:791` · `AmbassadorStarListResource`

### PLATFORM-027 · 用户-大使-编辑大使风采

- 接口声明：`PATCH /star/<int:id_>`
- 输入字段：`name`, `intro_cn`, `intro_en`, `intro_tc`, `file_id`, `continent`, `country`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:852` · `AmbassadorStarResource`

### PLATFORM-028 · 用户-大使-删除大使风采

- 接口声明：`DELETE /star/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:893` · `AmbassadorStarResource`

### PLATFORM-029 · 用户-大使-修改大使风采排序

- 接口声明：`PUT /star-order/<int:id_>`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:927` · `AmbassadorStarOrderResource`

### PLATFORM-030 · 大使申请列表

- 接口声明：`GET /applications`
- 输入字段：`status`, `location_code`, `refer_keyword`, `ambassador_keyword`, `keyword`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:992` · `AmbassadorApplicationListResource`

### PLATFORM-031 · 大使申请详情

- 接口声明：`GET /application/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1143` · `AmbassadorApplicationResource`

### PLATFORM-032 · 大使代理列表

- 接口声明：`GET /agents`
- 输入字段：`status`, `is_appraisal`, `is_ambassador`, `user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1167` · `AmbassadorAgentListResource`

### PLATFORM-033 · 用户-大使代理-变更记录 

- 接口声明：`GET /agent/change-history`
- 输入字段：`search_keyword`, `change_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1223` · `AmbassadorAgentChangeLogResource`

### PLATFORM-034 · 用户-CoinEX代理-代理推荐列表 

- 接口声明：`GET /agent/referral`
- 输入字段：`user_id`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1312` · `AmbassadorAgentReferralResource`

### PLATFORM-035 · 特殊返佣比例列表

- 接口声明：`GET /rate`
- 输入字段：`business_type`, `start_date`, `end_date`, `keyword`, `page`, `limit`, `export`, `active_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1392` · `SpecialReferralRateResource`

### PLATFORM-036 · 添加特殊返佣比例

- 接口声明：`POST /rate`
- 输入字段：`user_id`, `business_data`, `expired_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1486` · `SpecialReferralRateResource`

### PLATFORM-037 · 修改特殊返佣比例

- 接口声明：`PUT /rate`
- 输入字段：`user_id`, `business_type`, `rate`, `expired_at`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1551` · `SpecialReferralRateResource`

### PLATFORM-038 · 删除特殊返佣比例

- 接口声明：`DELETE /rate`
- 输入字段：`user_id`, `business_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1595` · `SpecialReferralRateResource`

### PLATFORM-039 · 特殊返佣比例-批量上传

- 接口声明：`POST /rate/batch-import`
- 输入字段：`data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1637` · `BatchSpecialReferralRateResource`

### PLATFORM-040 · 大使-高潜线索库

- 接口声明：`GET /potential`
- 输入字段：`user_id`, `location`, `area`, `source`, `status`, `ambassador_status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1745` · `PotentialAmbassadorResource`

### PLATFORM-041 · 大使-商务线索库

- 接口声明：`GET /business/trace`
- 输入字段：`user_id`, `location`, `area`, `language`, `source`, `status`, `ambassador_status`, `trace_user_id`, `order_by`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:1896` · `BusinessAmbassadorTraceResource`

### PLATFORM-042 · 商务线索库-批量分配跟进人

- 接口声明：`POST /business/batch/trace`
- 输入字段：`user_ids`, `trace_user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2190` · `BusinessTraceDetailResource`

### PLATFORM-043 · 商务线索库-修改备注

- 接口声明：`PUT /business/batch/trace`
- 输入字段：`trace_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2229` · `BusinessTraceDetailResource`

### PLATFORM-044 · 商务线索库-终止跟进

- 接口声明：`DELETE /business/batch/trace`
- 输入字段：`trace_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2259` · `BusinessTraceDetailResource`

### PLATFORM-045 · 用户-大使体系-大使活动列表

- 接口声明：`GET /activities`
- 输入字段：`name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2290` · `AmbassadorActivitiesResource`

### PLATFORM-046 · 用户-大使体系-大使活动创建

- 接口声明：`POST /activities`
- 输入字段：`name`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2324` · `AmbassadorActivitiesResource`

### PLATFORM-047 · 用户-大使体系-大使活动详情

- 接口声明：`GET /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2353` · `AmbassadorActivityResource`

### PLATFORM-048 · 用户-大使体系-大使活动编辑

- 接口声明：`PUT /activity/<int:id_>`
- 输入字段：`name`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2374` · `AmbassadorActivityResource`

### PLATFORM-049 · 用户-大使体系-大使活动状态编辑

- 接口声明：`PATCH /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2398` · `AmbassadorActivityResource`

### PLATFORM-050 · 用户-大使体系-获取单条内容

- 接口声明：`GET /activity/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2426` · `AmbassadorActivityContentResource`

### PLATFORM-051 · 用户-大使体系-大使活动内容编辑

- 接口声明：`PUT /activity/<int:id_>/langs/<lang>`
- 输入字段：`content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador.py:2434` · `AmbassadorActivityContentResource`

### PLATFORM-052 · 大使激励包>批次管理-列表

- 接口声明：`GET /batch`
- 输入字段：`page`, `limit`, `batch_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:38` · `AmbassadorPackageBatchResource`

### PLATFORM-053 · 大使激励包>批次管理-创建

- 接口声明：`POST /batch`
- 输入字段：`batch_name`, `asset`, `package_amount`, `periods`, `valid_days`, `refer_trade_users`, `refer_trade_amount`, `release_time`, `group_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:95` · `AmbassadorPackageBatchResource`

### PLATFORM-054 · 大使激励包>批次管理-更新状态

- 接口声明：`PATCH /batch/<int:batch_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:147` · `AmbassadorPackageBatchDetailResource`

### PLATFORM-055 · 大使激励包>批次管理-审核驳回

- 接口声明：`DELETE /batch/<int:batch_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:214` · `AmbassadorPackageBatchDetailResource`

### PLATFORM-056 · 大使激励包>批次管理-更新

- 接口声明：`PUT /batch/<int:batch_id>`
- 输入字段：`batch_name`, `asset`, `package_amount`, `periods`, `valid_days`, `refer_trade_users`, `refer_trade_amount`, `release_time`, `group_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:237` · `AmbassadorPackageBatchDetailResource`

### PLATFORM-057 · 大使激励包>批次管理-用户下载

- 接口声明：`GET /batch/<int:batch_id>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:311` · `AmbassadorPackageBatchUserDownloadResource`

### PLATFORM-058 · 大使激励包>批次统计-列表

- 接口声明：`GET /batch/stats`
- 输入字段：`page`, `limit`, `batch_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:362` · `AmbassadorPackageBatchStatsResource`

### PLATFORM-059 · 大使激励包>使用明细-列表

- 接口声明：`GET /user/packages`
- 输入字段：`page`, `limit`, `batch_id`, `user_id`, `ambassador_type`, `status`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:451` · `UserPackageResource`

### PLATFORM-060 · 大使激励包>使用明细-停用

- 接口声明：`PATCH /user/package/<int:package_id>/stop`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:621` · `UserPackageDetailResource`

### PLATFORM-061 · 大使激励包>结算记录-列表

- 接口声明：`GET /batch/settlement/records`
- 输入字段：`page`, `limit`, `batch_id`, `user_id`, `start_time`, `end_time`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/ambassador_package.py:667` · `PackageSettlementHistoryResource`

### PLATFORM-062 · 风控 - 反洗钱高风险用户列表 - 查询列表

- 接口声明：`GET /high-risk-users`
- 输入字段：`user_id`, `keyword`, `country_code`, `region_code`, `status`, `control_type`, `effective_start_time`, `effective_end_time`, `sort_field`, `sort_order`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/aml.py:39` · `AMLHighRiskUsersResource`

### PLATFORM-063 · 风控 - 反洗钱高风险用户列表 - 添加用户

- 接口声明：`POST /high-risk-users`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/aml.py:169` · `AMLHighRiskUsersResource`

### PLATFORM-064 · 风控 - 反洗钱高风险用户列表 - 修改状态/备注

- 接口声明：`PATCH /high-risk-users/<int:row_id>`
- 输入字段：`status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/aml.py:269` · `AMLHighRiskUserResource`

### PLATFORM-065 · 风控 - 反洗钱高风险用户列表 - 批量导入

- 接口声明：`POST /high-risk-users/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/aml.py:299` · `AMLHighRiskUsersImportResource`

### PLATFORM-066 · 风控 - 反洗钱高风险用户列表 - 下载导入模板

- 接口声明：`GET /high-risk-users/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/aml.py:333` · `AMLHighRiskUsersTemplateResource`

### PLATFORM-067 · API 加速配置列表

- 接口声明：`GET /config`
- 输入字段：`search_keyword`, `trade_type`, `api_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/api_speed.py:40` · `UserApiSpeedConfigResource`

### PLATFORM-068 · 创建 API 加速配置

- 接口声明：`POST /config`
- 输入字段：`user_id`, `group`, `ms`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/api_speed.py:117` · `UserApiSpeedConfigResource`

### PLATFORM-069 · 修改 API 加速配置

- 接口声明：`PUT /config/<int:id_>`
- 输入字段：`ms`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/api_speed.py:159` · `EditUserApiSpeedConfigResource`

### PLATFORM-070 · 删除 API 加速配置

- 接口声明：`DELETE /config/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/api_speed.py:182` · `EditUserApiSpeedConfigResource`

### PLATFORM-071 · 币币-定投-定投档位配置 

- 接口声明：`GET /config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:56` · `AutoInvestConfigResource`

### PLATFORM-072 · 币币-定投-定投档位配置-修改 

- 接口声明：`PUT /config`
- 输入字段：`configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:72` · `AutoInvestConfigResource`

### PLATFORM-073 · 币币-定投-市场定投档位 

- 接口声明：`GET /market-depths`
- 输入字段：`market`, `rank`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:124` · `AutoInvestMarketsResource`

### PLATFORM-074 · 币币-定投-添加市场定投档位 

- 接口声明：`POST /market-depths`
- 输入字段：`market`
- 显式控制：lock_request(key='auto_invest_market_edit')
- 代码依据：`app/api/admin/auto_invest.py:173` · `AutoInvestMarketsResource`

### PLATFORM-075 · 币币-定投-删除市场定投档位 

- 接口声明：`DELETE /market-depths/<string:market>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：lock_request(key='auto_invest_market_edit')
- 代码依据：`app/api/admin/auto_invest.py:217` · `AutoInvestMarketDepthDetailResource`

### PLATFORM-076 · 币币-定投-定投订单列表 

- 接口声明：`GET /orders`
- 输入字段：`start`, `end`, `user_id`, `plan_id`, `source_asset`, `target_asset`, `status`, `result`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:248` · `AutoInvestOrderListResource`

### PLATFORM-077 · 币币-定投-定投策略列表

- 接口声明：`GET /plans`
- 输入字段：`start`, `end`, `user_id`, `plan_id`, `source_asset`, `target_asset`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:309` · `AutoInvestPlanListResource`

### PLATFORM-078 · 币币-定投-终止策略

- 接口声明：`PUT /plans/<int:id_>/stop`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:387` · `AutoInvestPlanStopResource`

### PLATFORM-079 · 币币-定投-批量终止策略

- 接口声明：`PUT /plans/batch-stop`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:408` · `AutoInvestPlanBatchStopResource`

### PLATFORM-080 · 币币-定投-策略修改记录列表

- 接口声明：`GET /plans/<int:id_>/logs`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:445` · `AutoInvestPlanLogResource`

### PLATFORM-081 · 币币-定投-系统定投订单列表 

- 接口声明：`GET /sys-orders`
- 输入字段：`order_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:477` · `SysAutoInvestOrderListResource`

### PLATFORM-082 · 币币-定投-系统定投订单-挂单历史 

- 接口声明：`GET /sys-trade-orders`
- 输入字段：`sys_order_id`, `status`, `has_deal`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auto_invest.py:522` · `SysAssetAutoInvestTradeOrderListResource`

### PLATFORM-083 · 风控 - 用户资产导出 - 查询列表

- 接口声明：`GET /user-asset`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/batch_export.py:85` · `UserAssetExportResource`

### PLATFORM-084 · 风控 - 用户资产导出 - 上传数据

- 接口声明：`POST /user-asset`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/batch_export.py:131` · `UserAssetExportResource`

### PLATFORM-085 · 风控 - 用户资产导出 - 下载模板

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/batch_export.py:176` · `UserAssetExportTemplateResource`

### PLATFORM-086 · 风控 - 用户资产导出 - 更新数据

- 接口声明：`POST /user-asset/<int:export_id>`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/batch_export.py:193` · `UserAssetExportDetailResource`

### PLATFORM-087 · 风控 - 用户资产导出 - 下载

- 接口声明：`GET /user-asset/<int:export_id>`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/batch_export.py:229` · `UserAssetExportDetailResource`

### PLATFORM-088 · 用户-大客户体系-大区团队-团队列表

- 接口声明：`GET /teams`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:160` · `BigCustomerTeamsResource`

### PLATFORM-089 · 用户-大客户体系-大区团队-编辑团队

- 接口声明：`PUT /teams`
- 输入字段：`id`, `leader_id`, `pr_user_ids`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:348` · `BigCustomerTeamsResource`

### PLATFORM-090 · 用户-大客户体系-大区团队-KA经理列表

- 接口声明：`GET /manager`
- 输入字段：`user_id`, `team_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:429` · `BigCustomerManagersResource`

### PLATFORM-091 · 用户-大客户体系-大区团队-添加KA经理

- 接口声明：`POST /manager`
- 输入字段：`user_id`, `team_id`, `self_rate`, `leader_rate`, `pr_rates`, `remark`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/big_customer.py:627` · `BigCustomerManagersResource`

### PLATFORM-092 · 用户-大客户体系-大区团队-编辑KA经理

- 接口声明：`PUT /manager`
- 输入字段：`user_id`, `team_id`, `self_rate`, `leader_rate`, `pr_rates`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:679` · `BigCustomerManagersResource`

### PLATFORM-093 · 用户-大客户体系-大区团队-修改KA经理状态

- 接口声明：`PATCH /manager`
- 输入字段：`user_id`, `status`, `new_manager_id_to_assign`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:737` · `BigCustomerManagersResource`

### PLATFORM-094 · 用户-大客户体系-大区团队-KA经理列表导出

- 接口声明：`GET /manager/export`
- 输入字段：`user_id`, `team_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:834` · `BigCustomerManagerExportResource`

### PLATFORM-095 · 用户-大客户体系-大客户-大客户列表

- 接口声明：`GET `
- 输入字段：`user_id`, `manager_id`, `team_id`, `big_customer_type`, `status`, `has_manager`, `country_code`, `sort_col`, `sort_type`, `chat_message_count_range`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:889` · `BigCustomerResource`

### PLATFORM-096 · 用户-大客户体系-大客户-大客户列表详情

- 接口声明：`GET /<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1125` · `BigCustomerDetailResource`

### PLATFORM-097 · 用户-大客户体系-大客户-聊天消息翻译

- 接口声明：`POST /<int:user_id>/im-msg/translate`
- 输入字段：`msg_key`, `msg_id`, `seq`, `send_id`, `send_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1203` · `BigCustomerImMsgTranslateResource`

### PLATFORM-098 · 用户-大客户体系-大客户-大客户国家详情信息

- 接口声明：`GET /country-info`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1247` · `BigCustomerCountryInfoResource`

### PLATFORM-099 · 用户-大客户体系-大客户-大客户列表导出

- 接口声明：`GET /export`
- 输入字段：`user_id`, `manager_id`, `team_id`, `big_customer_type`, `status`, `has_manager`, `country_code`, `sort_col`, `sort_type`, `chat_message_count_range`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1308` · `BigCustomerExportResource`

### PLATFORM-100 · 用户-大客户体系-大客户-导出数据

- 接口声明：`POST /export-data`
- 输入字段：`export_type`, `start_month`, `end_month`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1340` · `BigCustomerDataExportResource`

### PLATFORM-101 · 用户-大客户体系-大客户-导出数据历史

- 接口声明：`GET /export-data/history`
- 输入字段：`export_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1384` · `BigCustomerDataExportHistoryResource`

### PLATFORM-102 · 用户-大客户列表-编辑大客户(修改备注)

- 接口声明：`PUT /<int:user_id>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1431` · `BigUserCustomerDetailResource`

### PLATFORM-103 · 用户-大客户列表-大客户曲线数据

- 接口声明：`GET /series`
- 输入字段：`user_id`, `data_type`, `start_date`, `end_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1458` · `BigUserCustomerSeriesResource`

### PLATFORM-104 · 用户-大客户体系-大客户-新增大客户(需审核)

- 接口声明：`POST /new-audit/add-big-customer`
- 输入字段：`user_id`, `big_customer_type`, `manager_id`, `remark`, `file_keys`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/big_customer.py:1644` · `NewAuditAddBigCustomerResource`

### PLATFORM-105 · 用户-大客户体系-大客户-设置KA经理(无需审核)

- 接口声明：`POST /new-audit/edit-manager`
- 输入字段：`user_id`, `manager_id`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/big_customer.py:1700` · `NewAuditEditManagerResource`

### PLATFORM-106 · 用户-大客户体系-大客户-设置KA经理模版

- 接口声明：`GET /edit-manager/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1762` · `BigCustomerEditManagerTemplateResource`

### PLATFORM-107 · 用户-大客户体系-大客户-设置KA经理模板上传

- 接口声明：`POST /edit-manager/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1771` · `BigCustomerEditManagerTemplateResource`

### PLATFORM-108 · 用户-大客户体系-大客户-修改大客户类型(需审核)

- 接口声明：`POST /new-audit/edit-type`
- 输入字段：`user_id`, `big_customer_type`, `remark`, `file_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1857` · `NewAuditEditBigCustomerTypeResource`

### PLATFORM-109 · 用户-大客户体系-大客户-删除大客户(需审核)

- 接口声明：`POST /new-audit/delete-big-customer`
- 输入字段：`user_id`, `remark`, `file_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:1905` · `NewAuditDeleteBitCustomerResource`

### PLATFORM-110 · 用户-大客户体系-大客户-大客户审核列表

- 接口声明：`GET /audit-list`
- 输入字段：`user_id`, `manager_id`, `status`, `audit_type`, `big_customer_type`, `only_system`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2016` · `BigCustomerAuditListResource`

### PLATFORM-111 · 用户-大客户体系-大客户-大客户审核列表-导出

- 接口声明：`GET /audit-list/export`
- 输入字段：`user_id`, `manager_id`, `status`, `audit_type`, `big_customer_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2130` · `BigCustomerAuditListExportResource`

### PLATFORM-112 · 用户-大客户体系-大客户-大客户审核-初审

- 接口声明：`POST /audit/do-audit`
- 输入字段：`id`, `status`, `comment`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2154` · `DoBigCustomerAuditResource`

### PLATFORM-113 · 用户-大客户体系-大客户-大客户审核-复审

- 接口声明：`POST /audit/do-review`
- 输入字段：`id`, `status`, `comment`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2201` · `DoBigCustomerReviewResource`

### PLATFORM-114 · 用户-大客户体系-大客户-平台大客户预添加列表

- 接口声明：`GET /pre-add-list`
- 输入字段：`user_id`, `team_id`, `country_code`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2284` · `BigCustomerPreAddListResource`

### PLATFORM-115 · 用户-大客户体系-大客户-平台大客户预添加列表-导出

- 接口声明：`GET /pre-add-list/export`
- 输入字段：`user_id`, `team_id`, `country_code`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2375` · `BigCustomerPreAddListExportResource`

### PLATFORM-116 · 用户-大客户体系-大客户-申请列表

- 接口声明：`GET /application-list`
- 输入字段：`id`, `keyword`, `user_id`, `manager_keyword`, `manager_id`, `team_id`, `country_code`, `status`, `big_customer_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2410` · `BigCustomerApplicationListResource`

### PLATFORM-117 · 用户-大客户体系-大客户-申请列表-导出

- 接口声明：`GET /application-list/export`
- 输入字段：`id`, `keyword`, `user_id`, `manager_keyword`, `manager_id`, `team_id`, `country_code`, `status`, `big_customer_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2558` · `BigCustomerApplicationListExportResource`

### PLATFORM-118 · 用户-大客户体系-大客户-申请详情

- 接口声明：`GET /application/<int:application_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2601` · `BigCustomerApplicationResource`

### PLATFORM-119 · 用户-大客户体系-大客户-申请修改KA经理

- 接口声明：`PUT /application/<int:application_id>/manager`
- 输入字段：`manager_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2642` · `BigCustomerApplicationManagerResource`

### PLATFORM-120 · 用户-大客户体系-大客户-申请编辑备注

- 接口声明：`PUT /application/<int:application_id>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2665` · `BigCustomerApplicationRemarkResource`

### PLATFORM-121 · 用户-大客户体系-大客户-申请审核

- 接口声明：`PUT /application/<int:application_id>/review`
- 输入字段：`action`, `manager_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2687` · `BigCustomerApplicationReviewResource`

### PLATFORM-122 · 用户-大客户体系-大客户-大客户变更记录

- 接口声明：`GET /changelog-list`
- 输入字段：`user_id`, `start_time`, `end_time`, `audit_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2733` · `BigCustomerChangelogListResource`

### PLATFORM-123 · 用户-大客户体系-大客户-大客户变更记录-导出

- 接口声明：`GET /changelog-list/export`
- 输入字段：`user_id`, `start_time`, `end_time`, `audit_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2817` · `BigCustomerChangelogListExportResource`

### PLATFORM-124 · 大客户-修改大客户参数配置

- 接口声明：`PUT /big-customer-config-setting`
- 输入字段：`config_data`, `group_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2838` · `BigCustomerSettingResource`

### PLATFORM-125 · 大客户-获取所有大客户参数配置

- 接口声明：`GET /big-customer-config-setting`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2880` · `BigCustomerSettingResource`

### PLATFORM-126 · 用户-大客户体系-大客户-获取大客户国家参数配置

- 接口声明：`GET /country-config-setting`
- 输入字段：`team_id`, `area`, `country_code`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:2921` · `BigCustomerCountrySettingResource`

### PLATFORM-127 · 用户-大客户体系-大客户-修改大客户国家参数配置

- 接口声明：`PUT /country-config-setting`
- 输入字段：`country_code`, `config_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/big_customer.py:3035` · `BigCustomerCountrySettingResource`

### PLATFORM-128 · 运营-博客-博客类别管理

- 接口声明：`GET /category`
- 输入字段：`page`, `limit`, `lang`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:26` · `BlogCategoryResource`

### PLATFORM-129 · 运营-博客-添加博客类别

- 接口声明：`POST /category`
- 输入字段：`name`, `remark`, `lang`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:57` · `BlogCategoryResource`

### PLATFORM-130 · 运营-博客-修改博客类别

- 接口声明：`PUT /category/<int:id_>`
- 输入字段：`name`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:91` · `BlogCategoryEditResource`

### PLATFORM-131 · 运营-博客-删除博客类别

- 接口声明：`DELETE /category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:112` · `BlogCategoryEditResource`

### PLATFORM-132 · 运营-博客类别管理-类别移动

- 接口声明：`PUT /category/<int:id_>/sort_id`
- 输入字段：`sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:135` · `BlogSortCategoryResource`

### PLATFORM-133 · 运营-博客类别管理-启用/停用

- 接口声明：`PUT /category/<int:id_>/enable`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:176` · `BlogEnableCategoryResource`

### PLATFORM-134 · 运营-博客-博客管理

- 接口声明：`GET /list`
- 输入字段：`page`, `category_id`, `blog_id`, `seo_url_keyword`, `lang`, `read_start_time`, `read_end_time`, `publish_start_time`, `publish_end_time`, `limit`, `sort_name`, `sort_type`, `is_blueprint`, `status`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:224` · `BlogResource`

### PLATFORM-135 · 运营-博客-创建博客主体

- 接口声明：`POST /list`
- 输入字段：`remark`, `category_id`, `published_at`, `lang`, `seo_url_keyword`, `seo_title`, `draft_title`, `draft_content`, `draft_abstract`, `cover`, `app_cover`, `is_blueprint`, `blueprint_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:363` · `BlogResource`

### PLATFORM-136 · 运营-博客管理-博客详情

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:450` · `BlogDetailsResource`

### PLATFORM-137 · 运营-博客-编辑博客主体

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`remark`, `category_id`, `is_blueprint`, `blueprint_id`, `published_at`, `status`, `seo_url_keyword`, `seo_title`, `draft_title`, `draft_content`, `draft_abstract`, `cover`, `app_cover`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:539` · `BlogDetailsResource`

### PLATFORM-138 · 运营-博客-删除博客

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:654` · `BlogDetailsResource`

### PLATFORM-139 · 运营-博客-编辑是否置顶博客

- 接口声明：`POST /is_top/<int:id_>`
- 输入字段：`is_top`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:676` · `BlogDetailsIsTopResource`

### PLATFORM-140 · 运营-博客-批量创建或更新翻译博客

- 接口声明：`POST /<int:id_>/save-multilingual-content`
- 输入字段：`translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:705` · `BlogMultilingualContentResource`

### PLATFORM-141 · 运营-博客-同步资讯数据

- 接口声明：`PUT /update-information/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/blog.py:819` · `BlogUpdateInformationResource`

### PLATFORM-142 · 经纪商-列表

- 接口声明：`GET `
- 输入字段：`user_id`, `name`, `status`, `page`, `limit`, `export`, `sort_field`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:54` · `BrokerResource`

### PLATFORM-143 · 经纪商-添加经纪商

- 接口声明：`POST `
- 输入字段：`user_id`, `name`, `rate`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:160` · `BrokerResource`

### PLATFORM-144 · 经纪商-编辑经纪商

- 接口声明：`PUT `
- 输入字段：`user_id`, `name`, `rate`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:210` · `BrokerResource`

### PLATFORM-145 · 经纪商-删除经纪商

- 接口声明：`DELETE `
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:246` · `BrokerResource`

### PLATFORM-146 · 经纪商申请-列表

- 接口声明：`GET /application-list`
- 输入字段：`user_id`, `name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:281` · `BrokerApplicationListResource`

### PLATFORM-147 · 经纪商申请-详情

- 接口声明：`GET /application/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:342` · `BrokerApplyDetailResource`

### PLATFORM-148 · 经纪商申请-编辑备注

- 接口声明：`PUT /application/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:359` · `BrokerApplyDetailResource`

### PLATFORM-149 · 经纪商-经纪商授权

- 接口声明：`POST /auth`
- 输入字段：`user_id`, `image_url`, `redirect_url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:389` · `BrokerAuthResource`

### PLATFORM-150 · 经纪商-删除经纪商授权

- 接口声明：`DELETE /auth`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:429` · `BrokerAuthResource`

### PLATFORM-151 · 经纪商-经纪商交易记录

- 接口声明：`GET /records`
- 输入字段：`user_id`, `broker_name`, `start_date`, `end_date`, `page`, `limit`, `report_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:460` · `BrokerRecordsListResource`

### PLATFORM-152 · 经纪商-经纪商返佣记录

- 接口声明：`GET /detail-list`
- 输入字段：`user_id`, `broker_user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:542` · `BrokerReferralDetailsListResource`

### PLATFORM-153 · 经纪商-用户返佣明细记录

- 接口声明：`GET /referral-detail`
- 输入字段：`user_id`, `broker_name`, `report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/broker.py:636` · `BrokerReferralUserDetailsListResource`

### PLATFORM-154 · 用户-商务大使体系-团队列表

- 接口声明：`GET /teams`
- 输入字段：`sort`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:153` · `BusTeamsResource`

### PLATFORM-155 · 用户-商务大使体系-新增团队

- 接口声明：`POST /teams`
- 输入字段：`name`, `leader_id`, `pr_user_ids`, `remark`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:320` · `BusTeamsResource`

### PLATFORM-156 · 用户-商务大使体系-编辑团队

- 接口声明：`PUT /teams`
- 输入字段：`id`, `name`, `leader_id`, `pr_user_ids`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:354` · `BusTeamsResource`

### PLATFORM-157 · 用户-商务大使体系-删除团队

- 接口声明：`DELETE /teams`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:412` · `BusTeamsResource`

### PLATFORM-158 · 用户-商务大使体系-商务列表

- 接口声明：`GET /bus-users`
- 输入字段：`user_id`, `team_id`, `status`, `page`, `limit`, `export`, `sort_col`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:478` · `BusUsersResource`

### PLATFORM-159 · 用户-商务大使体系-新建商务

- 接口声明：`POST /bus-users`
- 输入字段：`user_id`, `team_id`, `leader_rate`, `pr_rates`, `remark`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:671` · `BusUsersResource`

### PLATFORM-160 · 用户-商务大使体系-编辑商务

- 接口声明：`PUT /bus-users`
- 输入字段：`user_id`, `team_id`, `leader_rate`, `pr_rates`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:719` · `BusUsersResource`

### PLATFORM-161 · 用户-商务大使体系-编辑商务状态

- 接口声明：`PATCH /bus-users`
- 输入字段：`user_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:812` · `BusUsersResource`

### PLATFORM-162 · 用户-商务大使体系-商务列表-导出

- 接口声明：`GET /bus-users/export`
- 输入字段：`user_id`, `team_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:867` · `BusUsersExportResource`

### PLATFORM-163 · 用户-商务大使体系-商务大使审核列表

- 接口声明：`GET /bus-ambassador-audits`
- 输入字段：`status`, `type`, `amb_type`, `user_id`, `bus_user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1067` · `BusAmbAuditsResource`

### PLATFORM-164 · 用户-商务大使体系-商务大使审核列表-导出

- 接口声明：`GET /bus-ambassador-audits/export`
- 输入字段：`status`, `type`, `user_id`, `bus_user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1164` · `BusAmbAuditsExportResource`

### PLATFORM-165 · 用户-商务大使体系-商务大使列表-新增总代理商务大使(审核)

- 接口声明：`POST /bus-ambassador-audits/add-tree-root-amb`
- 输入字段：`user_id`, `bus_user_id`, `type`, `rate`, `share_users`, `mobile_num`, `delay_repay_month`, `remark`, `file_keys`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:1194` · `AddTreeRootBusAmbAuditResource`

### PLATFORM-166 · 用户-商务大使体系-商务大使列表-新增商务大使(审核)

- 接口声明：`POST /bus-ambassador-audits/add-amb`
- 输入字段：`user_id`, `bus_user_id`, `type`, `rate`, `share_users`, `mobile_num`, `delay_repay_month`, `remark`, `file_keys`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:1224` · `AddBusAmbAuditResource`

### PLATFORM-167 · 用户-商务大使体系-商务大使详情-修改状态(需审核)

- 接口声明：`POST /bus-ambassador-audits/edit-amb-status`
- 输入字段：`user_id`, `status`, `remark`, `file_keys`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:1321` · `EditBusAmbStatusAuditResource`

### PLATFORM-168 · 用户-商务大使体系-商务大使详情-删除总代理(需审核)

- 接口声明：`POST /bus-ambassador-audits/delete-amb`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1372` · `DeleteBusAmbAuditResource`

### PLATFORM-169 · 用户-商务大使体系-商务大使详情-修改代理类型(需审核)

- 接口声明：`POST /bus-ambassador-audits/edit-type`
- 输入字段：`user_id`, `edit_amb_type`, `remark`, `file_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1426` · `EditBusAmbTypeAuditResource`

### PLATFORM-170 · 用户-商务大使体系-商务大使详情-修改允许扩展子代理(需审核)

- 接口声明：`POST /bus-ambassador-audits/edit-allow-add-child`
- 输入字段：`user_id`, `allow_add_child`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1483` · `EditBusAmbAllowAddChildAuditResource`

### PLATFORM-171 · 用户-商务大使体系-商务大使详情-修改是否允许自返(需审核)

- 接口声明：`POST /bus-ambassador-audits/edit-allow-self-invite`
- 输入字段：`user_id`, `allow_self_invite`, `remark`, `file_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1533` · `EditBusAmbAllowSelfInviteAuditResource`

### PLATFORM-172 · 用户-商务大使体系-商务大使详情-编辑返佣比例(需审核)

- 接口声明：`POST /bus-ambassador-audits/edit-rate`
- 输入字段：`user_id`, `rate`, `share_users`, `remark`, `file_keys`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:1588` · `EditBusAmbRateAuditResource`

### PLATFORM-173 · 用户-商务大使体系-商务大使详情-编辑绑定商务(需审核)

- 接口声明：`POST /bus-ambassador-audits/edit-bus-user`
- 输入字段：`user_id`, `bus_user_id`, `remark`, `file_keys`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:1671` · `EditBusAmbBusUserAuditResource`

### PLATFORM-174 · 用户-商务大使体系-商务大使详情-恢复失效邀请关系(需审核)

- 接口声明：`POST /bus-ambassador-audits/restore-invalid-referral`
- 输入字段：`user_id`, `remark`
- 显式控制：lock_request(with_user=True)
- 代码依据：`app/api/admin/bus_ambassador.py:1727` · `RestoreAmbInvalidReferralAuditResource`

### PLATFORM-175 · 用户-商务大使体系-商务大使详情-编辑预付金还款时间(需审核)

- 接口声明：`POST /bus-ambassador-audits/edit-delay-repay-month`
- 输入字段：`user_id`, `delay_repay_month`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1787` · `EditBusAmbDelayRepayMonthAuditResource`

### PLATFORM-176 · 用户-商务大使体系-商务大使审核-初审

- 接口声明：`POST /bus-ambassador-audits/do-audit`
- 输入字段：`id`, `status`, `comment`, `file_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1849` · `DoBusAmbAuditResource`

### PLATFORM-177 · 用户-商务大使体系-商务大使审核-初审(批处理)

- 接口声明：`POST /bus-ambassador-audits/do-audit-batch`
- 输入字段：`ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1891` · `DoBusAmbAuditBatchResource`

### PLATFORM-178 · 用户-商务大使体系-商务大使审核-复审

- 接口声明：`POST /bus-ambassador-audits/do-review`
- 输入字段：`id`, `status`, `comment`, `file_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:1934` · `DoBusAmbReviewResource`

### PLATFORM-179 · 用户-商务大使体系-商务大使审核-复审(批处理)

- 接口声明：`POST /bus-ambassador-audits/do-review-batch`
- 输入字段：`ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:2012` · `DoBusAmbReviewBatchResource`

### PLATFORM-180 · 用户-商务大使体系-商务大使申请列表

- 接口声明：`GET /applications`
- 输入字段：`status`, `location_code`, `user_id`, `team_id`, `referrer_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:2579` · `BusAmbassadorApplyListResource`

### PLATFORM-181 · 用户-商务大使体系-商务大使申请详情

- 接口声明：`GET /applications/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:2741` · `BusAmbassadorApplyDetailResource`

### PLATFORM-182 · 用户-商务大使体系-商务大使申请审批

- 接口声明：`PUT /applications/<int:id_>`
- 输入字段：`record_id`, `result`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:2762` · `BusAmbassadorApplyDetailResource`

### PLATFORM-183 · 用户-商务大使体系-商务大使申请审批-批量通过

- 接口声明：`POST /applications/batch-audit`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:2846` · `BusAmbassadorApplyBatchAuditResource`

### PLATFORM-184 · 用户-商务大使体系-商务大使申请审批-批量拒绝

- 接口声明：`POST /applications/batch-reject`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:2871` · `BusAmbassadorApplyBatchDeleteResource`

### PLATFORM-185 · 用户-商务大使体系-商务大使列表

- 接口声明：`GET /bus-ambassadors`
- 输入字段：`status`, `user_id`, `bus_user_id`, `type`, `source`, `check_status`, `delete_type`, `allow_self_invite`, `has_bus_user`, `page`, `limit`, `export`, `team_id`, `last_team_id`, `location_code`, `sort_col`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:2994` · `BusAmbassadorsResource`

### PLATFORM-186 · 用户-商务大使体系-商务大使列表-模板下载

- 接口声明：`GET /bus-ambassadors/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3393` · `BusAmbassadorsTemplateResource`

### PLATFORM-187 · 用户-商务大使体系-商务大使列表-模板上传

- 接口声明：`POST /bus-ambassadors/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3402` · `BusAmbassadorsTemplateResource`

### PLATFORM-188 · 用户-商务大使体系-商务大使列表-导出

- 接口声明：`GET /bus-ambassadors/export`
- 输入字段：`status`, `user_id`, `bus_user_id`, `type`, `source`, `check_status`, `delete_type`, `allow_self_invite`, `team_id`, `last_team_id`, `location_code`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3470` · `BusAmbassadorsExportResource`

### PLATFORM-189 · 用户-商务大使体系-商务大使详情-修改团队返佣系数

- 接口声明：`POST /bus-ambassadors/team-rate`
- 输入字段：`user_id`, `team_rate`, `remark`, `file_keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3496` · `BusAmbassadorTeamRateResource`

### PLATFORM-190 · 用户-商务大使体系-商务大使详情-新增备注

- 接口声明：`POST /bus-ambassadors/remark`
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3536` · `BusAmbassadorRemarkResource`

### PLATFORM-191 · 用户-商务大使体系-商务大使详情

- 接口声明：`GET /bus-ambassadors/detail`
- 输入字段：`user_id`, `remark_page`, `remark_limit`, `audit_page`, `audit_limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3570` · `BusAmbassadorDetailResource`

### PLATFORM-192 · 用户-商务大使体系-商务大使预付金申请列表

- 接口声明：`GET /loan-apply`
- 输入字段：`status`, `bus_amb_id`, `bus_user_id`, `loan_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3759` · `BusAmbLoanApplyResource`

### PLATFORM-193 · 用户-商务大使体系-商务大使预付金申请-新增

- 接口声明：`POST /loan-apply`
- 输入字段：`bus_amb_id`, `amount`, `reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3886` · `BusAmbLoanApplyResource`

### PLATFORM-194 · 用户-商务大使体系-商务大使预付金申请-审核

- 接口声明：`PATCH /loan-apply`
- 输入字段：`apply_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:3941` · `BusAmbLoanApplyResource`

### PLATFORM-195 · 用户-商务大使体系-商务大使预付金申请列表-导出

- 接口声明：`GET /loan-apply/export`
- 输入字段：`status`, `bus_amb_id`, `bus_user_id`, `loan_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4027` · `BusAmbLoanApplyExportResource`

### PLATFORM-196 · 用户-商务大使体系-商务大使预付金-还款记录

- 接口声明：`GET /repay-history`
- 输入字段：`status`, `bus_amb_id`, `bus_user_id`, `loan_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4047` · `BusAmbRepayHistoryResource`

### PLATFORM-197 · 用户-商务大使体系-商务大使预付金申请列表-查看还款详情

- 接口声明：`GET /one-repay-history`
- 输入字段：`loan_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4123` · `BusAmbOneRepayHistoryResource`

### PLATFORM-198 · 用户-商务大使体系-权限设置

- 接口声明：`GET /permission`
- 输入字段：`keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4138` · `BusAmbPermissionResource`

### PLATFORM-199 · 用户-商务大使体系-权限设置-添加

- 接口声明：`POST /permission`
- 输入字段：`user_keyword`, `limit_list`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4198` · `BusAmbPermissionResource`

### PLATFORM-200 · 用户-商务大使体系-权限设置-编辑

- 接口声明：`PUT /permission`
- 输入字段：`user_id`, `limit_list`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4240` · `BusAmbPermissionResource`

### PLATFORM-201 · 用户-商务大使体系-权限设置-删除

- 接口声明：`DELETE /permission`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4270` · `BusAmbPermissionResource`

### PLATFORM-202 · 用户-商务大使体系-变更记录

- 接口声明：`GET /change-log`
- 输入字段：`start_time`, `end_time`, `biz_id`, `admin_user_id`, `application_id`, `change_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4302` · `BusRelationChangeLogResource`

### PLATFORM-203 · 用户-商务大使体系-子代理列表

- 接口声明：`GET /tree-ambassadors`
- 输入字段：`status`, `user_id`, `parent_id`, `root_id`, `bus_user_id`, `team_id`, `tree_height`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4402` · `TreeAmbassadorsResource`

### PLATFORM-204 · 用户-商务大使体系-子代理编辑

- 接口声明：`PUT /tree-ambassadors`
- 输入字段：`user_id`, `rate`, `allow_add_child`, `admin_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4585` · `TreeAmbassadorsResource`

### PLATFORM-205 · 用户-商务大使体系-子代理删除

- 接口声明：`DELETE /tree-ambassadors`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4614` · `TreeAmbassadorsResource`

### PLATFORM-206 · 用户-商务大使体系-子代理列表-导出

- 接口声明：`GET /tree-ambassadors/export`
- 输入字段：`status`, `user_id`, `parent_id`, `root_id`, `bus_user_id`, `team_id`, `tree_height`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/bus_ambassador.py:4633` · `TreeAmbassadorsExportResource`

### PLATFORM-207 · Redis队列

- 接口声明：`GET /redis-queues`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/celery.py:18` · `CeleryQueuesResource`

### PLATFORM-208 · Redis队列详情

- 接口声明：`GET /redis-queues/<queue>`
- 输入字段：`limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/celery.py:33` · `CeleryQueueResource`

### PLATFORM-209 · 删除Redis队列

- 接口声明：`DELETE /redis-queues/<queue>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/celery.py:64` · `CeleryQueueResource`

### PLATFORM-210 · 用户-CoinEx合伙人-职位列表

- 接口声明：`GET /position`
- 输入字段：`lang`, `country`, `work_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coinexpartner.py:22` · `PartnerPositionResource`

### PLATFORM-211 · 用户-CoinEx合伙人-添加职位

- 接口声明：`POST /position`
- 输入字段：`name`, `lang`, `iso3_codes`, `work_type`, `deliver_mail`, `description`, `requirement`, `welfare`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coinexpartner.py:83` · `PartnerPositionResource`

### PLATFORM-212 · 用户-CoinEx合伙人-编辑职位

- 接口声明：`PUT /position`
- 输入字段：`id`, `name`, `lang`, `iso3_codes`, `work_type`, `deliver_mail`, `description`, `requirement`, `welfare`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coinexpartner.py:136` · `PartnerPositionResource`

### PLATFORM-213 · 用户-CoinEx合伙人-删除职位

- 接口声明：`DELETE /position`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coinexpartner.py:211` · `PartnerPositionResource`

### PLATFORM-214 · 用户-CoinEx合伙人-职位上移

- 接口声明：`PUT /position/<int:id_>/sort_id`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coinexpartner.py:240` · `PartnerPositionSortIDResource`

### PLATFORM-215 · 合约-跟单交易-获取全局配置

- 接口声明：`GET /settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:38` · `CopyTradingSettingsResource`

### PLATFORM-216 · 合约-跟单交易-市场配置列表

- 接口声明：`GET /markets`
- 输入字段：`market`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:57` · `CopyTradingMarketsResource`

### PLATFORM-217 · 合约-跟单交易-交易员列表 

- 接口声明：`GET /trader-list`
- 输入字段：`user_id`, `trader_id`, `nickname`, `status`, `is_manual_add`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:133` · `TraderListResource`

### PLATFORM-218 · 合约-跟单交易-交易员-获取开通资格信息

- 接口声明：`GET /trader-apply-condition`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:298` · `TraderApplicationConditionResource`

### PLATFORM-219 · 合约-跟单交易-带单列表 

- 接口声明：`GET /trade-history-list`
- 输入字段：`id`, `user_id`, `sub_user_id`, `trader_id`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:322` · `TradeHistoryListResource`

### PLATFORM-220 · 合约-跟单交易-跟单列表 

- 接口声明：`GET /follow-history-list`
- 输入字段：`trader_user_id`, `trader_id`, `user_id`, `sub_user_id`, `id`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:398` · `FollowHistoryListResource`

### PLATFORM-221 · 合约-跟单交易-划转记录列表 

- 接口声明：`GET /transfer-history-list`
- 输入字段：`main_user_id`, `history_id`, `from_user_id`, `to_user_id`, `status`, `type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:505` · `TransferHistoryListResource`

### PLATFORM-222 · 合约-跟单交易-分润记录列表 

- 接口声明：`GET /profit-share-list`
- 输入字段：`follower_user_id`, `trader_user_id`, `follow_history_id`, `trader_history_id`, `transfer_history_id`, `status`, `profit_share_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:564` · `ProfitShareListResource`

### PLATFORM-223 · 合约-跟单交易-交易员仓位变化列表 

- 接口声明：`GET /trader-position-change-record`
- 输入字段：`id`, `trader_user_id`, `trader_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:628` · `TraderPositionChangeRecordResource`

### PLATFORM-224 · 合约-跟单交易-跟单员订单操作列表 

- 接口声明：`GET /follower-order-operation-list`
- 输入字段：`user_id`, `sub_user_id`, `trader_user_id`, `change_record_id`, `start_time`, `end_time`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/copy_trading.py:672` · `FollowerOrderOperationListResource`

### PLATFORM-225 · 运营-卡劵中心-卡劵管理

- 接口声明：`GET /list`
- 输入字段：`coupon_type`, `coupon_id`, `coupon_status`, `coupon_denomination`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:114` · `CouponListResource`

### PLATFORM-226 · 运营-卡劵中心-创建卡劵

- 接口声明：`POST /list`
- 输入字段：`coupon_type`, `value`, `value_type`, `receivable_days`, `usable_days`, `activation_days`, `remark`, `extra`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:212` · `CouponListResource`

### PLATFORM-227 · 运营-卡劵中心-编辑卡劵

- 接口声明：`PUT /<int:coupon_id>`
- 输入字段：`coupon_type`, `value_type`, `value`, `receivable_days`, `usable_days`, `activation_days`, `remark`, `extra`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:303` · `CouponDetailResource`

### PLATFORM-228 · 运营-卡劵中心-修改卡劵状态

- 接口声明：`POST /<int:coupon_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:372` · `CouponDetailResource`

### PLATFORM-229 · 运营-卡劵中心-卡劵发放管理

- 接口声明：`GET /apply/list`
- 输入字段：`apply_id`, `title`, `coupon_type`, `exclude_coupon_type`, `status`, `page`, `limit`, `dynamic_user_type`, `sort_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:521` · `CouponApplyListResource`

### PLATFORM-230 · 运营-卡劵中心-创建卡劵发放

- 接口声明：`POST /apply/list`
- 输入字段：`title`, `business_party`, `send_at`, `coupon_id`, `total_count`, `send_user_type`, `dynamic_user_type`, `code`, `invitees_limit`, `groups`, `user_group_condition`, `source`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:664` · `CouponApplyListResource`

### PLATFORM-231 · 运营-卡劵中心-修改卡劵发放

- 接口声明：`PUT /apply/<int:apply_id>`
- 输入字段：`title`, `business_party`, `send_at`, `coupon_id`, `total_count`, `send_user_type`, `dynamic_user_type`, `groups`, `user_group_condition`, `code`, `invitees_limit`, `source`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:766` · `CouponApplyDetailResource`

### PLATFORM-232 · 运营-卡劵中心-更改卡劵申请状态

- 接口声明：`POST /apply/<int:apply_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:855` · `CouponApplyDetailResource`

### PLATFORM-233 · 运营-卡劵中心-审核卡劵

- 接口声明：`POST /apply/<int:apply_id>/audit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/coupon.py:884` · `CouponApplyAuditResource`

### PLATFORM-234 · 运营-卡劵中心-批量审核卡劵

- 接口声明：`POST /apply/batch/verify`
- 输入字段：`apply_ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/coupon.py:922` · `CouponApplyBatchVerifyResource`

### PLATFORM-235 · 运营-卡劵中心-卡券资金预警配置详情

- 接口声明：`GET /balance/warn`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:999` · `CouponBalanceWarnResource`

### PLATFORM-236 · 运营-卡劵中心-修改卡券资金预警配置

- 接口声明：`POST /balance/warn`
- 输入字段：`user_emails`, `asset`, `amount`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:1019` · `CouponBalanceWarnResource`

### PLATFORM-237 · 运营-卡劵中心-卡券发放用户下载

- 接口声明：`GET /apply/<int:id_>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:1066` · `CouponApplyUserResource`

### PLATFORM-238 · 卡劵中心-卡劵统计-使用详情

- 接口声明：`GET /usage`
- 输入字段：`coupon_apply_id`, `distribution_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:1263` · `CouponApplyUsageResource`

### PLATFORM-239 · 卡劵中心-手续费返现券-使用详情

- 接口声明：`GET /usage/cashback`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:1446` · `CouponUsageCashbackResource`

### PLATFORM-240 · 卡劵中心-合约跟单体验金-用户使用记录

- 接口声明：`GET /usage/copy_trading_experience_fee`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:1612` · `CouponUsageCtExperienceFeeResource`

### PLATFORM-241 · 卡劵中心-卡劵统计数据

- 接口声明：`GET /statistics`
- 输入字段：`coupon_type`, `title`, `coupon_apply_id`, `origin_type`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:1730` · `CouponStatisticsListResource`

### PLATFORM-242 · 卡劵中心-卡劵统计-用户交易统计

- 接口声明：`GET /user/trade`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:1992` · `CouponUserTradeStatisticsResponse`

### PLATFORM-243 · 卡劵中心-合约跟单体验金-用户交易统计

- 接口声明：`GET /user/trade/copy_trading_experience_fee`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2169` · `CouponUserTradeCtExperienceFeeStatisticsResponse`

### PLATFORM-244 · 卡劵中心-手续费返现券-用户交易统计

- 接口声明：`GET /user/trade/cashback-fee`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2279` · `CouponUserTradeCashBackFeeResponse`

### PLATFORM-245 · 卡劵中心-用户组配置

- 接口声明：`GET /user-groups`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2355` · `CouponUserGroupConfigResource`

### PLATFORM-246 · 交易赠金券-卡劵使用记录

- 接口声明：`GET /trading-gift/using`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2390` · `CouponTradingGiftUsingResource`

### PLATFORM-247 · 交易赠金券-用户转化

- 接口声明：`GET /trading-gift/trade`
- 输入字段：`coupon_apply_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2523` · `CouponTradingGiftTradeResponse`

### PLATFORM-248 · 理财加息券-卡劵使用记录

- 接口声明：`GET /investment-inc-rate/using`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2636` · `InvestmentIncRateCouponUsingResource`

### PLATFORM-249 · 理财加息券-卡劵转化统计

- 接口声明：`GET /investment-inc-rate/statistics`
- 输入字段：`coupon_apply_id`, `source`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2760` · `InvestmentIncRateCouponStatisticsResource`

### PLATFORM-250 · 合约补贴金-卡劵使用记录

- 接口声明：`GET /perpetual-subsidy/using`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:2864` · `PerpetualSubsidyCouponUsingResource`

### PLATFORM-251 · vip升级券-卡劵使用记录

- 接口声明：`GET /vip-upgrade/using`
- 输入字段：`coupon_apply_id`, `user_id`, `status`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3004` · `VipUpgradeCouponUsingResource`

### PLATFORM-252 · 活动-卡券申请查询

- 接口声明：`GET /apply/query`
- 输入字段：`end_at`, `start_at`, `status`, `dynamic_user_type`, `source`, `check_pool`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3125` · `CouponApplyQueryResponse`

### PLATFORM-253 · 卡券-智能投放-智能投放列表

- 接口声明：`GET /distribution`
- 输入字段：`id`, `name`, `coupon_type`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3210` · `CouponDistributionResponse`

### PLATFORM-254 · 卡券-智能投放-创建智能投放

- 接口声明：`POST /distribution`
- 输入字段：`name`, `business_party`, `start_at`, `cycle_type`, `cycle_count`, `send_type`, `once_count`, `once_limit`, `groups`, `remark`, `coupon_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3340` · `CouponDistributionResponse`

### PLATFORM-255 · 卡券-智能投放-修改投放规则

- 接口声明：`PUT /distribution/<int:distribution_id>`
- 输入字段：`name`, `business_party`, `start_at`, `cycle_type`, `cycle_count`, `send_type`, `once_count`, `once_limit`, `groups`, `remark`, `coupon_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3382` · `CouponDistributionDetailResponse`

### PLATFORM-256 · 卡券-智能投放-更改智能投放状态

- 接口声明：`POST /distribution/<int:distribution_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3430` · `CouponDistributionDetailResponse`

### PLATFORM-257 · 卡券-智能投放-禁用智能投放

- 接口声明：`PUT /distribution/<int:distribution_id>/forbidden`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3490` · `CouponDistributionForbiddenResource`

### PLATFORM-258 · 卡券-智能投放-审核智能投放

- 接口声明：`POST /distribution/<int:distribution_id>/verify`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/coupon.py:3510` · `CouponDistributionVerifyResource`

### PLATFORM-259 · 卡券-智能投放-智能投放发放统计

- 接口声明：`GET /distribution/statistics`
- 输入字段：`coupon_type`, `distribution_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3539` · `CouponDistributionStatisticsResource`

### PLATFORM-260 · 运营-卡劵中心-智能投放用户下载

- 接口声明：`GET /distribution/<int:id_>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3655` · `CouponDistributionUserResource`

### PLATFORM-261 · 用户详情-卡券记录

- 接口声明：`GET /user-coupons`
- 输入字段：`user_id`, `coupon_type`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3698` · `UserCouponListResource`

### PLATFORM-262 · 卡劵中心-卡券成本统计

- 接口声明：`GET /expenditure/statistics`
- 输入字段：`business_party`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/coupon.py:3835` · `CouponExpenditureStatisticsResource`

### PLATFORM-263 · 第三方资产托管-托管用户充值记录列表

- 接口声明：`GET /user-deposit`
- 输入字段：`asset`, `platform`, `status`, `user`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/custody.py:21` · `CustodyUserDepositResource`

### PLATFORM-264 · 第三方资产托管-托管用户提现记录列表

- 接口声明：`GET /user-withdraw`
- 输入字段：`asset`, `platform`, `status`, `user`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/custody.py:121` · `CustodyUserWithdrawResource`

### PLATFORM-265 · 第三方资产托管-托管结算清单列表

- 接口声明：`GET /settlement`
- 输入字段：`platform`, `platform_settlement_id`, `status`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/custody.py:208` · `CustodySettlementResource`

### PLATFORM-266 · 第三方资产托管-托管结算清单用户列表

- 接口声明：`GET /settlement-users`
- 输入字段：`settlement_id`, `asset`, `user`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/custody.py:292` · `CustodySettlementUsersResource`

### PLATFORM-267 · 第三方资产托管-平台充值记录列表

- 接口声明：`GET /platform-deposit`
- 输入字段：`asset`, `platform`, `status`, `settlement_id`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/custody.py:446` · `CustodyPlatformDepositResource`

### PLATFORM-268 · 第三方资产托管-平台提现记录列表

- 接口声明：`GET /platform-withdraw`
- 输入字段：`asset`, `platform`, `status`, `settlement_id`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/custody.py:510` · `CustodyPlatformWithdrawResource`

### PLATFORM-269 · 紧急联系人-列表

- 接口声明：`GET `
- 输入字段：`user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/emergency_contact.py:14` · `EmergencyContactResource`

### PLATFORM-270 · 权益中心-获取全局配置

- 接口声明：`GET /settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:372` · `EquitySettingsResource`

### PLATFORM-271 · 权益中心-修改全局配置

- 接口声明：`POST /settings`
- 输入字段：`settings`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:380` · `EquitySettingsResource`

### PLATFORM-272 · 权益中心-编辑全局配置

- 接口声明：`PUT /settings/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:395` · `EquitySettingsManagementResource`

### PLATFORM-273 · 权益中心-重置全局配置

- 接口声明：`DELETE /settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:411` · `EquitySettingsManagementResource`

### PLATFORM-274 · 权益中心-编辑风控配置

- 接口声明：`PUT /risk-settings/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:429` · `EquityRiskSettingsManagementResource`

### PLATFORM-275 · 权益中心-重置风控配置

- 接口声明：`DELETE /risk-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:460` · `EquityRiskSettingsManagementResource`

### PLATFORM-276 · 权益中心-权益配置与监控-风控事件列表

- 接口声明：`GET /risk-event`
- 输入字段：`status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:477` · `EquityRiskEventResource`

### PLATFORM-277 · 权益中心-权益配置与监控-风控事件审核

- 接口声明：`POST /risk-event`
- 输入字段：`id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:514` · `EquityRiskEventResource`

### PLATFORM-278 · 权益中心-权益配置与监控-风控用户列表

- 接口声明：`GET /risk-users`
- 输入字段：`start_time`, `end_time`, `status`, `user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:573` · `EquityRiskUsersResource`

### PLATFORM-279 · 权益中心-权益配置与监控-风控用户审核

- 接口声明：`POST /risk-users`
- 输入字段：`id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:646` · `EquityRiskUsersResource`

### PLATFORM-280 · 权益中心-权益配置与监控-风控用户批量审核

- 接口声明：`PUT /risk-users`
- 输入字段：`ids`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:681` · `EquityRiskUsersResource`

### PLATFORM-281 · 权益中心-权益模板详情

- 接口声明：`GET /detail`
- 输入字段：`equity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:721` · `EquityDetailResource`

### PLATFORM-282 · 权益中心-返现权益列表

- 接口声明：`GET /cashback/list`
- 输入字段：`equity_id`, `status`, `cost_amount`, `effective_days`, `cashback_scope`, `cashback_asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:762` · `CashbackEquityListResource`

### PLATFORM-283 · 权益中心-返现权益-创建

- 接口声明：`POST /cashback/list`
- 输入字段：`cashback_scope`, `cashback_asset`, `cashback_ratio`, `cost_asset`, `cost_amount`, `effective_days`, `remark`
- 显式控制：lock_request()
- 代码依据：`app/api/admin/equity_center.py:832` · `CashbackEquityListResource`

### PLATFORM-284 · 权益中心-返现权益-禁用 / 启用

- 接口声明：`PATCH /cashback/list`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:889` · `CashbackEquityListResource`

### PLATFORM-285 · 权益中心-权益发放-返现权益发放列表

- 接口声明：`GET /cashback/user-equity`
- 输入字段：`user_id`, `status`, `equity_id`, `business_type`, `source_value`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1093` · `UserCashbackEquityListResource`

### PLATFORM-286 · 权益中心-权益发放-返现权益发放明细

- 接口声明：`GET /cashback/user-equity-history`
- 输入字段：`user_equity_id`, `apply_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1158` · `UserCashbackEquityHistoryResource`

### PLATFORM-287 · 权益中心-理财加息权益列表-每日加息明细

- 接口声明：`GET /invest-increase/daily-history`
- 输入字段：`user_equity_id`, `apply_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1293` · `InvestIncreaseDailyHistoryResource`

### PLATFORM-288 · 权益中心-理财加息权益列表

- 接口声明：`GET /invest-increase/list`
- 输入字段：`equity_id`, `status`, `asset`, `increase_rate`, `principal_amount_limit`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1359` · `InvestIncreaseEquityListResource`

### PLATFORM-289 · 权益中心-理财加息权益-创建

- 接口声明：`POST /invest-increase/list`
- 输入字段：`increase_rate`, `principal_amount_limit`, `assets`, `activation_days`, `usable_days`, `total_interest`, `remark`
- 显式控制：lock_request()
- 代码依据：`app/api/admin/equity_center.py:1431` · `InvestIncreaseEquityListResource`

### PLATFORM-290 · 权益中心-理财加息权益-禁用 / 启用

- 接口声明：`PATCH /invest-increase/list`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1493` · `InvestIncreaseEquityListResource`

### PLATFORM-291 · 权益中心-权益发放-理财加息权益发放列表

- 接口声明：`GET /invest-increase/user-equity`
- 输入字段：`user_id`, `status`, `equity_id`, `business_type`, `source_value`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1622` · `InvestIncreaseEquityUserListResource`

### PLATFORM-292 · 权益中心-相关记录

- 接口声明：`GET /relation-history`
- 输入字段：`history_type`, `start`, `end`, `row_id`, `user_id`, `equity_id`, `main_user_id`, `user_equity_id`, `trade_business_id`, `settle_his_id`, `settlement_status`, `asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1740` · `EquityRelationHisResource`

### PLATFORM-293 · 权益中心-合约体验金权益-列表

- 接口声明：`GET /perpetual-trial/list`
- 输入字段：`equity_id`, `status`, `market`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:1868` · `PerpetualTrialListResource`

### PLATFORM-294 · 权益中心-合约体验金权益-创建

- 接口声明：`POST /perpetual-trial/list`
- 输入字段：`cost_asset`, `cost_amount`, `allowed_markets`, `effective_days`, `position_hours`, `realized_profit_threshold`, `max_leverage`, `max_open_position_count`, `max_profit_rate`, `withdrawable_days`, `withdrawable_params`, `remark`
- 显式控制：lock_request()
- 代码依据：`app/api/admin/equity_center.py:1961` · `PerpetualTrialListResource`

### PLATFORM-295 · 权益中心-理财加息权益-禁用 / 启用

- 接口声明：`PATCH /perpetual-trial/list`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:2033` · `PerpetualTrialListResource`

### PLATFORM-296 · 权益中心-合约体验金权益-用户权益列表

- 接口声明：`GET /perpetual-trial/user-equity`
- 输入字段：`user_id`, `status`, `equity_id`, `business_type`, `source_value`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:2169` · `PerpetualTrialUserEquityResource`

### PLATFORM-297 · 权益中心-合约体验金权益-数据追踪详情

- 接口声明：`GET /perpetual-trial/trace-detail`
- 输入字段：`user_equity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:2795` · `PerpetualTrialTraceDetailResource`

### PLATFORM-298 · 权益中心-权益发放列表

- 接口声明：`GET /send-apply/list`
- 输入字段：`equity_type`, `apply_id`, `equity_id`, `title`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3041` · `EquitySendApplyListResource`

### PLATFORM-299 · 权益中心-权益发放-创建

- 接口声明：`POST /send-apply/list`
- 输入字段：`title`, `business_party`, `send_type`, `send_at`, `total_send_count`, `equity_type`, `equity_id`, `airdrop_asset`, `airdrop_amount`, `user_selection_type`, `manual_user_list`, `groups`, `message_templates`, `notice_channel_modes`, `remark`
- 显式控制：lock_request()
- 代码依据：`app/api/admin/equity_center.py:3166` · `EquitySendApplyListResource`

### PLATFORM-300 · 权益中心-权益发放-权益发放详情

- 接口声明：`GET /send-apply/<int:apply_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3330` · `EquitySendApplyDetailResource`

### PLATFORM-301 · 权益中心-权益发放-修改发放

- 接口声明：`PUT /send-apply/<int:apply_id>`
- 输入字段：`title`, `business_party`, `send_type`, `send_at`, `equity_type`, `equity_id`, `airdrop_asset`, `airdrop_amount`, `total_send_count`, `user_selection_type`, `manual_user_list`, `groups`, `remark`, `resubmit_wait_audit`, `message_templates`, `notice_channel_modes`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3431` · `EquitySendApplyDetailResource`

### PLATFORM-302 · 运营-权益发放-更改权益发放状态（拒绝、禁用）

- 接口声明：`PATCH /send-apply/<int:apply_id>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3555` · `EquitySendApplyDetailResource`

### PLATFORM-303 · 运营-权益发放-批量审核权益发放（通过/拒绝）

- 接口声明：`POST /send-apply/batch-audit`
- 输入字段：`ids`, `status`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/equity_center.py:3598` · `EquitySendApplyBatchAuditResource`

### PLATFORM-304 · 运营-权益发放-审核权益发放

- 接口声明：`POST /send-apply/<int:apply_id>/audit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/equity_center.py:3679` · `EquitySendApplyAuditResource`

### PLATFORM-305 · 运营-权益发放-权益发放用户下载

- 接口声明：`GET /send-apply/<int:apply_id>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3716` · `EquitySendApplyUserResource`

### PLATFORM-306 · 权益中心-返现权益-其他业务嵌入

- 接口声明：`GET /cashback/embed`
- 输入字段：`equity_type`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3752` · `EquityCashbackEmbedResource`

### PLATFORM-307 · 权益中心-权益监控-发奖账户每日消耗统计列表

- 接口声明：`GET /daily-consumption`
- 输入字段：`issue_asset`, `issue_start_date`, `issue_end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3794` · `EquityDailyConsumptionResource`

### PLATFORM-308 · 权益中心-权益监控-发奖消耗明细列表

- 接口声明：`GET /daily-consumption-detail`
- 输入字段：`consumption_id`, `issue_type`, `issue_asset`, `business_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3835` · `EquityDailyConsumptionDetailResource`

### PLATFORM-309 · 权益中心-合约体验金-数据监控

- 接口声明：`GET /perpetual-trial/data-monitor`
- 输入字段：`period`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:3912` · `PerpetualTrialMonitorResource`

### PLATFORM-310 · 权益中心-返现权益统计报表

- 接口声明：`GET /cashback/stat-report-list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:4083` · `CashbackStatReportListResource`

### PLATFORM-311 · 权益中心-活期理财加息权益统计报表

- 接口声明：`GET /invest-increase/stat-report-list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:4122` · `InvestIncreaseStatReportListResource`

### PLATFORM-312 · 权益中心-合约体验金权益统计报表

- 接口声明：`GET /perpetual-trial/stat-report-list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:4183` · `PerpetualTrialStatReportListResource`

### PLATFORM-313 · 权益中心-成本统计

- 接口声明：`GET /cost`
- 输入字段：`business_party`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/equity_center.py:4215` · `EquityCostResource`

### PLATFORM-314 · Api 限频列表

- 接口声明：`GET /config`
- 输入字段：`search_keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:24` · `UserApiLimitConfigResource`

### PLATFORM-315 · 创建 Api 限频配置

- 接口声明：`POST /config`
- 输入字段：`user_id`, `group`, `limit_count`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:93` · `UserApiLimitConfigResource`

### PLATFORM-316 · 修改 Api 限频配置

- 接口声明：`PUT /config/<int:id_>`
- 输入字段：`limit_count`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:136` · `EditUserApiLimitConfigResource`

### PLATFORM-317 · 删除 Api 限频配置

- 接口声明：`DELETE /config/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:175` · `EditUserApiLimitConfigResource`

### PLATFORM-318 · 长周期特殊限频配置

- 接口声明：`GET /long-period`
- 输入字段：`search_keyword`, `trade_type`, `api_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:223` · `LangPeriodResource`

### PLATFORM-319 · 创建长周期限频配置

- 接口声明：`POST /long-period`
- 输入字段：`user_id`, `group`, `long_period_hour`, `limit_total_count`, `low_rate_second`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:286` · `LangPeriodResource`

### PLATFORM-320 · 修改 长周期 限频配置

- 接口声明：`PUT /long-period/<int:id_>`
- 输入字段：`long_period_hour`, `limit_total_count`, `low_rate_second`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:330` · `EditLongPeriodResource`

### PLATFORM-321 · 删除 长周期 限频配置

- 接口声明：`DELETE /long-period/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/frequency_limit.py:355` · `EditLongPeriodResource`

### PLATFORM-322 · 运营-运营管理-搜索栏限时活动-搜索栏限时活动列表

- 接口声明：`GET /limited-time-activity/list`
- 输入字段：`name`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:67` · `LimitedTimeActivityListResource`

### PLATFORM-323 · 运营-运营管理-搜索栏限时活动-搜索栏限时活动详情

- 接口声明：`GET /limited-time-activity`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:126` · `LimitedTimeActivityResource`

### PLATFORM-324 · 运营-运营管理-搜索栏限时活动-创建/修改搜索栏限时活动

- 接口声明：`POST /limited-time-activity`
- 输入字段：`id`, `platform`, `name`, `contents`, `start_at`, `end_at`, `web_link_id`, `app_link_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:162` · `LimitedTimeActivityResource`

### PLATFORM-325 · 运营-运营管理-搜索栏限时活动-删除搜索栏限时活动

- 接口声明：`DELETE /limited-time-activity`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:286` · `LimitedTimeActivityResource`

### PLATFORM-326 · 运营-运营管理-搜索栏限时活动-搜索栏限时活动模版

- 接口声明：`GET /limited-time-activity/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:319` · `BatchUploadTemplateResource`

### PLATFORM-327 · 运营-运营管理-搜索栏相关功能配置-列表

- 接口声明：`GET /related-function/list`
- 输入字段：`name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:403` · `RelatedFunctionListResource`

### PLATFORM-328 · 运营-运营管理-搜索栏相关功能配置-详情

- 接口声明：`GET /related-function`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:476` · `RelatedFunctionResource`

### PLATFORM-329 · 运营-运营管理-搜索栏相关功能配置-创建/修改

- 接口声明：`POST /related-function`
- 输入字段：`id`, `platform`, `name`, `status`, `icon`, `dark_icon`, `contents`, `web_link_id`, `app_link_id`, `sort_weight`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:501` · `RelatedFunctionResource`

### PLATFORM-330 · 运营-运营管理-搜索栏相关功能配置-删除

- 接口声明：`DELETE /related-function`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:609` · `RelatedFunctionResource`

### PLATFORM-331 · 运营-运营管理-搜索栏相关功能配置-状态切换

- 接口声明：`PUT /related-function/status`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:630` · `RelatedFunctionStatusResource`

### PLATFORM-332 · 运营-运营管理-搜索栏相关功能配置-模板下载

- 接口声明：`GET /related-function/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:659` · `RelatedFunctionTemplateResource`

### PLATFORM-333 · 运营-运营管理-搜索栏相关功能配置-批量导入

- 接口声明：`POST /related-function/import`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/global_search.py:686` · `RelatedFunctionImportResource`

### PLATFORM-334 · 资讯-推送PUSH

- 接口声明：`POST /push`
- 输入字段：`id`, `name`, `push_type`, `push_time`, `remark`, `ttl`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/information.py:61` · `PushResource`

### PLATFORM-335 · 资讯-翻译

- 接口声明：`POST /translate`
- 输入字段：`source_lang`, `target_langs`, `title`, `abstract`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/information.py:141` · `TranslateResource`

### PLATFORM-336 · KYT - 提现地址风险筛查记录-列表

- 接口声明：`GET /withdrawal-pre-screening`
- 输入字段：`user_id`, `asset`, `chain`, `address`, `category_id`, `begin_at`, `end_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:42` · `WithdrawalPreScreeningResource`

### PLATFORM-337 · KYT - 提现地址风险筛查记录-备注

- 接口声明：`PATCH /withdrawal-pre-screening/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:127` · `WithdrawalPreScreeningDetailResource`

### PLATFORM-338 · Web KYT 评估 - 查看列表

- 接口声明：`GET /deposit-sender-risk-assessments`
- 输入字段：`ids`, `deposit_id`, `chain`, `assess_object`, `status`, `assessor`, `audit_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:155` · `DepositSenderRiskAssessmentsResource`

### PLATFORM-339 · 风控-反洗钱系统-提现KYT风险评估

- 接口声明：`GET /withdrawal-risk-assessments`
- 输入字段：`ids`, `withdrawal_id`, `chain`, `address`, `status`, `assessor`, `reason`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:296` · `WithdrawalRiskAssessmentsResource`

### PLATFORM-340 · KYT - 充值风险评估白名单用户-列表

- 接口声明：`GET /whitelist-user`
- 输入字段：`user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:355` · `WhiteListUsersResource`

### PLATFORM-341 · KYT - 充值风险评估白名单用户-添加

- 接口声明：`POST /whitelist-user`
- 输入字段：`user_ids`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:388` · `WhiteListUsersResource`

### PLATFORM-342 · KYT - 充值风险评估白名单用户-删除

- 接口声明：`DELETE /whitelist-user/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:428` · `WhiteListUserResource`

### PLATFORM-343 · KYT - 制裁地区白名单-列表

- 接口声明：`GET /sanctioned-jurisdiction`
- 输入字段：`name`, `direction`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:456` · `SanctionedJurisdictionResource`

### PLATFORM-344 · KYT - 制裁地区白名单-添加

- 接口声明：`POST /sanctioned-jurisdiction`
- 输入字段：`name`, `remark`, `direction`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:494` · `SanctionedJurisdictionResource`

### PLATFORM-345 · KYT - 制裁地区白名单-删除

- 接口声明：`DELETE /sanctioned-jurisdiction/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:533` · `SanctionedJurisdictionDetailResource`

### PLATFORM-346 · KYT 充值风险评估白名单 from 地址 - 查看列表

- 接口声明：`GET /deposit-sender-risk-assessment-whitelist`
- 输入字段：`chain`, `address`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:562` · `DepositSenderRiskAssessmentWhitelistResource`

### PLATFORM-347 · KYT 充值风险评估白名单 from 地址 - 添加

- 接口声明：`POST /deposit-sender-risk-assessment-whitelist`
- 输入字段：`chain`, `addresses`, `reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:600` · `DepositSenderRiskAssessmentWhitelistResource`

### PLATFORM-348 · KYT 充值风险评估白名单 from 地址 - 删除单条

- 接口声明：`DELETE /deposit-sender-risk-assessment-whitelist/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:691` · `DepositSenderRiskAssessmentWhitelistItemResource`

### PLATFORM-349 · 充提KYT白名单-提现地址评估白名单-列表

- 接口声明：`GET /withdrawal-address-risk-assessment-whitelist`
- 输入字段：`chain`, `address`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:718` · `WithdrawalAddressRiskAssessmentWhitelistResource`

### PLATFORM-350 · 充提KYT白名单-提现地址评估白名单-添加

- 接口声明：`POST /withdrawal-address-risk-assessment-whitelist`
- 输入字段：`chain`, `addresses`, `reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:762` · `WithdrawalAddressRiskAssessmentWhitelistResource`

### PLATFORM-351 · 充提KYT白名单-提现地址评估白名单-删除

- 接口声明：`DELETE /withdrawal-address-risk-assessment-whitelist/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:837` · `WithdrawalAddressRiskAssessmentWhitelistItemResource`

### PLATFORM-352 · Web 充值黑名单 - 获取列表

- 接口声明：`GET /blacklisted-deposit-senders`
- 输入字段：`chain`, `dynamic`, `address`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:864` · `BlacklistedDepositSendersResource`

### PLATFORM-353 · Web 充值黑名单 - 新增

- 接口声明：`POST /blacklisted-deposit-senders`
- 输入字段：`chain`, `address`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:936` · `BlacklistedDepositSendersResource`

### PLATFORM-354 · Web 充值黑名单 - 批量删除

- 接口声明：`DELETE /blacklisted-deposit-senders`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:972` · `BlacklistedDepositSendersResource`

### PLATFORM-355 · Web 充值黑名单 - 获取单个

- 接口声明：`GET /blacklisted-deposit-senders/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:997` · `BlacklistedDepositSenderResource`

### PLATFORM-356 · Web 充值黑名单 - 修改单个

- 接口声明：`PATCH /blacklisted-deposit-senders/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1002` · `BlacklistedDepositSenderResource`

### PLATFORM-357 · Web 充值黑名单 - 删除单个

- 接口声明：`DELETE /blacklisted-deposit-senders/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1029` · `BlacklistedDepositSenderResource`

### PLATFORM-358 · Web 充值黑名单 - 批量上传

- 接口声明：`POST /blacklisted-deposit-senders/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1048` · `BatchUploadBlacklistedDepositSenderResource`

### PLATFORM-359 · Web KYT 设置 - 查看所有

- 接口声明：`GET /settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1167` · `KytSettingsAdminResource`

### PLATFORM-360 · Web KYT 设置 - 查看单项

- 接口声明：`GET /settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1177` · `ChainConfigManagementAdminResource`

### PLATFORM-361 · Web KYT 设置 - 修改单项

- 接口声明：`PUT /settings/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1185` · `ChainConfigManagementAdminResource`

### PLATFORM-362 · KYT 设置 - 重置单项

- 接口声明：`DELETE /settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1208` · `ChainConfigManagementAdminResource`

### PLATFORM-363 · Web KYT 服务商 - 查看列表 

- 接口声明：`GET /chain-assessors`
- 输入字段：`direction`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1234` · `ChainAssessorsAdminResource`

### PLATFORM-364 · Web KYT 服务商 - 修改链配置

- 接口声明：`PUT /chain-assessors/<chain>`
- 输入字段：`assessor_name`, `direction`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/kyt.py:1282` · `SingleChainAssessorAdminResource`

### PLATFORM-365 · 运营-通用运营配置-直播页管理列表

- 接口声明：`GET /list`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/live.py:32` · `LivePageListResource`

### PLATFORM-366 · 运营-通用运营配置-直播页详情

- 接口声明：`GET /`
- 输入字段：`uid`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/live.py:80` · `QuestionnaireResource`

### PLATFORM-367 · 运营-通用运营配置-创建/修改直播页

- 接口声明：`POST /`
- 输入字段：`uid`, `name`, `assets`, `is_qr_code`, `poster_file_ids`, `slogan`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/live.py:119` · `QuestionnaireResource`

### PLATFORM-368 · 运营-通用运营配置-删除直播页

- 接口声明：`DELETE /`
- 输入字段：`uid`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/live.py:145` · `QuestionnaireResource`

### PLATFORM-369 · 现货maker返佣-返佣记录 

- 接口声明：`GET /history`
- 输入字段：`start_date`, `end_date`, `user_id`, `asset`, `level`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/makercashback.py:24` · `MakerCashBackHistoryResource`

### PLATFORM-370 · 链上交易-全局配置-列表

- 接口声明：`GET /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/config.py:60` · `OnchainConfigResource`

### PLATFORM-371 · 链上交易-全局配置-编辑

- 接口声明：`PUT /`
- 输入字段：`keys`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/config.py:65` · `OnchainConfigResource`

### PLATFORM-372 · 统计-资产统计-链上Bot持仓统计

- 接口声明：`GET /wallet-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/statistic.py:56` · `OnchainWalletAssetsResource`

### PLATFORM-373 · 统计-资产统计-链上资产负债统计

- 接口声明：`GET /asset-liability`
- 输入字段：`chain`, `contract`, `min_usd`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/statistic.py:189` · `OnchainAssetLiabilityResource`

### PLATFORM-374 · 链上交易-代币限制管理-列表

- 接口声明：`GET /blocklist`
- 输入字段：`chain`, `symbol`, `contract`, `notice_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:84` · `OnchainTokenBlocklistResource`

### PLATFORM-375 · 链上交易-代币限制管理-添加/编辑

- 接口声明：`PUT /blocklist`
- 输入字段：`chain`, `contract`, `block_type`, `notice_type`, `reason`, `stop_asset_liability_notice`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:146` · `OnchainTokenBlocklistResource`

### PLATFORM-376 · 链上交易-代币限制管理-删除

- 接口声明：`DELETE /blocklist`
- 输入字段：`chain`, `contract`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:207` · `OnchainTokenBlocklistResource`

### PLATFORM-377 · 链上交易-系统限制名单-列表

- 接口声明：`GET /system-blocklist`
- 输入字段：`chain`, `contract`, `symbol`, `source_type`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:228` · `OnchainTokenSystemBlocklistResource`

### PLATFORM-378 · 链上交易-系统限制名单-操作

- 接口声明：`POST /system-blocklist`
- 输入字段：`id`, `processed_result`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:293` · `OnchainTokenSystemBlocklistResource`

### PLATFORM-379 · 链上交易-链上资产

- 接口声明：`GET /<int:user_id>/balance`
- 输入字段：`contract`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:335` · `OnchainTokenBalanceResource`

### PLATFORM-380 · 链上交易-热门榜代币配置-列表

- 接口声明：`GET /hot/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:391` · `OnchainTokenHotConfigResource`

### PLATFORM-381 · 链上交易-热门榜代币配置-添加/编辑

- 接口声明：`PUT /hot/config`
- 输入字段：`chain`, `contract`, `is_top`, `expired_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:427` · `OnchainTokenHotConfigResource`

### PLATFORM-382 · 链上交易-热门榜代币配置-删除

- 接口声明：`DELETE /hot/config`
- 输入字段：`chain`, `contract`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:488` · `OnchainTokenHotConfigResource`

### PLATFORM-383 · 链上交易-RWA专区白名单配置-列表

- 接口声明：`GET /rwa/whitelist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:513` · `OnchainRWAWhitelistResource`

### PLATFORM-384 · 链上交易-RWA专区白名单配置-添加

- 接口声明：`POST /rwa/whitelist`
- 输入字段：`project_full_name`, `project_code`, `issuer`, `chain`, `contract`, `cover`, `is_top`, `about`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:637` · `OnchainRWAWhitelistResource`

### PLATFORM-385 · 链上交易-RWA专区白名单配置-编辑

- 接口声明：`PUT /rwa/whitelist`
- 输入字段：`id`, `project_full_name`, `project_code`, `issuer`, `chain`, `contract`, `cover`, `is_top`, `about`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:657` · `OnchainRWAWhitelistResource`

### PLATFORM-386 · 链上交易-RWA专区白名单配置-开启/暂停交易

- 接口声明：`PATCH /rwa/whitelist`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:673` · `OnchainRWAWhitelistResource`

### PLATFORM-387 · 链上交易-RWA专区白名单配置-删除

- 接口声明：`DELETE /rwa/whitelist`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:695` · `OnchainRWAWhitelistResource`

### PLATFORM-388 · 链上交易-RWA专区白名单配置-模板下载

- 接口声明：`GET /rwa/whitelist/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:737` · `OnchainRWAWhitelistTemplateResource`

### PLATFORM-389 · 链上交易-RWA专区白名单配置-批量上传

- 接口声明：`POST /rwa/whitelist/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/onchain/token.py:768` · `OnchainRWAWhitelistBatchUploadResource`

### PLATFORM-390 · 系统-操作记录

- 接口声明：`GET /admin-op-log`
- 输入字段：`keyword`, `namespace`, `object`, `operation`, `started_at`, `ended_at`, `last_id`, `first_id`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/op_log.py:37` · `AdminOperationLogResource`

### PLATFORM-391 · 现货-预测市场-币种配置

- 接口声明：`GET /asset-config`
- 输入字段：`active_status`, `asset`, `time_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:33` · `PreTradingAssetConfigResource`

### PLATFORM-392 · 现货-预测市场-添加币种配置

- 接口声明：`POST /asset-config`
- 输入字段：`asset`, `pledge_ratio`, `redeem_fee_rate`, `settlement_fee_rate`, `issue_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:139` · `PreTradingAssetConfigResource`

### PLATFORM-393 · 现货-预测市场-编辑币种配置

- 接口声明：`PUT /asset-config`
- 输入字段：`asset`, `pledge_ratio`, `redeem_fee_rate`, `settlement_fee_rate`, `issue_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:184` · `PreTradingAssetConfigResource`

### PLATFORM-394 · 现货-预测市场-编辑币种配置交割

- 接口声明：`PATCH /asset-config`
- 输入字段：`asset`, `settlement_price`, `settlement_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:226` · `PreTradingAssetConfigResource`

### PLATFORM-395 · 现货-预测市场-审核通过币种配置

- 接口声明：`PATCH /asset-config/audit`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:275` · `PreTradingAssetConfigAuditResource`

### PLATFORM-396 · 现货-预测市场-暂停/恢复预测市场

- 接口声明：`PATCH /asset-config/pause`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:308` · `PreTradingAssetConfigPauseResource`

### PLATFORM-397 · 现货-预测市场-当前发行

- 接口声明：`GET /user-asset-record`
- 输入字段：`status`, `user_id`, `asset`, `time_type`, `filter_zero_issue`, `order_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:342` · `PreTradingUserAssetRecordResource`

### PLATFORM-398 · 现货-预测市场-发行流水

- 接口声明：`GET /user-operate-history`
- 输入字段：`status`, `type`, `asset`, `user_id`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:427` · `PreTradingUserOperateHistoryResource`

### PLATFORM-399 · 现货-预测市场-交割配置详情

- 接口声明：`GET /asset-config/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:494` · `PreTradingAssetConfigDetailResource`

### PLATFORM-400 · 现货-预测市场-编辑交割配置内容文案

- 接口声明：`PUT /asset-config/<int:id_>/langs/<lang>`
- 输入字段：`content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:544` · `PreTradingAssetConfigDetailLangResource`

### PLATFORM-401 · 现货-预测市场-市场收盘价

- 接口声明：`GET /kline-close-price`
- 输入字段：`asset`, `kline_market`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:585` · `PreTradingAssetKlineClosePriceResource`

### PLATFORM-402 · 现货-预测市场-获取交割信息

- 接口声明：`GET /settle`
- 输入字段：`asset`, `kline_market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:638` · `PreTradingAssetSettleResource`

### PLATFORM-403 · 现货-预测市场-执行交割流程

- 接口声明：`POST /settle`
- 输入字段：`asset`, `cmd`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:707` · `PreTradingAssetSettleResource`

### PLATFORM-404 · 现货-预测市场-交割记录导出

- 接口声明：`GET /settle-his`
- 输入字段：`asset`, `market`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/pre_trading.py:759` · `PreTradingAssetSettleHisResource`

### PLATFORM-405 · 题库-问题列表

- 接口声明：`GET /list`
- 输入字段：`tag`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:33` · `QuestionListResource`

### PLATFORM-406 · 题库-创建问题

- 接口声明：`POST /list`
- 输入字段：`name`, `tag`, `option_type`, `detail_lang_map`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:59` · `QuestionListResource`

### PLATFORM-407 · 题库-问题详情

- 接口声明：`GET /<string:q_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:80` · `QuestionResource`

### PLATFORM-408 · 题库-修改问题

- 接口声明：`PUT /<string:q_id>`
- 输入字段：`name`, `tag`, `option_type`, `detail_lang_map`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:93` · `QuestionResource`

### PLATFORM-409 · 题库-删除问题

- 接口声明：`DELETE /<string:q_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:108` · `QuestionResource`

### PLATFORM-410 · 题库-获取问题组

- 接口声明：`GET /group/list`
- 输入字段：`tag`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:133` · `QuestionGroupListResource`

### PLATFORM-411 · 题库-创建问题组

- 接口声明：`POST /group/list`
- 输入字段：`name`, `tag`, `question_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:158` · `QuestionGroupListResource`

### PLATFORM-412 · 题库-问题组详情

- 接口声明：`GET /group/<string:g_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:174` · `QuestionGroupResource`

### PLATFORM-413 · 题库-修改问题组

- 接口声明：`PUT /group/<string:g_id>`
- 输入字段：`name`, `tag`, `question_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/question.py:180` · `QuestionGroupResource`

### PLATFORM-414 · 运营-活动-问卷工具-问卷列表

- 接口声明：`GET /list`
- 输入字段：`uid`, `start_time`, `end_time`, `status`, `creator`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:40` · `QuestionnaireListResource`

### PLATFORM-415 · 运营-活动-问卷工具-问卷筛选下拉栏数据

- 接口声明：`GET /list/simple`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:129` · `QuestionnaireListSimpleResource`

### PLATFORM-416 · 活动-问卷工具-问卷详情

- 接口声明：`GET /`
- 输入字段：`uid`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:150` · `QuestionnaireResource`

### PLATFORM-417 · 活动-问卷工具-创建/修改问卷

- 接口声明：`POST /`
- 输入字段：`uid`, `name`, `start_time`, `end_time`, `submit_limit`, `only_visible_to_creator`, `items`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:188` · `QuestionnaireResource`

### PLATFORM-418 · 活动-问卷工具-终止问卷

- 接口声明：`PUT /`
- 输入字段：`uid`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:316` · `QuestionnaireResource`

### PLATFORM-419 · 活动-问卷工具-删除问卷

- 接口声明：`DELETE /`
- 输入字段：`uid`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:345` · `QuestionnaireResource`

### PLATFORM-420 · 活动-问卷工具-问卷明细

- 接口声明：`GET /response/list`
- 输入字段：`questionnaire_uid`, `lang`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:379` · `QuestionnaireResponseListResource`

### PLATFORM-421 · 报表-用户报表-问卷报表

- 接口声明：`GET /statistic`
- 输入字段：`questionnaire_uid`, `lang`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:452` · `QuestionnaireStatisticResource`

### PLATFORM-422 · 运营-活动-问卷工具-问卷模板

- 接口声明：`GET /batch-upload/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/questionnaire.py:523` · `BatchUploadTemplateResource`

### PLATFORM-423 · 运营-标签管理-标签列表

- 接口声明：`GET /asset/tags`
- 输入字段：`status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:76` · `AssetTagsResource`

### PLATFORM-424 · 运营-标签管理-新增标签

- 接口声明：`POST /asset/tags`
- 输入字段：`translations`, `assets`, `status`, `is_show`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:191` · `AssetTagsResource`

### PLATFORM-425 · 运营-标签管理-修改标签

- 接口声明：`PUT /asset/tag/<int:tag_id>`
- 输入字段：`translations`, `assets`, `status`, `is_show`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:262` · `AssetTagResource`

### PLATFORM-426 · 运营-标签管理-修改排序/开启/关闭

- 接口声明：`PATCH /asset/tag/<int:tag_id>`
- 输入字段：`change`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:360` · `AssetTagResource`

### PLATFORM-427 · 运营-币种标签-拖拽排序

- 接口声明：`POST /asset/tag/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:430` · `BannerSortResource`

### PLATFORM-428 · 运营-币种标签-批量上传模版下载 

- 接口声明：`GET /asset/tags/batch-upload`
- 输入字段：`excel_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:452` · `AssetTagBatchUploadResource`

### PLATFORM-429 · 运营-币种标签-批量上传 

- 接口声明：`POST /asset/tags/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:481` · `AssetTagBatchUploadResource`

### PLATFORM-430 · 运营-标签管理-专题列表

- 接口声明：`GET /asset/topics`
- 输入字段：`status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:675` · `AssetTopicsResource`

### PLATFORM-431 · 运营-标签管理-添加专题 

- 接口声明：`POST /asset/topics`
- 输入字段：`translations`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:725` · `AssetTopicsResource`

### PLATFORM-432 · 运营-专题管理-修改专题

- 接口声明：`PUT /asset/topic/<int:topic_id>`
- 输入字段：`translations`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:776` · `AssetTopicResource`

### PLATFORM-433 · 运营-专题管理-修改排序/开启/关闭

- 接口声明：`PATCH /asset/topic/<int:topic_id>`
- 输入字段：`change`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:820` · `AssetTopicResource`

### PLATFORM-434 · 运营-币种管理-新币专区-币种列表

- 接口声明：`GET /new-asset-list`
- 输入字段：`status`, `id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:876` · `NewAssetListResource`

### PLATFORM-435 · 运营-币种管理-新币专区-添加新币排行

- 接口声明：`POST /new-asset-list`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:914` · `NewAssetListResource`

### PLATFORM-436 · 运营-币种资料-修改新币专区资料

- 接口声明：`PATCH /new-asset-information/<int:id_>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:937` · `NewAssetInformationDetailResource`

### PLATFORM-437 · 运营-币种资料-币种列表

- 接口声明：`GET /coin-list`
- 输入字段：`status`, `tag_id`, `id`, `code`, `circulation_type`, `coin_display_scene`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1013` · `CoinListResource`

### PLATFORM-438 · 运营-币种资料-币种资料搜索

- 接口声明：`GET /coin-information`
- 输入字段：`keyword`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1142` · `CoinInformationResource`

### PLATFORM-439 · 运营-币种资料-创建币种资料

- 接口声明：`POST /coin-information`
- 输入字段：`icon`, `thumbnail_icon`, `code`, `name`, `issued_date`, `online_time`, `total_supply`, `issued_price_data`, `official_website`, `white_paper`, `report_url`, `source_code`, `explorer`, `twitter`, `facebook`, `reddit`, `medium`, `discord`, `telegram`, `instagram`, `translations`, `circulation`, `circulation_notice`, `circulation_lock`, `coin_display_scene`, `tag_ids`, `explorer_data`, `status`, `token_usage_data`, `circulation_source_data`, `token_unlock_data`, `api_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1220` · `CoinInformationResource`

### PLATFORM-440 · 运营-币种资料-编辑流通量触发告警阈值

- 接口声明：`PATCH /coin-information`
- 输入字段：`min_rate`, `max_rate`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1399` · `CoinInformationResource`

### PLATFORM-441 · 运营-币种资料-修改币种资料

- 接口声明：`PATCH /coin-information/<int:id_>`
- 输入字段：`icon`, `thumbnail_icon`, `name`, `issued_date`, `online_time`, `total_supply`, `issued_price_data`, `official_website`, `white_paper`, `report_url`, `source_code`, `explorer`, `twitter`, `facebook`, `reddit`, `medium`, `discord`, `youtube`, `telegram`, `instagram`, `api_id`, `translations`, `circulation`, `circulation_notice`, `circulation_lock`, `coin_display_scene`, `tag_ids`, `explorer_data`, `status`, `token_usage_data`, `circulation_source_data`, `token_unlock_data`, `auto_translation_languages`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1442` · `CoinInformationDetailResource`

### PLATFORM-442 · 运营-币种资料-上/下架币种

- 接口声明：`PUT /coin-information/<int:id_>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1681` · `CoinInformationDetailResource`

### PLATFORM-443 · 运营-币种资料-批量上传更新币种资料 

- 接口声明：`POST /coin-information/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1721` · `CoinInformationBatchUploadResource`

### PLATFORM-444 · 运营-币种资料-批量下载币种资料 

- 接口声明：`GET /coin-information/batch-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1897` · `UserTagGroupUserResource`

### PLATFORM-445 · 运营-币种资料-上传币种图标 

- 接口声明：`POST /coin-information/icon-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:1968` · `CoinInformationIconUploadResource`

### PLATFORM-446 · 运营-币种资料-查看API获取的币种资料

- 接口声明：`GET /api-coin-info-result`
- 输入字段：`api_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:2004` · `ApiCoinInfoResultResource`

### PLATFORM-447 · 运营-币种资料-通过API获取币种资料

- 接口声明：`POST /api-coin-info-result`
- 输入字段：`api_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:2041` · `ApiCoinInfoResultResource`

### PLATFORM-448 · 运营-币种资料-编辑API获取的下载资料

- 接口声明：`PATCH /api-coin-info-result`
- 输入字段：`api_id`, `official_website`, `white_paper`, `report_url`, `source_code`, `telegram`, `facebook`, `twitter`, `reddit`, `medium`, `discord`, `youtube`, `instagram`, `en_short_description`, `cn_short_description`, `en_long_description`, `cn_long_description`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/quotes.py:2077` · `ApiCoinInfoResultResource`

### PLATFORM-449 · 运营-CoinEx 招聘-职位列表

- 接口声明：`GET /jobs`
- 输入字段：`job_type`, `work_place`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/recruit.py:72` · `JobsResource`

### PLATFORM-450 · 运营-CoinEx 招聘-添加职位

- 接口声明：`POST /jobs`
- 输入字段：`job_type`, `work_place`, `experience`, `education`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/recruit.py:127` · `JobsResource`

### PLATFORM-451 · 运营-CoinEx 招聘-职位编辑

- 接口声明：`PUT /job/<int:id_>`
- 输入字段：`job_type`, `work_place`, `experience`, `education`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/recruit.py:172` · `JobResource`

### PLATFORM-452 · 运营-CoinEx 招聘-职位删除

- 接口声明：`DELETE /job/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/recruit.py:238` · `JobResource`

### PLATFORM-453 · 报表-大使报表

- 接口声明：`GET /report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/ambassador.py:53` · `AmbassadorReportResource`

### PLATFORM-454 · 用户-CoinEx大使-大使返佣报表

- 接口声明：`GET /referral-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `keyword`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/ambassador.py:167` · `AmbassadorReferralReportResource`

### PLATFORM-455 · 用户-CoinEx大使-被邀请人返佣报表

- 接口声明：`GET /referral-detail-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `user_id`, `referree_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/ambassador.py:240` · `AmbassadorReferralDetailReportResource`

### PLATFORM-456 · 统计-API统计-实时访问统计

- 接口声明：`GET `
- 输入字段：`api_type`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/api.py:39` · `ApiRealTimeResource`

### PLATFORM-457 · 统计-API统计-历史访问统计

- 接口声明：`GET /history`
- 输入字段：`api_type`, `user_id`, `start_time`, `end_time`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/api.py:74` · `ApiHistoryResource`

### PLATFORM-458 · 统计-API统计-访问排名统计

- 接口声明：`GET /rank`
- 输入字段：`hour_type`, `api_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/api.py:115` · `ApiRankResource`

### PLATFORM-459 · 统计-API统计-资源占用数据报表

- 接口声明：`GET /access-rank`
- 输入字段：`user_id`, `start_date`, `end_date`, `page`, `system`, `limit`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/api.py:231` · `ApiAccessRankResource`

### PLATFORM-460 · 统计-API统计-资源占用数据-用户饱和度

- 接口声明：`GET /saturation/chart`
- 输入字段：`user_id`, `group_type`, `start_time`, `end_time`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/api.py:418` · `ApiSaturationChartResource`

### PLATFORM-461 · 统计-API统计-资源占用数据-系统饱和度

- 接口声明：`GET /saturation/sys/chart`
- 输入字段：`user_id`, `trade_type`, `group_type`, `start_time`, `end_time`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/api.py:605` · `ApiSysSaturationChartResource`

### PLATFORM-462 · 统计-API统计-资源占用数据-请求质量

- 接口声明：`GET /req-quality/chart`
- 输入字段：`user_id`, `trade_type`, `start_time`, `end_time`, `interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/api.py:683` · `ApiReqQualityChartResource`

### PLATFORM-463 · 统计-APP统计报表

- 接口声明：`GET /app-report`
- 输入字段：`start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/app.py:21` · `AppReportResource`

### PLATFORM-464 · 统计-APP维度统计

- 接口声明：`GET /app-report-group`
- 输入字段：`day`, `time_range`, `order_by`, `sort_type`, `group_by`, `dim_or`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/app.py:51` · `AppReportGroupResource`

### PLATFORM-465 · APP统计-语区分布

- 接口声明：`GET /app-login-users-lang`
- 输入字段：`time_range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/app.py:115` · `AppLoginUsersLangResource`

### PLATFORM-466 · 报表-定投报表-全站报表 

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/auto_invest.py:37` · `AutoInvestSiteReportResource`

### PLATFORM-467 · 用户-大客户体系-大区团队-团队返佣记录/团队

- 接口声明：`GET /team-referral-report`
- 输入字段：`start_date`, `end_date`, `team_id`, `user_id`, `report_type`, `sort_col`, `sort_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:96` · `BcTeamRefReportResource`

### PLATFORM-468 · 用户-大客户体系-大区团队-团队返佣记录/团队-导出

- 接口声明：`GET /team-referral-report-export`
- 输入字段：`start_date`, `end_date`, `team_id`, `user_id`, `page`, `limit`, `export`, `report_type`, `sort_col`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:255` · `BcTeamRefReportExportResource`

### PLATFORM-469 · 用户-大客户体系-大区团队-团队返佣记录/KA经理

- 接口声明：`GET /manager-referral-report`
- 输入字段：`start_date`, `end_date`, `user_id`, `team_id`, `report_type`, `sort_col`, `sort_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:303` · `BcManagerRefReportResource`

### PLATFORM-470 · 用户-大客户体系-大区团队-团队返佣记录/KA经理-导出

- 接口声明：`GET /manager-referral-report-export`
- 输入字段：`start_date`, `end_date`, `user_id`, `team_id`, `page`, `limit`, `export`, `report_type`, `sort_col`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:349` · `BcManagerRefReportExportResource`

### PLATFORM-471 · 用户-大客户体系-大区团队-团队返佣记录/主管、统筹账号

- 接口声明：`GET /leader-referral-report`
- 输入字段：`start_date`, `end_date`, `team_id`, `user_id`, `report_type`, `sort_col`, `sort_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:388` · `BcLeaderRefReportResource`

### PLATFORM-472 · 用户-大客户体系-大区团队-团队返佣记录/主管、统筹账号-导出

- 接口声明：`GET /leader-referral-report-export`
- 输入字段：`start_date`, `end_date`, `team_id`, `user_id`, `page`, `limit`, `export`, `report_type`, `sort_col`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:465` · `BcLeaderRefReportExportResource`

### PLATFORM-473 · 用户-大客户体系-大区团队-团队返佣记录明细

- 接口声明：`GET /team-referral-detail-report`
- 输入字段：`start_date`, `end_date`, `big_customer_id`, `manager_id`, `team_id`, `big_customer_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:508` · `BcTeamRefDetailReportResource`

### PLATFORM-474 · 用户-大客户体系-大区团队-团队返佣记录明细-导出

- 接口声明：`GET /team-referral-detail-report-export`
- 输入字段：`start_date`, `end_date`, `big_customer_id`, `manager_id`, `team_id`, `big_customer_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:630` · `BcTeamRefDetailReportExportResource`

### PLATFORM-475 · 报表-返佣报表-大客户报表

- 接口声明：`GET /big-customer-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`, `team_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:679` · `BigCustomerReportResource`

### PLATFORM-476 · 报表-返佣报表-大客户报表详情

- 接口声明：`GET /big-customer-report-detail`
- 输入字段：`report_type`, `sort_field`, `report_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/big_customer.py:790` · `BigCustomerReportDetailResource`

### PLATFORM-477 · 报表-返佣报表-经纪商返佣报表 

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `order`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/broker.py:17` · `AutoInvestSiteReportResource`

### PLATFORM-478 · 用户-商务大使体系-商务大使返佣记录

- 接口声明：`GET /ambassador-referral-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `keyword`, `bus_user_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:176` · `BusinessAmbassadorReferralReportResource`

### PLATFORM-479 · 用户-商务大使体系-子代理返佣记录

- 接口声明：`GET /tree-amb-referral-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `keyword`, `parent_id`, `bus_user_id`, `tree_height`, `team_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:363` · `TreeAmbassadorReferralReportResource`

### PLATFORM-480 · 用户-商务大使体系-商务代理返佣记录

- 接口声明：`GET /share-referral-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `target_user_keyword`, `bus_amb_keyword`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:529` · `BusinessShareReferralReportResource`

### PLATFORM-481 · 用户-商务大使体系-商务返佣记录

- 接口声明：`GET /team-referral-report`
- 输入字段：`report_type`, `user_type`, `start_date`, `end_date`, `team_id`, `sort_col`, `sort_type`, `page`, `limit`, `user_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:669` · `BusinessUserReferralReportResource`

### PLATFORM-482 · 大使体系-商务-商务返佣记录-全站-查看

- 接口声明：`GET /business-referral-report/site`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1174` · `BusinessReferralSiteReportResource`

### PLATFORM-483 · 大使体系-商务-商务返佣记录-全站-下载

- 接口声明：`GET /business-referral-report/site/export`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1185` · `BusinessReferralSiteReportExportResource`

### PLATFORM-484 · 大使体系-商务-商务返佣记录-团队-查看

- 接口声明：`GET /business-referral-report/team`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1197` · `BusinessReferralTeamReportResource`

### PLATFORM-485 · 大使体系-商务-商务返佣记录-团队-下载

- 接口声明：`GET /business-referral-report/team/export`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1208` · `BusinessReferralTeamReportExportResource`

### PLATFORM-486 · 大使体系-商务-商务返佣记录-商务-查看

- 接口声明：`GET /business-referral-report/business`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1220` · `BusinessReferralBusinessReportResource`

### PLATFORM-487 · 大使体系-商务-商务返佣记录-商务-下载

- 接口声明：`GET /business-referral-report/business/export`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1231` · `BusinessReferralBusinessReportExportResource`

### PLATFORM-488 · 报表-返佣报表-商务大使报表

- 接口声明：`GET /ambassador-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`, `team_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1299` · `BusinessAmbassadorReportResource`

### PLATFORM-489 · 报表-返佣报表-商务大使报表详情

- 接口声明：`GET /ambassador-report-detail`
- 输入字段：`report_type`, `sort_field`, `report_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1376` · `AmbassadorReportDetailResource`

### PLATFORM-490 · 报表-返佣报表-代理返佣明细报表

- 接口声明：`GET /ambassador-detail-referral-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `referree_id`, `user_id`, `bus_team_id`, `bus_user_id`, `agent_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/bus_ambassador.py:1460` · `BusinessAmbassadorDetailReferralReportResource`

### PLATFORM-491 · 报表-跟单交易报表 

- 接口声明：`GET /site-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/copy_trading.py:37` · `CopyTradingSiteReportResource`

### PLATFORM-492 · 报表-收入报表-收入详情

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:117` · `ReportInfoResource`

### PLATFORM-493 · 报表-收入报表-币种盈利余额

- 接口声明：`GET /net-income-balance`
- 输入字段：`asset`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:134` · `NetIncomeBalanceResource`

### PLATFORM-494 · 报表-收入报表-币种盈利余额明细

- 接口声明：`GET /net-income-balance-history`
- 输入字段：`asset`, `income_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:166` · `NetIncomeBalanceHistoryResource`

### PLATFORM-495 · 报表-收入报表-币种收入明细

- 接口声明：`GET /site-income-history`
- 输入字段：`asset`, `income_type`, `start_date`, `end_date`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:248` · `SiteIncomeHistoryResource`

### PLATFORM-496 · 报表-收入报表-币种收入报表

- 接口声明：`GET /asset-income-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `asset`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:342` · `AssetIncomeReportResource`

### PLATFORM-497 · 报表-收入报表-币种收入报表-异步下载

- 接口声明：`GET /asset-income-report-async-download`
- 输入字段：`report_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:442` · `AssetIncomeReportAsyncDownloadResource`

### PLATFORM-498 · 报表-收入报表-保险基金兑换报表 

- 接口声明：`GET /insurance-exchange-report`
- 输入字段：`report_type`, `report_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:468` · `InsuranceExchangeReportResource`

### PLATFORM-499 · 报表-收入报表-保险基金兑换报表-币种详情

- 接口声明：`GET /insurance-exchange-report-detail`
- 输入字段：`start_date`, `end_date`, `asset`, `report_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:502` · `InsuranceExchangeReportDetailResource`

### PLATFORM-500 · 报表-收入报表-小币兑换报表

- 接口声明：`GET /small-coin-exchange-report`
- 输入字段：`report_type`, `report_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:554` · `SmallCoinExchangeReportResource`

### PLATFORM-501 · 报表-收入报表-小币兑换-币种详情报表

- 接口声明：`GET /small-coin-detail-exchange-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:599` · `SmallCoinDetailExchangeReportResource`

### PLATFORM-502 · 报表-收入报表-亏损平衡报表

- 接口声明：`GET /loss-process-report`
- 输入字段：`report_type`, `report_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:652` · `LossProcessReportResource`

### PLATFORM-503 · 报表-收入报表-盈亏平衡-币种详情报表

- 接口声明：`GET /loss-process-detail-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:689` · `LossProcessDetailReportResource`

### PLATFORM-504 · 报表-收入报表-CET回购报表

- 接口声明：`GET /cet-buy-back-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:736` · `CetBuyBackReportResource`

### PLATFORM-505 · 报表-收入报表-实收报表

- 接口声明：`GET /real-income-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:907` · `RealIncomeReportResource`

### PLATFORM-506 · 报表-收入报表-净收报表

- 接口声明：`GET /admin-net-income-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:1002` · `AdminNetIncomeReportResource`

### PLATFORM-507 · 报表-CET销毁明细表

- 接口声明：`GET /cet-destroy-history`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:1081` · `CetDestroyHistoryResource`

### PLATFORM-508 · 报表-返佣报表

- 接口声明：`GET /refer-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:1134` · `ReferReportResource`

### PLATFORM-509 · 报表-现货maker返佣报表 

- 接口声明：`GET /markercashback-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:1201` · `MarkerCashBackReportResource`

### PLATFORM-510 · 报表-应收报表 

- 接口声明：`GET /business-report`
- 输入字段：`page`, `limit`, `start_date`, `end_date`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:1317` · `BusinessIncomeReportResource`

### PLATFORM-511 · 报表-收入报表-运营支出月报

- 接口声明：`GET /operating-expenses-report`
- 输入字段：`start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:1398` · `OperatingExpensesResource`

### PLATFORM-512 · 报表-收入报表-运营支出月报-报表曲线

- 接口声明：`GET /operating-expenses-report-series`
- 输入字段：`start_date`, `end_date`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/income.py:1462` · `OperatingExpensesSeriesResource`

### PLATFORM-513 · 报表-内容报表-内容浏览

- 接口声明：`GET /view`
- 输入字段：`lang`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/information.py:26` · `ReportInformationViewResource`

### PLATFORM-514 · 报表-内容报表-内容发布

- 接口声明：`GET /publish`
- 输入字段：`lang`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/information.py:123` · `ReportInformationPublishResource`

### PLATFORM-515 · 风控-执法用户数据导出-列表展示

- 接口声明：`GET `
- 输入字段：`user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/law_enforcement.py:22` · `LawEnforcementResource`

### PLATFORM-516 · 风控-执法用户数据导出-上传用户

- 接口声明：`POST `
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/law_enforcement.py:68` · `LawEnforcementResource`

### PLATFORM-517 · 风控-执法用户数据导出-编辑

- 接口声明：`PATCH `
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/law_enforcement.py:106` · `LawEnforcementResource`

### PLATFORM-518 · 风控-执法用户数据导出-删除

- 接口声明：`DELETE `
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/law_enforcement.py:132` · `LawEnforcementResource`

### PLATFORM-519 · 风控-执法用户数据导出-下载数据

- 接口声明：`GET /download`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/law_enforcement.py:156` · `LawEnforcementReportResource`

### PLATFORM-520 · 报表-链上交易报表-全站

- 接口声明：`GET /site`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/onchain.py:36` · `OnchainSiteTradeReportResource`

### PLATFORM-521 · 报表-链上交易报表-Token

- 接口声明：`GET /token`
- 输入字段：`search_key`, `report_type`, `page`, `limit`, `start_date`, `end_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/onchain.py:109` · `OnchainTokenTradeReportResource`

### PLATFORM-522 · 运营-邮件短信报表 

- 接口声明：`GET /country-notice`
- 输入字段：`report_type`, `country`, `start_date`, `end_date`, `order`, `sort`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/reach.py:63` · `CountryNoticeReportResource`

### PLATFORM-523 · 报表-短信渠道报表 

- 接口声明：`GET /channel-notice`
- 输入字段：`report_type`, `channel`, `start_date`, `end_date`, `order`, `sort`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/reach.py:138` · `ChannelNoticeReportResource`

### PLATFORM-524 · 运营-邮件短信报表-明细 

- 接口声明：`GET /country-notice-detail`
- 输入字段：`report_type`, `report_date`, `order`, `sort`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/reach.py:201` · `CountryNoticeReportDetailResource`

### PLATFORM-525 · 报表-短信渠道报表-明细 

- 接口声明：`GET /channel-notice-detail`
- 输入字段：`report_type`, `report_date`, `order`, `sort`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/reach.py:250` · `ChannelNoticeReportDetailResource`

### PLATFORM-526 · 运营-短信明细报表 

- 接口声明：`GET /sms`
- 输入字段：`start_date`, `end_date`, `country`, `business`, `provider`, `order`, `sort`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/reach.py:300` · `SmsReportDetailResource`

### PLATFORM-527 · 运营-短信明细报表-异步下载 

- 接口声明：`GET /sms/async-download`
- 输入字段：`start_time`, `end_time`, `country`, `business`, `provider`, `order`, `sort`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/reach.py:412` · `SmsReportDetailAsyncDownloadResource`

### PLATFORM-528 · 运营->短链接管理->短链接配置->短链接列表 

- 接口声明：`GET `
- 输入字段：`publicity_channel`, `business_segment`, `category_id`, `publicity_channel_id`, `country`, `language_area`, `allow_subset`, `short_url`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:44` · `ShortLinkResource`

### PLATFORM-529 · 运营->短链接管理->短链接配置->生成短链接 

- 接口声明：`POST `
- 输入字段：`original_url`, `title`, `language_area`, `country`, `publicity_channel_id`, `exposure_project_id`, `remark`, `allow_subset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:152` · `ShortLinkResource`

### PLATFORM-530 · 运营->短链接管理->短链接配置->编辑短链接 

- 接口声明：`PUT `
- 输入字段：`id`, `title`, `exposure_project_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:201` · `ShortLinkResource`

### PLATFORM-531 · 运营->短链接管理->短链接配置->删除短链接 

- 接口声明：`DELETE `
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:227` · `ShortLinkResource`

### PLATFORM-532 · 运营->短链接管理->短链接配置->下载邀请人资料模版 

- 接口声明：`GET /subset/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:274` · `ShortLinkSubsetTemplateResource`

### PLATFORM-533 · 运营->短链接管理->短链接配置->上传邀请人资料 

- 接口声明：`POST /subset/import/<int:parent_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:306` · `ShortLinkSubsetImportResource`

### PLATFORM-534 · 运营->短链接管理->短链接配置->邀请码短链接列表 

- 接口声明：`GET /subset`
- 输入字段：`parent_id`, `trace_code`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:381` · `ShortLinkSubsetResource`

### PLATFORM-535 · 运营->短链接管理->短链接注册用户

- 接口声明：`GET /register-users`
- 输入字段：`short_link_id`, `location_code`, `keyword`, `trace_code`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:484` · `ShortLinkRegisterUsersResource`

### PLATFORM-536 · 运营->短链接管理->短链接统计->报表 

- 接口声明：`GET /report`
- 输入字段：`short_link_id`, `start_date`, `end_date`, `trace_code`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:686` · `ShortLinkReportResource`

### PLATFORM-537 · 运营->短链接管理->短链接统计->报表详情 

- 接口声明：`GET /report-detail`
- 输入字段：`report_date`, `order`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:814` · `ShortLinkReportDetailResource`

### PLATFORM-538 · 运营->短链接管理->短链接统计->报表曲线 

- 接口声明：`GET /series`
- 输入字段：`short_link_id`, `start_date`, `end_date`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:857` · `ShortLinkSeriesResource`

### PLATFORM-539 · 运营-短链接管理-推广渠道列表

- 接口声明：`GET /publicity-channel`
- 输入字段：`platform`, `business_segment`, `category_id`, `channel`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:928` · `PublicityChannelsResource`

### PLATFORM-540 · 运营-短链接管理-新建推广渠道

- 接口声明：`POST /publicity-channel`
- 输入字段：`platform`, `category_id`, `channel`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:981` · `PublicityChannelsResource`

### PLATFORM-541 · 运营-短链接管理-新增渠道平台

- 接口声明：`POST /publicity-channel-category`
- 输入字段：`name`, `business_segment`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1031` · `PublicityChannelCategoryResource`

### PLATFORM-542 · 运营-短链接管理-渠道平台列表

- 接口声明：`GET /publicity-channel-category`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1063` · `PublicityChannelCategoryResource`

### PLATFORM-543 · 运营-短链接管理-删除渠道平台

- 接口声明：`DELETE /publicity-channel-category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1080` · `PublicityChannelCategoryDetailResource`

### PLATFORM-544 · 运营-短链接管理-编辑渠道平台

- 接口声明：`PATCH /publicity-channel-category/<int:id_>`
- 输入字段：`name`, `business_segment`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1095` · `PublicityChannelCategoryDetailResource`

### PLATFORM-545 · 运营-短链接管理-编辑推广渠道

- 接口声明：`PATCH /publicity-channel/<int:id_>`
- 输入字段：`category_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1132` · `PublicityChannelResource`

### PLATFORM-546 · 运营-短链接管理-删除推广渠道

- 接口声明：`DELETE /publicity-channel/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1168` · `PublicityChannelResource`

### PLATFORM-547 · 运营-短链接管理-曝光专项

- 接口声明：`GET /exposure-project`
- 输入字段：`name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1214` · `ExposureProjectResource`

### PLATFORM-548 · 运营-短链接管理-新增曝光专项

- 接口声明：`POST /exposure-project`
- 输入字段：`name`, `type`, `detail`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1237` · `ExposureProjectResource`

### PLATFORM-549 · 运营-短链接管理-修改曝光专项

- 接口声明：`PUT /exposure-project`
- 输入字段：`id`, `type`, `name`, `detail`, `remark`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1259` · `ExposureProjectResource`

### PLATFORM-550 · 曝光专项统计

- 接口声明：`GET /exposure-project/report`
- 输入字段：`exposure_project_id`, `title`, `short_url`, `language_area`, `publicity_channel_id`, `type`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/short_link.py:1325` · `ExposureProjectReportResource`

### PLATFORM-551 · 统计-用户触达统计

- 接口声明：`GET /page/visitors/count`
- 输入字段：`scope`, `page`, `channel`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/analytics.py:49` · `PageVisitorsCountResource`

### PLATFORM-552 · 统计-用户触达统计-用户列表

- 接口声明：`GET /page/visitors`
- 输入字段：`scope`, `page`, `channel`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/analytics.py:71` · `PageVisitorsResource`

### PLATFORM-553 · 统计-邀请好友数据

- 接口声明：`GET /refer-statistic`
- 输入字段：`day_interval`, `sort_field`, `sort_type`, `user_type`, `is_ambassador`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/analytics.py:138` · `ReferStatisticResource`

### PLATFORM-554 · 数据监控-事件管理-事件列表

- 接口声明：`GET /event`
- 输入字段：`id`, `type_id`, `name`, `status`, `created_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:58` · `MonitorEventResource`

### PLATFORM-555 · 数据监控-事件管理-事件列表-新增

- 接口声明：`POST /event`
- 输入字段：`type_id`, `name`, `data_type`, `desc`, `time_range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:123` · `MonitorEventResource`

### PLATFORM-556 · 数据监控-事件管理-事件列表-批量新增

- 接口声明：`POST /event/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:183` · `MonitorEventBatchResource`

### PLATFORM-557 · 数据监控-事件管理-事件列表-详情

- 接口声明：`GET /event/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:271` · `MonitorEventDetailResource`

### PLATFORM-558 · 数据监控-事件管理-事件列表-修改

- 接口声明：`PUT /event/<int:id_>`
- 输入字段：`type_id`, `name`, `desc`, `time_range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:338` · `MonitorEventDetailResource`

### PLATFORM-559 · 数据监控-事件管理-事件列表-删除

- 接口声明：`DELETE /event/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:399` · `MonitorEventDetailResource`

### PLATFORM-560 · 数据监控-事件管理-收藏事件

- 接口声明：`PUT /event/<int:id_>/collection`
- 输入字段：`is_del`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:427` · `MonitorEventCollection`

### PLATFORM-561 · 数据游览-事件管理-事件分组-列表

- 接口声明：`GET /event/group`
- 输入字段：`group_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:464` · `MonitorEventGroupResource`

### PLATFORM-562 · 数据游览-事件管理-图表数据

- 接口声明：`POST /event/chart`
- 输入字段：`event_id`, `tags`, `interval`, `interval_range`, `start_time`, `end_time`, `page`, `page_size`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:586` · `MonitorEventChartResource`

### PLATFORM-563 · 数据监控-事件管理-事件类型列表

- 接口声明：`GET /event/type`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:713` · `MonitorEventTypeResource`

### PLATFORM-564 · 数据监控-事件管理-事件类型列表-新建

- 接口声明：`POST /event/type`
- 输入字段：`name`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:750` · `MonitorEventTypeResource`

### PLATFORM-565 · 数据监控-事件管理-事件类型列表-删除

- 接口声明：`DELETE /event/type/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:775` · `MonitorEventTypeDetailResource`

### PLATFORM-566 · 数据监控-事件标签-事件标签-列表

- 接口声明：`GET /event/tag`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:795` · `MonitorEventTagResource`

### PLATFORM-567 · 数据监控-事件标签-事件标签-新增

- 接口声明：`POST /event/tag`
- 输入字段：`name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:826` · `MonitorEventTagResource`

### PLATFORM-568 · 数据监控-事件标签-事件标签-修改

- 接口声明：`PUT /event/tag/<int:id_>`
- 输入字段：`name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:853` · `EventTagDetailResource`

### PLATFORM-569 · 数据监控-事件管理-事件模版

- 接口声明：`GET /event/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:891` · `MonitorEventDataTemplateResource`

### PLATFORM-570 · 数据监控-事件管理-事件列表-批量更新状态

- 接口声明：`PUT /event/status/batch-update`
- 输入字段：`ids`, `update_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/biz_monitor.py:905` · `MonitorEventStatusBatchUpdateResource`

### PLATFORM-571 · 统计-资产统计

- 接口声明：`GET /assets`
- 输入字段：`sort_name`, `sort_type`, `account_type`, `asset`, `tag_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:115` · `RealtimeAssetResource`

### PLATFORM-572 · 统计-活跃资产统计

- 接口声明：`GET /active-assets`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:202` · `RealtimeActiveAssetsResource`

### PLATFORM-573 · 统计-实时成交

- 接口声明：`GET /deals`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:224` · `RealDealsResource`

### PLATFORM-574 · 统计-实时充提

- 接口声明：`GET /deposit_withdraw`
- 输入字段：`time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:285` · `RealDepositWithdrawResource`

### PLATFORM-575 · 统计-实时统计-杠杆实时爆仓

- 接口声明：`GET /margin-liquidation`
- 输入字段：`time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:316` · `RealtimeMarginLiquidationResource`

### PLATFORM-576 · 统计-实时统计-合约实时爆仓

- 接口声明：`GET /perpetual-liquidation`
- 输入字段：`time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:338` · `RealtimePerpetualLiquidationResource`

### PLATFORM-577 · 统计-注册用户-国籍分布 统计-注册用户-语言分布

- 接口声明：`GET /user-register`
- 输入字段：`time_type`, `group_type`, `area`, `sort_by`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:417` · `UserRegisterResource`

### PLATFORM-578 · 币币-杠杆-杠杆资产统计-市场 

- 接口声明：`GET /margin-markets`
- 输入字段：`order`, `order_type`, `asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:631` · `MarginMarketResource`

### PLATFORM-579 · 币币-杠杆-杠杆资产统计-币种

- 接口声明：`GET /margin-assets`
- 输入字段：`order`, `order_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:672` · `MarginAssetResource`

### PLATFORM-580 · 币币-杠杆-杠杆资产统计-币种详情

- 接口声明：`GET /margin-asset`
- 输入字段：`order`, `order_type`, `asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:714` · `MarginAssetDetailResource`

### PLATFORM-581 · 统计-借贷资产

- 接口声明：`GET /loan-assets`
- 输入字段：`asset`, `in_margin`, `in_pledge`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:754` · `LoanAssetResource`

### PLATFORM-582 · 统计-实时资产

- 接口声明：`GET /summary-assets`
- 输入字段：`asset`, `account_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:780` · `SummaryAssetsResource`

### PLATFORM-583 · 统计-实时用户

- 接口声明：`GET /users`
- 输入字段：`export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:818` · `UsersResource`

### PLATFORM-584 · 统计-净留存统计

- 接口声明：`GET /deposit-withdraw-retention-rate`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:1055` · `DepositWithdrawRetentionRateResource`

### PLATFORM-585 · 统计-活跃用户-国籍分布 统计-活跃用户-语言分布

- 接口声明：`GET /active-user`
- 输入字段：`time_type`, `group_type`, `area`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:1081` · `ActiveUserResource`

### PLATFORM-586 · 统计-资产用户-国籍分布 统计-资产用户-语言分布

- 接口声明：`GET /asset-user`
- 输入字段：`asset`, `account_type`, `sort_type`, `sort_name`, `group_type`, `area`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:1214` · `AssetUserResource`

### PLATFORM-587 · 统计-交易用户-国籍分布 统计-交易用户-语言分布

- 接口声明：`GET /user-trade`
- 输入字段：`time_type`, `asset`, `market`, `account_type`, `sort_type`, `sort_name`, `group_type`, `area`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:1491` · `UserTradeResource`

### PLATFORM-588 · 统计-收入统计-国籍分布 统计-收入统计-语言分布

- 接口声明：`GET /trade-fee`
- 输入字段：`time_type`, `sort_type`, `sort_name`, `group_type`, `area`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:1803` · `UserTradeFee`

### PLATFORM-589 · 统计-邀请排行

- 接口声明：`GET /referral-rank`
- 输入字段：`time_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2137` · `ReferralRankResource`

### PLATFORM-590 · 统计-交易成交比例

- 接口声明：`GET /trade-ratio`
- 输入字段：`time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2208` · `TradeRatioResource`

### PLATFORM-591 · 统计-永续市场交易增长排名

- 接口声明：`GET /perpetual-trade-rank`
- 输入字段：`time_type`, `sort_name`, `sort_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2225` · `PerpetualRankResource`

### PLATFORM-592 · 统计-币币资产交易增长排名

- 接口声明：`GET /spot-asset-trade-rank`
- 输入字段：`time_type`, `sort_name`, `sort_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2318` · `SpotAssetTradeRankResource`

### PLATFORM-593 · 统计-近30天活跃用户

- 接口声明：`GET /active-users`
- 输入字段：`type`, `range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2452` · `ActiveUserStatisticResource`

### PLATFORM-594 · 实时深度-现货合约

- 接口声明：`GET /real-depth`
- 输入字段：`trade_type`, `market`, `exchange`, `export`, `sort_type`, `sort_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2532` · `RealtimeDepthResource`

### PLATFORM-595 · 报表-合约报表-合约用户统计

- 接口声明：`GET /perpetual-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2652` · `PerpetualPositionUserResource`

### PLATFORM-596 · 统计-不活跃用户统计

- 接口声明：`GET /no-active-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2670` · `NoActiveUserResource`

### PLATFORM-597 · 统计-实时统计-合约市场数据

- 接口声明：`GET /perpetual-monitor`
- 输入字段：`market`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2829` · `PerpetualMonitorResource`

### PLATFORM-598 · 统计-实时统计-指标历史曲线

- 接口声明：`GET /perpetual-monitor-series`
- 输入字段：`series_type`, `market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2857` · `PerpetualMonitorSeriesResource`

### PLATFORM-599 · 统计-实时统计-杠杆市场数据

- 接口声明：`GET /margin-monitor`
- 输入字段：`market`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2931` · `MarginMonitorResource`

### PLATFORM-600 · 统计-实时统计-杠杆指标历史曲线

- 接口声明：`GET /margin-monitor-series`
- 输入字段：`series_type`, `market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2959` · `MarginMonitorSeriesResource`

### PLATFORM-601 · 统计-用户统计-合约盈亏统计

- 接口声明：`GET /perpetual-profit-loss`
- 输入字段：`range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:2976` · `PerpetualProfitLossResource`

### PLATFORM-602 · 统计-用户统计-安全设置统计

- 接口声明：`GET /security`
- 输入字段：`range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3011` · `SecuritySettingStatisticsResource`

### PLATFORM-603 · 统计-用户统计-大使统计

- 接口声明：`GET /ambassador`
- 输入字段：`ambassador_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3038` · `AmbassadorStatisticsResource`

### PLATFORM-604 · 统计-资产统计-借贷资产评估表

- 接口声明：`GET /asset-synthetic`
- 输入字段：`asset`, `is_margin`, `is_perpetual`, `is_pledge_asset`, `sort_by`, `sort_type`, `is_export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3088` · `AssetSyntheticStatisticsResource`

### PLATFORM-605 · 统计-资产统计-借贷资产评估表-修改备注

- 接口声明：`PUT /asset-synthetic`
- 输入字段：`asset`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3204` · `AssetSyntheticStatisticsResource`

### PLATFORM-606 · 统计-实时统计-实时流动性监控

- 接口声明：`GET /market-liquidity-statistic`
- 输入字段：`market_type`, `market`, `sort_name`, `sort_direction`, `use_advanced_condition`, `show_depth`, `export`, `trade_area`, `exchange`, `is_amm_market`, `data_mode`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3304` · `MarketLiquidityStatisticResource`

### PLATFORM-607 · 统计-实时统计-市场流动性详情

- 接口声明：`GET /market-liquidity-detail`
- 输入字段：`market_type`, `market`, `data_mode`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3659` · `MarketLiquidityDetailResource`

### PLATFORM-608 · 统计-实时统计-市场流动性曲线

- 接口声明：`GET /market-liquidity-series`
- 输入字段：`market_type`, `market`, `field`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3848` · `MarketLiquiditySeriesResource`

### PLATFORM-609 · 统计-实时统计-市场流动性统计筛选条件

- 接口声明：`PUT /market-liquidity-filter`
- 输入字段：`market_type`, `and_filters`, `or_filters`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3901` · `MarketLiquidityFilterResource`

### PLATFORM-610 · 统计-实时统计-做市商账户监控列表

- 接口声明：`GET /account-score-statistic`
- 输入字段：`market_type`, `user_id`, `sort_name`, `sort_direction`, `user_category`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:3996` · `AccountScoreStatisticResource`

### PLATFORM-611 · 统计-实时统计-做市商账户详情-按日期

- 接口声明：`GET /account-statistic-time-detail`
- 输入字段：`market_type`, `user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4150` · `AccountStatisticTimeDetailResource`

### PLATFORM-612 · 统计-实时统计-编辑做市商账户备注

- 接口声明：`PUT /account-statistic-remark`
- 输入字段：`market_type`, `user_id`, `remark`, `credit_total`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4256` · `AccountStatisticRemarkResource`

### PLATFORM-613 · 统计-实时统计-做市商账户详情-按市场

- 接口声明：`GET /account-statistic-market-detail`
- 输入字段：`market_type`, `user_id`, `report_time`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4323` · `AccountStatisticMarketDetailResource`

### PLATFORM-614 · 统计-实时统计-特殊账户资金统计

- 接口声明：`GET /special-account-statistic`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4454` · `SpecialAccountStatisticResource`

### PLATFORM-615 · 统计-实时统计-特殊账户资金统计-导出

- 接口声明：`GET /special-account-statistic-export`
- 输入字段：`report_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4702` · `SpecialAccountStatisticExportResource`

### PLATFORM-616 · 统计-实时统计-特殊账户资金统计详情

- 接口声明：`GET /special-account-statistic-detail`
- 输入字段：`user_id`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4758` · `SpecialAccountStatisticDetailResource`

### PLATFORM-617 · 统计-实时统计-特殊账户配置列表

- 接口声明：`GET /special-account-config`
- 输入字段：`user_id`, `exchange`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4898` · `SpecialAccountConfigResource`

### PLATFORM-618 · 统计-实时统计-新增特殊账户配置

- 接口声明：`POST /special-account-config`
- 输入字段：`user_id`, `exchange`, `api_key`, `secret`, `api_passphrase`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4932` · `SpecialAccountConfigResource`

### PLATFORM-619 · 统计-实时统计-编辑特殊账户配置

- 接口声明：`PUT /special-account-config`
- 输入字段：`id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4965` · `SpecialAccountConfigResource`

### PLATFORM-620 · 统计-实时统计-删除特殊账户配置

- 接口声明：`DELETE /special-account-config`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:4991` · `SpecialAccountConfigResource`

### PLATFORM-621 · 统计-资产统计-借贷统计

- 接口声明：`GET /loan-statistic`
- 输入字段：`asset`, `loan_type`, `sort_name`, `sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/statistic/real_time.py:5018` · `LoanStatisticResource`

### PLATFORM-622 · UserEmailCheckTemplateResource.get（用途待确认）

- 接口声明：`GET /user-check/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:46` · `UserEmailCheckTemplateResource`

### PLATFORM-623 · 用户-用户验证-列表展示

- 接口声明：`GET /user-check`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:59` · `UserCheckResource`

### PLATFORM-624 · 用户-用户验证-批量上传

- 接口声明：`POST /user-check`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:78` · `UserCheckResource`

### PLATFORM-625 · 用户-用户验证-删除

- 接口声明：`DELETE /user-check`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:182` · `UserCheckResource`

### PLATFORM-626 · 用户-用户验证-导出

- 接口声明：`GET /user-check/export`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:230` · `UserCheckExportResource`

### PLATFORM-627 · UserMaskIdTransferTemplateResource.get（用途待确认）

- 接口声明：`GET /user-check/mask-id-transfer/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:285` · `UserMaskIdTransferTemplateResource`

### PLATFORM-628 · 用户-用户验证-CUID列表

- 接口声明：`GET /user-check/mask-id-transfer`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:304` · `UserMaskIdTransferResource`

### PLATFORM-629 · 用户-用户验证-CUID上传

- 接口声明：`POST /user-check/mask-id-transfer`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:323` · `UserMaskIdTransferResource`

### PLATFORM-630 · 用户-用户验证-CUID删除

- 接口声明：`DELETE /user-check/mask-id-transfer`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:379` · `UserMaskIdTransferResource`

### PLATFORM-631 · 用户-用户验证-CUID导出

- 接口声明：`GET /user-check/mask-id-transfer/export`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:405` · `UserMaskIdTransferExportResource`

### PLATFORM-632 · 新手必读-文章列表

- 接口声明：`GET /zendesk/help_center/newbie-must-read/articles`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:436` · `NewbieMustReadArticlesResource`

### PLATFORM-633 · 新手必读-文章详情

- 接口声明：`GET /zendesk/help_center/newbie-must-read/articles/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:499` · `NewbieMustReadArticleDetailResource`

### PLATFORM-634 · 新手必读-增加/修改文章

- 接口声明：`POST /zendesk/help_center/newbie-must-read/articles/<int:id_>`
- 输入字段：`light_icon`, `dark_icon`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:535` · `NewbieMustReadArticleDetailResource`

### PLATFORM-635 · 新手必读-修改文章状态

- 接口声明：`PUT /zendesk/help_center/newbie-must-read/articles/<int:id_>`
- 输入字段：`valid`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:645` · `NewbieMustReadArticleDetailResource`

### PLATFORM-636 · 新手必读-删除文章

- 接口声明：`DELETE /zendesk/help_center/newbie-must-read/articles/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:677` · `NewbieMustReadArticleDetailResource`

### PLATFORM-637 · 新手必读-文章排序

- 接口声明：`PUT /zendesk/help_center/newbie-must-read/articles/<int:id_>/sort`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/support.py:710` · `NewbieMustReadArticleSortResource`

### PLATFORM-638 · 心跳

- 接口声明：`GET /ping`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:67` · `PingResource`

### PLATFORM-639 · 系统-站点设置列表

- 接口声明：`GET /site-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:78` · `SiteSettingsResource`

### PLATFORM-640 · 系统-站点设置详情

- 接口声明：`GET /site-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:89` · `SiteSettingsManagementResource`

### PLATFORM-641 · 系统-站点设置编辑

- 接口声明：`PUT /site-settings/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:97` · `SiteSettingsManagementResource`

### PLATFORM-642 · 系统-站点设置配置删除

- 接口声明：`DELETE /site-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:125` · `SiteSettingsManagementResource`

### PLATFORM-643 · 系统-站点设置-保护期状态列表

- 接口声明：`GET /protect-duration-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:171` · `ProtectDurationSettingsResource`

### PLATFORM-644 · 系统-保护期设置编辑

- 接口声明：`PUT /protect-duration-settings/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:210` · `ProtectDurationSettingResource`

### PLATFORM-645 · 系统-保护期配置删除

- 接口声明：`DELETE /protect-duration-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:238` · `ProtectDurationSettingResource`

### PLATFORM-646 · 系统-业务变量配置列表

- 接口声明：`GET /business-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:262` · `BusinessSettingsResource`

### PLATFORM-647 · 系统-业务变量配置详情

- 接口声明：`GET /business-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:273` · `BusinessSettingsManagementResource`

### PLATFORM-648 · 系统-业务变量配置编辑

- 接口声明：`PUT /business-settings/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:281` · `BusinessSettingsManagementResource`

### PLATFORM-649 · 系统-业务变量配置删除

- 接口声明：`DELETE /business-settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:336` · `BusinessSettingsManagementResource`

### PLATFORM-650 · 系统-国家配置列表

- 接口声明：`GET /country-settings`
- 输入字段：`keyword`, `kyc_compliance_mode`, `allow_kyc_country`, `allow_kyc_nationality`, `pro_supported`, `allow_kyc_auto_audit_from_app`, `allow_kyc_auto_audit_from_web`, `allow_register_from_app`, `allow_register_from_web`, `allow_register`, `allow_binding_mobile`, `allow_visit`, `ip_reminder_on`, `allow_login`, `kyc_allow_login`, `only_withdrawal`, `allow_liveness`, `page`, `limit`
- 显式控制：ns.use_kwargs(dict(keyword=fields.String, kyc_compliance_mode=fields.String, allow_kyc_country=BoolField(allow_none=True), allow_kyc_nationality=BoolField(allow_none=True), pro_sup
- 代码依据：`app/api/admin/system.py:379` · `CountrySettingsListResource`

### PLATFORM-651 · 系统-编辑国家配置

- 接口声明：`PUT /country-settings/<code>/<field>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:494` · `CountrySettingsFieldResource`

### PLATFORM-652 · 系统-国家配置-最新注册用户ID

- 接口声明：`GET /country-settings/latest-register-user-id`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:528` · `LatestRegisterUserIdResource`

### PLATFORM-653 · 系统-sms配置

- 接口声明：`GET /country-sms-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:539` · `CountrySmsSettingsListResource`

### PLATFORM-654 · 系统-sms配置修改

- 接口声明：`PUT /country-sms-settings/<int:country_code>`
- 输入字段：`sms_providers`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:566` · `CountrySmsSettingsResource`

### PLATFORM-655 · 系统-sms配置删除

- 接口声明：`DELETE /country-sms-settings/<int:country_code>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:606` · `CountrySmsSettingsResource`

### PLATFORM-656 · 系统-短信渠道状态表

- 接口声明：`GET /country-sms-status`
- 输入字段：`country`, `provider`, `status`, `is_open`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:634` · `CountrySmsStatusResource`

### PLATFORM-657 · 系统-汇率

- 接口声明：`GET /asset-prices`
- 输入字段：`asset`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:682` · `AssetPricesResource`

### PLATFORM-658 · 系统-IP白名单设置

- 接口声明：`GET /ip-whitelist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:714` · `IpWhiteListResource`

### PLATFORM-659 · 系统-IP白名单编辑

- 接口声明：`POST /ip-whitelist`
- 输入字段：`ips`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:720` · `IpWhiteListResource`

### PLATFORM-660 · dashboard首页

- 接口声明：`GET /dashboard`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:750` · `DashBoardIndex`

### PLATFORM-661 · 系统-升级维护-临时维护记录列表

- 接口声明：`GET /temp-maintain`
- 输入字段：`page`, `limit`, `scope`, `started_at`, `ended_at`, `keyword`, `active_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1119` · `TempMaintainResource`

### PLATFORM-662 · 系统-升级维护-新增临时维护记录

- 接口声明：`POST /temp-maintain`
- 输入字段：`scope`, `started_at`, `ended_at`, `jump_page_enabled`, `remark`, `url`, `protect_duration`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1185` · `TempMaintainResource`

### PLATFORM-663 · 系统-升级维护-修改临时维护记录

- 接口声明：`PUT /temp-maintain/<int:id_>`
- 输入字段：`scope`, `started_at`, `ended_at`, `jump_page_enabled`, `remark`, `url`, `protect_duration`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1246` · `TempMaintainDetailResource`

### PLATFORM-664 · 系统-升级维护-删除临时维护记录

- 接口声明：`DELETE /temp-maintain/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1310` · `TempMaintainDetailResource`

### PLATFORM-665 · 系统-升级维护-终止临时维护

- 接口声明：`PATCH /temp-maintain/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1333` · `TempMaintainDetailResource`

### PLATFORM-666 · 系统-升级维护-获取临时维护记录

- 接口声明：`GET /temp-maintain/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1357` · `TempMaintainDetailResource`

### PLATFORM-667 · 运营-维护通知-获取维护通知详情

- 接口声明：`GET /temp-maintain/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1381` · `TempMaintainContentResource`

### PLATFORM-668 · 运营-维护通知-编辑维护通知详情

- 接口声明：`PUT /temp-maintain/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1395` · `TempMaintainContentResource`

### PLATFORM-669 · 系统-升级维护-新建单市场维护

- 接口声明：`POST /single-market/maintain`
- 输入字段：`market`, `maintain_status`, `maintain_expect_end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1562` · `SingleMarketMaintainsResource`

### PLATFORM-670 · 系统-升级维护-单市场维护状态列表

- 接口声明：`GET /single-market/maintain`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1591` · `SingleMarketMaintainsResource`

### PLATFORM-671 · 系统-升级维护-编辑单市场维护

- 接口声明：`PUT /single-market/maintain/<int:id_>`
- 输入字段：`maintain_status`, `maintain_expect_end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1606` · `SingleMarketMaintainResource`

### PLATFORM-672 · 系统-升级维护-删除单市场维护

- 接口声明：`DELETE /single-market/maintain/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1630` · `SingleMarketMaintainResource`

### PLATFORM-673 · 系统-局部地区屏蔽表

- 接口声明：`GET /local-areas-block`
- 输入字段：`type`, `country_code`, `state_code`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1682` · `LocalAreasBlockListResource`

### PLATFORM-674 · 系统-局部地区屏蔽表创建

- 接口声明：`POST /local-areas-block`
- 输入字段：`type`, `country_code`, `state_codes`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1745` · `LocalAreasBlockListResource`

### PLATFORM-675 · 系统-自营交易-查看配置

- 接口声明：`GET /prop-trading-config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1792` · `PropTradingConfigResource`

### PLATFORM-676 · 系统-自营交易-修改配置

- 接口声明：`POST /prop-trading-config`
- 输入字段：`sample_rate`, `market_scope`, `markets`, `blacklist_markets`, `group`, `risk_deal_amount`, `risk_deal_amount_rate`, `prop_risk_deal_amount_rate`, `prop_risk_deal_amount`, `op_position_count`, `op_win_rate`, `whitelist_deal_days`, `whitelist_deal_amount`, `whitelist_register_days`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1817` · `PropTradingConfigResource`

### PLATFORM-677 · 系统-自营交易-查看用户

- 接口声明：`GET /prop-trading-user`
- 输入字段：`group`, `user_id`, `status`, `reason`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1945` · `PropTradingUserResource`

### PLATFORM-678 · 系统-自营交易-添加用户

- 接口声明：`POST /prop-trading-user`
- 输入字段：`group`, `user_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:1985` · `PropTradingUserResource`

### PLATFORM-679 · 系统-自营交易-报表

- 接口声明：`GET /prop-trading-report`
- 输入字段：`market`, `start_date`, `end_date`, `sort`, `page`, `limit`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:2023` · `PropTradingReportResource`

### PLATFORM-680 · 系统-自营交易-监控

- 接口声明：`GET /prop-trading-slice`
- 输入字段：`market`, `field`, `latest`, `start`, `end`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:2114` · `PropTradingDataViewResource`

### PLATFORM-681 · 系统-自营交易-统计

- 接口声明：`GET /prop-trading-stat`
- 输入字段：`sort`, `page`, `limit`, `slice_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:2223` · `PropTradingLatestResource`

### PLATFORM-682 · 系统-自营交易-对手盘统计

- 接口声明：`GET /prop-trading-user-stat`
- 输入字段：`period`, `market`, `user_id`, `position_ge`, `win_amount_ge`, `sort`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:2310` · `PropTradingUserStatResource`

### PLATFORM-683 · KlineBoostSettingResource.get（用途待确认）

- 接口声明：`GET /kline-boost-setting`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:2369` · `KlineBoostSettingResource`

### PLATFORM-684 · KlineBoostSettingResource.post（用途待确认）

- 接口声明：`POST /kline-boost-setting`
- 输入字段：`business`, `current_multiple`, `end_multiple`, `increase_rate`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:2395` · `KlineBoostSettingResource`

### PLATFORM-685 · LangCnNamesResource.get（用途待确认）

- 接口声明：`GET /lang/cn-names`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/system.py:2449` · `LangCnNamesResource`

### PLATFORM-686 · 上传-文件上传

- 接口声明：`POST /image`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/upload.py:39` · `ImageUploadResource`

### PLATFORM-687 · 上传-币种Icon生成缩略图

- 接口声明：`POST /generate-icon-thumbnail`
- 输入字段：`image_file_key`, `width`, `height`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/upload.py:179` · `GenerateIconThumbnailResource`

### PLATFORM-688 · 上传-视频上传

- 接口声明：`POST /video`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/upload.py:237` · `VideoUploadResource`

### PLATFORM-689 · 上传-文件上传

- 接口声明：`POST /video-subtitle`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/upload.py:326` · `VideoSubtitleUploadResource`

### PLATFORM-690 · 用户-VIP-VIP列表

- 接口声明：`GET `
- 输入字段：`search_keyword`, `page`, `limit`, `user_type`, `level`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/vip.py:122` · `VipResource`

### PLATFORM-691 · 用户-VIP-增加VIP

- 接口声明：`POST `
- 输入字段：`user_id`, `real_level`, `lock_level`, `remark`, `expired_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/vip.py:229` · `VipResource`

### PLATFORM-692 · 用户-VIP-用户列表-清除保底等级

- 接口声明：`PUT `
- 输入字段：`user_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/vip.py:318` · `VipResource`

### PLATFORM-693 · 用户-VIP-用户列表-设置保底等级

- 接口声明：`PUT /<int:user_id>`
- 输入字段：`lock_level`, `remark`, `expired_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/vip.py:376` · `VipDetailResource`

### PLATFORM-694 · 用户-VIP-VIP用户列表-下载批量上传模板

- 接口声明：`GET /batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/vip.py:468` · `VipBatchUploadResource`

### PLATFORM-695 · 用户-VIP-VIP用户列表-批量上传保底等级

- 接口声明：`POST /batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/vip.py:477` · `VipBatchUploadResource`

### PLATFORM-696 · 用户-VIP-变更记录

- 接口声明：`GET /change-log`
- 输入字段：`search_keyword`, `change_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/vip.py:745` · `VipUserChangeLogResource`

### PLATFORM-697 · HomepageResource.get（用途待确认）

- 接口声明：`GET /homepage`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:29` · `HomepageResource`

### PLATFORM-698 · academy 文章列表导航

- 接口声明：`GET /nav`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:44` · `NavCategoryResource`

### PLATFORM-699 · 获取文章详情  Returns:     title (str): 文章标题     abstract (str): 文章摘要     content (str): 文章内容     read_time (int): 阅读时长(分钟)     primary_category_id (int): 主分类ID     secondary_category_id

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:60` · `DetailsResource`

### PLATFORM-700 · RelatedArticlesResource.get（用途待确认）

- 接口声明：`GET /<int:id_>/related-articles`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:247` · `RelatedArticlesResource`

### PLATFORM-701 · 币种资料页-相关文章

- 接口声明：`GET /coin-related-articles`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:324` · `CoinRelatedArticlesResource`

### PLATFORM-702 · EnabledTagsResource.get（用途待确认）

- 接口声明：`GET /tags`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:366` · `EnabledTagsResource`

### PLATFORM-703 · GlossaryResource.get（用途待确认）

- 接口声明：`GET /glossary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:395` · `GlossaryResource`

### PLATFORM-704 · SearchResource.get（用途待确认）

- 接口声明：`GET /search`
- 输入字段：`search_key`, `tag_id`, `last_id`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:410` · `SearchResource`

### PLATFORM-705 · SitemapResource.get（用途待确认）

- 接口声明：`GET /sitemap`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:436` · `SitemapResource`

### PLATFORM-706 · app 最新 top x 篇文章（不区分目录）

- 接口声明：`GET /last`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:454` · `LastResource`

### PLATFORM-707 · app 一级目录下的文章

- 接口声明：`GET /pid/<int:primary_category_id>`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/academy.py:490` · `PrimaryCategoryArticleResource`

### PLATFORM-708 · AIAnalysisReferenceResource.get（用途待确认）

- 接口声明：`GET /reference`
- 输入字段：`refer_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/ai_analysis.py:42` · `AIAnalysisReferenceResource`

### PLATFORM-709 · AIAnalysisSummaryResource.get（用途待确认）

- 接口声明：`GET /<string:asset>/summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/ai_analysis.py:67` · `AIAnalysisSummaryResource`

### PLATFORM-710 · AIAnalysisDetailResource.get（用途待确认）

- 接口声明：`GET /<string:asset>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/ai_analysis.py:81` · `AIAnalysisDetailResource`

### PLATFORM-711 · AIAnalysisVoteResource.put（用途待确认）

- 接口声明：`PUT /<string:asset>/vote`
- 输入字段：`is_up`
- 显式控制：require_login
- 代码依据：`app/api/frontend/ai_analysis.py:124` · `AIAnalysisVoteResource`

### PLATFORM-712 · AIAnalysisVoteResource.delete（用途待确认）

- 接口声明：`DELETE /<string:asset>/vote`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/ai_analysis.py:159` · `AIAnalysisVoteResource`

### PLATFORM-713 · PageVisitorsResource.post（用途待确认）

- 接口声明：`POST /page/visitors`
- 输入字段：`scope`, `page`, `channel`
- 显式控制：require_login
- 代码依据：`app/api/frontend/analytics.py:46` · `PageVisitorsResource`

### PLATFORM-714 · PopupPushCountResource.post（用途待确认）

- 接口声明：`POST /popup_window_push/count`
- 输入字段：`report_type`, `id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/analytics.py:66` · `PopupPushCountResource`

### PLATFORM-715 · PushStatisticResource.post（用途待确认）

- 接口声明：`POST /push-statistic`
- 输入字段：`report_type`, `id`, `token`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/analytics.py:84` · `PushStatisticResource`

### PLATFORM-716 · PushStatisticEmailResource.get（用途待确认）

- 接口声明：`GET /push-statistic/email`
- 输入字段：`token`, `manager_id`, `mission_plan_id`, `equity_send_apply_id`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/analytics.py:158` · `PushStatisticEmailResource`

### PLATFORM-717 · MetricsResource.post（用途待确认）

- 接口声明：`POST /metrics`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/analytics.py:184` · `MetricsResource`

### PLATFORM-718 · AssetAnalyticsResource.post（用途待确认）

- 接口声明：`POST /asset`
- 输入字段：`asset`, `scene`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/analytics.py:209` · `AssetAnalyticsResource`

### PLATFORM-719 · EventResource.post（用途待确认）

- 接口声明：`POST /report-event`
- 输入字段：`page`, `event`
- 显式控制：require_login(allow_sub_account=False); ns.use_kwargs(dict(page=EnumField(['/register', '/signin'], required=True), event=EnumField(['register', 'login'], required=True)))
- 代码依据：`app/api/frontend/analytics.py:249` · `EventResource`

### PLATFORM-720 · DeviceResource.post（用途待确认）

- 接口声明：`POST /device`
- 输入字段：`device_id`, `device_info`, `device_type`, `signature`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/analytics.py:264` · `DeviceResource`

### PLATFORM-721 · 事件追踪上报

- 接口声明：`POST /trace`
- 输入字段：`event`, `token`, `data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/analytics.py:299` · `EventTraceResource`

### PLATFORM-722 · DownloadResource.get（用途待确认）

- 接口声明：`GET /download/`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:52` · `DownloadResource`

### PLATFORM-723 · DownloadURLResource.get（用途待确认）

- 接口声明：`GET /download/url/`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:73` · `DownloadURLResource`

### PLATFORM-724 · 设置接口

- 接口声明：`GET /setting/`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:96` · `SettingListResource`

### PLATFORM-725 · 新快捷方式入口

- 接口声明：`GET /setting/new-entrances`
- 输入字段：`version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:119` · `NewEntranceListResource`

### PLATFORM-726 · 用户快捷入口排序 

- 接口声明：`GET /setting/new-entrances/sort`
- 输入字段：`version`
- 显式控制：require_login
- 代码依据：`app/api/frontend/app.py:158` · `NewEntranceSortResource`

### PLATFORM-727 · 编辑快捷入口排序 

- 接口声明：`POST /setting/new-entrances/sort`
- 输入字段：`id_list`, `version`
- 显式控制：require_login
- 代码依据：`app/api/frontend/app.py:184` · `NewEntranceSortResource`

### PLATFORM-728 · AppActivateResource.get（用途待确认）

- 接口声明：`GET /setting/app-activate`
- 输入字段：`activate_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:233` · `AppActivateResource`

### PLATFORM-729 · NewAppActivateResource.get（用途待确认）

- 接口声明：`GET /setting/app-activate-introduction`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:259` · `NewAppActivateResource`

### PLATFORM-730 · AppActivatePublicityResource.get（用途待确认）

- 接口声明：`GET /setting/app-activate-publicity`
- 输入字段：`version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:282` · `AppActivatePublicityResource`

### PLATFORM-731 · StartPageResource.get（用途待确认）

- 接口声明：`GET /setting/start-page`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:313` · `StartPageResource`

### PLATFORM-732 · PushReportResource.post（用途待确认）

- 接口声明：`POST /push/report`
- 输入字段：`push_id`, `channel`, `info`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:341` · `PushReportResource`

### PLATFORM-733 · PushReportLogoutResource.post（用途待确认）

- 接口声明：`POST /push/report/logout`
- 输入字段：`push_id`, `user_id`, `channel`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:411` · `PushReportLogoutResource`

### PLATFORM-734 · App各种push开关相关事件上报

- 接口声明：`PUT /event/report`
- 输入字段：`device_id`, `report_user`, `events`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:445` · `EventReportResource`

### PLATFORM-735 · IOSSupportResource.post（用途待确认）

- 接口声明：`POST /ios-support`
- 输入字段：`body`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:520` · `IOSSupportResource`

### PLATFORM-736 · APP推送上报

- 接口声明：`POST /push/submit/<business_push_id>`
- 输入字段：`push_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:538` · `PushSubmitResource`

### PLATFORM-737 · DynamicFallingResource.get（用途待确认）

- 接口声明：`GET /dynamic-falling`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:590` · `DynamicFallingResource`

### PLATFORM-738 · IOSAdsResource.post（用途待确认）

- 接口声明：`POST /ios-ads`
- 输入字段：`token`, `device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:600` · `IOSAdsResource`

### PLATFORM-739 · AppCertResource.post（用途待确认）

- 接口声明：`POST /cert`
- 输入字段：`cert`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:616` · `AppCertResource`

### PLATFORM-740 · AppsflyerResource.post（用途待确认）

- 接口声明：`POST /appsflyer`
- 输入字段：`af_id`, `register_af_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/app.py:638` · `AppsflyerResource`

### PLATFORM-741 · app首页理财信息

- 接口声明：`GET /invest/summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:676` · `AppInvestSummaryResource`

### PLATFORM-742 · 客户端顶部市场列表 market_name: 兼容旧版本 client_top_markets: 客户端顶部市场配置列表

- 接口声明：`GET /homepage/market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/app.py:706` · `AppHomepageMarketResource`

### PLATFORM-743 · 提交定投计划 

- 接口声明：`POST /plans`
- 输入字段：`source_amount`, `source_stop_amount`, `market`, `cycle_type`, `invest_day`, `invest_time`, `hour_interval`, `notice_type`, `notice_value`, `timezone_offset`, `is_manual`
- 显式控制：require_login(allow_sub_account=False); trade_permission_validate(is_spot=True, account_id=0)
- 代码依据：`app/api/frontend/auto_invest.py:125` · `AutoInvestPlanResource`

### PLATFORM-744 · 定投计划列表 

- 接口声明：`GET /plans`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:232` · `AutoInvestPlanResource`

### PLATFORM-745 · AutoInvestPlansOrdersResource.get（用途待确认）

- 接口声明：`GET /plans/orders/<int:id_>`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:281` · `AutoInvestPlansOrdersResource`

### PLATFORM-746 · AutoInvestPlanResourceDetail.get（用途待确认）

- 接口声明：`GET /plans/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:332` · `AutoInvestPlanResourceDetail`

### PLATFORM-747 · AutoInvestPlanResourceDetail.put（用途待确认）

- 接口声明：`PUT /plans/<int:id_>`
- 输入字段：`source_amount`, `cycle_type`, `invest_day`, `invest_time`, `hour_interval`, `is_time_changed`, `source_stop_amount`, `notice_type`, `notice_value`, `timezone_offset`, `is_manual`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:380` · `AutoInvestPlanResourceDetail`

### PLATFORM-748 · 返回支持定投市场的最大定投市值，最小下单量（固定USDT：1） 

- 接口声明：`GET /markets/config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auto_invest.py:478` · `AutoInvestMarketsResource`

### PLATFORM-749 · AutoInvestPlanStatusResource.put（用途待确认）

- 接口声明：`PUT /plans/status/<int:id_>`
- 输入字段：`status`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:496` · `AutoInvestPlanStatusResource`

### PLATFORM-750 · AutoInvestPlanSliceOrderResource.get（用途待确认）

- 接口声明：`GET /plans/slice/orders/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:527` · `AutoInvestPlanSliceOrderResource`

### PLATFORM-751 · AutoInvestPlanSliceResource.get（用途待确认）

- 接口声明：`GET /plans/slice/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:557` · `AutoInvestPlanSliceResource`

### PLATFORM-752 · PlanInvestManualResource.post（用途待确认）

- 接口声明：`POST /plans/manual/<int:id_>`
- 输入字段：`source_amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/auto_invest.py:575` · `PlanInvestManualResource`

### PLATFORM-753 · DepositAddressesResource.get（用途待确认）

- 接口声明：`GET /deposit/address/list/<coin_type>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:21` · `DepositAddressesResource`

### PLATFORM-754 · DepositAddressResource.get（用途待确认）

- 接口声明：`GET /deposit/address/<coin_type>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:30` · `DepositAddressResource`

### PLATFORM-755 · DepositAddressResource.put（用途待确认）

- 接口声明：`PUT /deposit/address/<coin_type>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:34` · `DepositAddressResource`

### PLATFORM-756 · WithdrawalAddressesResource.get（用途待确认）

- 接口声明：`GET /withdraw/address`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:43` · `WithdrawalAddressesResource`

### PLATFORM-757 · WithdrawalAddressesResource.post（用途待确认）

- 接口声明：`POST /withdraw/address`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:47` · `WithdrawalAddressesResource`

### PLATFORM-758 · WithdrawalAddressResource.put（用途待确认）

- 接口声明：`PUT /withdraw/address/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:56` · `WithdrawalAddressResource`

### PLATFORM-759 · WithdrawalAddressResource.delete（用途待确认）

- 接口声明：`DELETE /withdraw/address/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:63` · `WithdrawalAddressResource`

### PLATFORM-760 · LocalWithdrawalAddressesResource.get（用途待确认）

- 接口声明：`GET /local/withdraw/address`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:72` · `LocalWithdrawalAddressesResource`

### PLATFORM-761 · LocalWithdrawalAddressesResource.post（用途待确认）

- 接口声明：`POST /local/withdraw/address`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:76` · `LocalWithdrawalAddressesResource`

### PLATFORM-762 · LocalWithdrawalAddressResource.put（用途待确认）

- 接口声明：`PUT /local/withdraw/address/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:85` · `LocalWithdrawalAddressResource`

### PLATFORM-763 · LocalWithdrawalAddressResource.delete（用途待确认）

- 接口声明：`DELETE /local/withdraw/address/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:89` · `LocalWithdrawalAddressResource`

### PLATFORM-764 · BitcoinCashAddressResource.post（用途待确认）

- 接口声明：`POST /bitcoin/cash/address`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:98` · `BitcoinCashAddressResource`

### PLATFORM-765 · WithdrawalAddressFromWithdrawalResource.post（用途待确认）

- 接口声明：`POST /coin/withdraw/address/<int:withdrawal_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:107` · `WithdrawalAddressFromWithdrawalResource`

### PLATFORM-766 · LocalWithdrawalAddressFromWithdrawalResource.post（用途待确认）

- 接口声明：`POST /coin/local/withdraw/address/<int:withdrawal_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/bank.py:116` · `LocalWithdrawalAddressFromWithdrawalResource`

### PLATFORM-767 · 尊享客户申请状态

- 接口声明：`GET /application/status`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:39` · `BigCustomerApplicationStatusResource`

### PLATFORM-768 · 尊享客户申请提交

- 接口声明：`POST /application`
- 输入字段：`name`, `telegram`, `exchanges`, `other_exchange_name`, `proof_file_ids`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:66` · `BigCustomerApplicationSubmitResource`

### PLATFORM-769 · 大客户相关的用户信息

- 接口声明：`GET /user-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:107` · `KaUserInfoResource`

### PLATFORM-770 · 已读提示

- 接口声明：`PATCH /user-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:170` · `KaUserInfoResource`

### PLATFORM-771 · 获取大客户群聊的信息（群里历史聊天人的头像、昵称）

- 接口声明：`GET /im-group-info`
- 输入字段：`im_group_id`, `role_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:190` · `ImGroupInfoResource`

### PLATFORM-772 · KA经理-我的大客户-标签选项

- 接口声明：`GET /manager/key-accounts/tags`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:303` · `ManagerKaTagsResource`

### PLATFORM-773 · KA经理-我的大客户-列表

- 接口声明：`GET /manager/key-accounts`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:333` · `ManagerKaListResource`

### PLATFORM-774 · KA经理-我的大客户-详情

- 接口声明：`GET /manager/key-accounts/<int:bc_user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:391` · `ManagerKaDetailResource`

### PLATFORM-775 · KA经理-我的大客户-编辑昵称、备注

- 接口声明：`PATCH /manager/key-accounts/<int:bc_user_id>`
- 输入字段：`nickname`, `remark`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:455` · `ManagerKaDetailResource`

### PLATFORM-776 · 获取域名白名单

- 接口声明：`GET /domain-whitelist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/big_customer.py:489` · `DomainWhitelistResource`

### PLATFORM-777 · GreetingSettingResource.get（用途待确认）

- 接口声明：`GET /manager/greeting-setting`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:518` · `GreetingSettingResource`

### PLATFORM-778 · GreetingSettingResource.patch（用途待确认）

- 接口声明：`PATCH /manager/greeting-setting`
- 输入字段：`greeting`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:526` · `GreetingSettingResource`

### PLATFORM-779 · ImGroupTopResource.get（用途待确认）

- 接口声明：`GET /im-group-top`
- 输入字段：`im_group_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:568` · `ImGroupTopResource`

### PLATFORM-780 · KA经理-我的大客户-增加置顶聊天

- 接口声明：`PUT /manager/im-group-top`
- 输入字段：`im_group_id`, `seq`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:638` · `ManagerImGroupTopResource`

### PLATFORM-781 · KA经理-我的大客户-取消置顶聊天

- 接口声明：`DELETE /manager/im-group-top`
- 输入字段：`im_group_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/big_customer.py:658` · `ManagerImGroupTopResource`

### PLATFORM-782 · 大客户相关系统消息

- 接口声明：`GET /im-message`
- 输入字段：`message_enum`, `params`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/big_customer.py:683` · `ImMessageResource`

### PLATFORM-783 · CategoryList.get（用途待确认）

- 接口声明：`GET /category-list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/blog.py:33` · `CategoryList`

### PLATFORM-784 · BlogList.get（用途待确认）

- 接口声明：`GET /list`
- 输入字段：`page`, `limit`, `category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/blog.py:70` · `BlogList`

### PLATFORM-785 · BlogPopular.get（用途待确认）

- 接口声明：`GET /popular`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/blog.py:140` · `BlogPopular`

### PLATFORM-786 · BlogDetail.get（用途待确认）

- 接口声明：`GET /detail`
- 输入字段：`blog_id`, `category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/blog.py:157` · `BlogDetail`

### PLATFORM-787 · 博客RSS

- 接口声明：`GET /rss`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/blog.py:364` · `BlogRSSResource`

### PLATFORM-788 · 提交经纪商申请 

- 接口声明：`POST /application`
- 输入字段：`name`, `contact_name`, `contact_info`, `city`, `type`, `contact_type`, `introduction`, `official_website`, `user_scale`, `trade_scale`, `extra_info`, `extra_data`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/broker.py:43` · `BrokerApplyResource`

### PLATFORM-789 · 经纪商信息

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:98` · `BrokerInfoResource`

### PLATFORM-790 · 设置经纪商用户返佣比例

- 接口声明：`POST /info/refer_user_rate`
- 输入字段：`refer_user_rate`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:145` · `BrokerInfoReferUserRateResource`

### PLATFORM-791 · 推广数据分析-经纪商返佣曲线(用户每日返佣数据表格) 

- 接口声明：`GET /series`
- 输入字段：`points`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:170` · `BrokerSeriesResource`

### PLATFORM-792 · 经纪商返佣历史 / 返佣记录 

- 接口声明：`GET /reports`
- 输入字段：`page`, `limit`, `code`, `report_type`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:243` · `BrokerReportResource`

### PLATFORM-793 · 明细-经纪商返佣历史 / 返佣记录 

- 接口声明：`GET /reports/detail`
- 输入字段：`report_date`, `report_type`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:332` · `BrokerReportDetailResource`

### PLATFORM-794 · 经纪商返佣历史 / 返佣记录-用户月度明细 

- 接口声明：`GET /reports/referral-detail`
- 输入字段：`user_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:410` · `BrokerReportReferralDetailResource`

### PLATFORM-795 · 经纪商图片/文件上传

- 接口声明：`POST /upload/file`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/broker.py:447` · `FileUploadResource`

### PLATFORM-796 · 获取Broker的活动列表

- 接口声明：`GET /activity/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:476` · `BrokerActivityListResource`

### PLATFORM-797 · 获取所有上线的（包括未开始）Broker活动

- 接口声明：`GET /activities/ongoing`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/broker.py:541` · `BrokerActiveActivityListResource`

### PLATFORM-798 · 获取Broker活动汇总数据

- 接口声明：`GET /activity/<int:activity_id>/summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:563` · `BrokerActivitySummaryResource`

### PLATFORM-799 · 获取Broker活动用户明细数据

- 接口声明：`GET /activity/<int:activity_id>/users`
- 输入字段：`page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/broker.py:628` · `BrokerActivityUsersResource`

### PLATFORM-800 · 发邮箱c-box

- 接口声明：`POST /by_email`
- 输入字段：`coin_type`, `c_box_type`, `total_amount`, `count`, `greeting`, `theme_id`, `only_new_user`, `valid_days`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/c_box.py:40` · `EmailCBoxResource`

### PLATFORM-801 · 领取邮箱c-box

- 接口声明：`PATCH /by_email`
- 输入字段：`c_box_id`, `body`, `sign`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/c_box.py:66` · `EmailCBoxResource`

### PLATFORM-802 · 发口令c-box

- 接口声明：`POST /by_code`
- 输入字段：`coin_type`, `c_box_type`, `total_amount`, `count`, `greeting`, `theme_id`, `code`, `valid_days`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/c_box.py:84` · `CodeCBoxResource`

### PLATFORM-803 · 领取口令c-box

- 接口声明：`PATCH /by_code`
- 输入字段：`code`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:111` · `CodeCBoxResource`

### PLATFORM-804 · 获取口令对应的c-box信息

- 接口声明：`GET /by_code`
- 输入字段：`code`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:123` · `CodeCBoxResource`

### PLATFORM-805 · 校验口令是否可用

- 接口声明：`GET /code/available`
- 输入字段：`code`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:140` · `CBoxCodeAvailableResource`

### PLATFORM-806 · 生成口令

- 接口声明：`POST /code`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:160` · `CBoxCodeResource`

### PLATFORM-807 · 获取主题列表

- 接口声明：`GET /themes`
- 输入字段：`version`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:174` · `CBoxThemeResource`

### PLATFORM-808 · c-box信息

- 接口声明：`GET /info/<string:encrypt_c_box_id>`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/c_box.py:190` · `CBoxInfoResource`

### PLATFORM-809 · 获取用户是否在admin配置了仅限新用户领取及是否设置了提现多人审核

- 接口声明：`GET /conf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:206` · `CBoxConfResource`

### PLATFORM-810 · 获取c-box验证信息

- 接口声明：`GET /verify`
- 输入字段：`c_box_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/c_box.py:220` · `ReceiveVerifyResource`

### PLATFORM-811 · 验证是否已领c-box

- 接口声明：`POST /verify`
- 输入字段：`c_box_id`, `body`, `sign`
- 显式控制：require_login
- 代码依据：`app/api/frontend/c_box.py:230` · `ReceiveVerifyResource`

### PLATFORM-812 · 获取c-box发送记录

- 接口声明：`GET /user/send_history`
- 输入字段：`start_time`, `end_time`, `coin_type`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:250` · `UserSendCBoxListResource`

### PLATFORM-813 · 获取领取c-box记录

- 接口声明：`GET /user/receive_history`
- 输入字段：`start_time`, `end_time`, `coin_type`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:272` · `UserReceiveCBoxListResource`

### PLATFORM-814 · c-box汇率，剩余额度

- 接口声明：`GET /rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:294` · `CBoxRateResource`

### PLATFORM-815 · c-box已发、剩余额度

- 接口声明：`GET /send-limit-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/c_box.py:323` · `CBoxSendLimitResource`

### PLATFORM-816 · c-box活动区推广展示

- 接口声明：`GET /promotion`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/c_box.py:347` · `CBoxPromotionResource`

### PLATFORM-817 · TelegramWebhookResource.post（用途待确认）

- 接口声明：`POST /telegram/<token>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/callback.py:44` · `TelegramWebhookResource`

### PLATFORM-818 · PaxfulCallBack.post（用途待确认）

- 接口声明：`POST /paxful`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/callback.py:121` · `PaxfulCallBack`

### PLATFORM-819 · XanPoolCallBack.post（用途待确认）

- 接口声明：`POST /xanpool`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/callback.py:153` · `XanPoolCallBack`

### PLATFORM-820 · 接收Sumsub回调结果

- 接口声明：`POST /sumsub`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/callback.py:194` · `SumsubCallBack`

### PLATFORM-821 · WhatsApp: 接收第三方回调结果

- 接口声明：`POST /whatsapp`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/callback.py:278` · `WhatsappMessageCallbackResource`

### PLATFORM-822 · Telegram: 接收第三方回调结果

- 接口声明：`POST /telegram`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/callback.py:334` · `TelegramMessageCallbackResource`

### PLATFORM-823 · PaybisCallBack.post（用途待确认）

- 接口声明：`POST /paybis`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/callback.py:408` · `PaybisCallBack`

### PLATFORM-824 · 首页-CoinEx合伙人-职位列表

- 接口声明：`GET /positions`
- 输入字段：`country`, `work_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/coinexpartner.py:16` · `PartnerPositionResource`

### PLATFORM-825 · 首页-CoinEx合伙人-职位详情

- 接口声明：`GET /position/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/coinexpartner.py:73` · `PartnerPositionDetailResource`

### PLATFORM-826 · CommentAtUserCheckResource.get（用途待确认）

- 接口声明：`GET /comment/at-user/check`
- 输入字段：`account_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/comment.py:53` · `CommentAtUserCheckResource`

### PLATFORM-827 · CommentTipLimitResource.get（用途待确认）

- 接口声明：`GET /comment-tip/tip-limit`
- 输入字段：`asset`
- 显式控制：require_login
- 代码依据：`app/api/frontend/comment.py:82` · `CommentTipLimitResource`

### PLATFORM-828 · CommentTipTransferResource.post（用途待确认）

- 接口声明：`POST /comment-tip/<int:comment_id>/tip`
- 输入字段：`receive_user_id`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/comment.py:103` · `CommentTipTransferResource`

### PLATFORM-829 · 支持跟单的市场列表 

- 接口声明：`GET /markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:313` · `CopyTradingMarketsResource`

### PLATFORM-830 · 跟单修改的配置 

- 接口声明：`GET /configs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:323` · `CopyTradingConfigsResource`

### PLATFORM-831 · 所有交易员 

- 接口声明：`GET /public/traders`
- 输入字段：`time_range`, `data_type`, `hide_full`, `nickname`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:341` · `PublicTradersResource`

### PLATFORM-832 · 带单人详情 

- 接口声明：`GET /public/trader-detail`
- 输入字段：`trader_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:494` · `PublicTraderDetailResource`

### PLATFORM-833 · 带单人-跟单人列表（当前跟单中的） 

- 接口声明：`GET /public/followers`
- 输入字段：`trader_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:545` · `PublicTraderFollowersResource`

### PLATFORM-834 · 带单人-当前带单的仓位 

- 接口声明：`GET /public/current-position`
- 输入字段：`trader_id`, `market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:657` · `PublicTraderCurrentPositionResource`

### PLATFORM-835 · 带单人-历史带单的仓位 

- 接口声明：`GET /public/finished-position`
- 输入字段：`trader_id`, `market`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:690` · `PublicTraderFinishedPositionResource`

### PLATFORM-836 · 带单人-统计数据-数据总览 

- 接口声明：`GET /public/trade-data`
- 输入字段：`trader_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:740` · `PublicTraderTradeDataResource`

### PLATFORM-837 · 带单人-统计数据-盈亏数据曲线 

- 接口声明：`GET /public/profit-series`
- 输入字段：`trader_id`, `time_range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:785` · `PublicTraderProfitSeriesResource`

### PLATFORM-838 · 带单人-统计数据-资产规模曲线 

- 接口声明：`GET /public/aum-series`
- 输入字段：`trader_id`, `time_range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:831` · `PublicTraderAumSeriesResource`

### PLATFORM-839 · 带单人-统计数据-合约交易偏好 

- 接口声明：`GET /public/market-percent`
- 输入字段：`trader_id`, `time_range`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/copy_trading.py:886` · `PublicTraderMarketPercentResource`

### PLATFORM-840 · 合约跟单交易的用户信息 

- 接口声明：`GET /user-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:911` · `CopyUserInfoResource`

### PLATFORM-841 · 获取带单人申请信息 

- 接口声明：`GET /trader/application`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:942` · `TraderApplicationResource`

### PLATFORM-842 · 提交带单人申请 

- 接口声明：`POST /trader/application`
- 输入字段：`nickname`, `contact`, `account_name`, `avatar`, `introduction`, `telegram`, `facebook`, `twitter`, `reddit`, `medium`, `discord`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/copy_trading.py:974` · `TraderApplicationResource`

### PLATFORM-843 · 带单人-修改个人信息 

- 接口声明：`PUT /trader/profile`
- 输入字段：`avatar`, `nickname`, `account_name`, `introduction`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/copy_trading.py:1002` · `TraderProfileResource`

### PLATFORM-844 · 带单人-修改带单参数设定 

- 接口声明：`PUT /trader/settings`
- 输入字段：`profit_share_rate`, `max_copy_amount`, `min_copy_amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/copy_trading.py:1023` · `TraderSettingsResource`

### PLATFORM-845 · 带单人-停止带单 

- 接口声明：`POST /trader/stop`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1046` · `TraderStopTradeResource`

### PLATFORM-846 · 带单人-获取可划转数 

- 接口声明：`GET /trader/transfer`
- 输入字段：`type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1086` · `TraderTransferResource`

### PLATFORM-847 · 带单人-划转资产（带单人 <--> 带单子帐号） 

- 接口声明：`POST /trader/transfer`
- 输入字段：`type`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1115` · `TraderTransferResource`

### PLATFORM-848 · 带单人-划转历史 

- 接口声明：`GET /trader/transfer-history`
- 输入字段：`trade_history_id`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1133` · `TraderTransferHistoryResource`

### PLATFORM-849 · 带单人-使用卡券 

- 接口声明：`POST /trader/coupon`
- 输入字段：`user_coupon_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1205` · `TraderCouponResource`

### PLATFORM-850 · 带单人-分润记录 

- 接口声明：`GET /trader/profit-share-history`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1222` · `TraderProfitShareHistoryResource`

### PLATFORM-851 · 带单人-分润汇总信息 

- 接口声明：`GET /trader/profit-share-summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1276` · `TraderProfitShareSummaryResource`

### PLATFORM-852 · 带单人-跟单人列表（带单人自身视角） 

- 接口声明：`GET /trader/followers`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1307` · `TraderFollowersResource`

### PLATFORM-853 · 我关注的交易员 

- 接口声明：`GET /follower/favorite`
- 输入字段：`nickname`, `hide_full`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1380` · `FollowerFavoriteTradersResource`

### PLATFORM-854 · 关注交易员 

- 接口声明：`POST /follower/favorite`
- 输入字段：`trader_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1477` · `FollowerFavoriteTradersResource`

### PLATFORM-855 · 取消关注交易员 

- 接口声明：`DELETE /follower/favorite`
- 输入字段：`trader_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1489` · `FollowerFavoriteTradersResource`

### PLATFORM-856 · 跟单人-开始跟单 

- 接口声明：`POST /follower/start`
- 输入字段：`trader_id`, `margin_type`, `leverage_type`, `add_margin_amount`, `user_coupon_id`, `profit_trigger_rate`, `loss_trigger_rate`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1506` · `FollowerStartFollowResource`

### PLATFORM-857 · 跟单人-停止跟单预览 

- 接口声明：`GET /follower/stop-preview`
- 输入字段：`trader_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1528` · `FollowerStopFollowPreviewResource`

### PLATFORM-858 · 跟单人-停止跟单 

- 接口声明：`POST /follower/stop`
- 输入字段：`trader_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1583` · `FollowerStopFollowResource`

### PLATFORM-859 · 跟单人-修改跟单参数设定 

- 接口声明：`PUT /follower/settings`
- 输入字段：`trader_id`, `margin_type`, `leverage_type`, `add_margin_amount`, `user_coupon_id`, `profit_trigger_rate`, `loss_trigger_rate`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1600` · `FollowerSettingsResource`

### PLATFORM-860 · 跟单人-增加保证金（仓位是跟单子帐号的）

- 接口声明：`POST /follower/margin/adjust`
- 输入字段：`market`, `follow_history_id`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1623` · `FollowerAdjustPositionMarginResource`

### PLATFORM-861 · 跟单人-划转历史 

- 接口声明：`GET /follower/transfer-history`
- 输入字段：`follow_history_id`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1640` · `FollowerTransferHistoryResource`

### PLATFORM-862 · 跟单人-跟单数据统计 

- 接口声明：`GET /follower/follow-data`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1710` · `FollowerFollowDataResource`

### PLATFORM-863 · 跟单人-当前跟单 

- 接口声明：`GET /follower/current-follow`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1753` · `FollowerCurrentFollowResource`

### PLATFORM-864 · 跟单人-历史跟单 

- 接口声明：`GET /follower/finished-follow`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1798` · `FollowerFinishedFollowResource`

### PLATFORM-865 · 跟单人-跟单详情 

- 接口声明：`GET /follower/follow-detail`
- 输入字段：`id`, `trader_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1866` · `FollowerFollowDetailResource`

### PLATFORM-866 · 跟单人-跟单详情-当前仓位 

- 接口声明：`GET /follower/current-position`
- 输入字段：`follow_history_id`, `market`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:1984` · `FollowerCurrentPositionResource`

### PLATFORM-867 · 跟单人-跟单详情-历史仓位 

- 接口声明：`GET /follower/finished-position`
- 输入字段：`follow_history_id`, `market`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:2012` · `FollowerFinishedPositionResource`

### PLATFORM-868 · 跟单人-跟单详情-当前仓位 一键平仓 

- 接口声明：`POST /follower/close-position`
- 输入字段：`follow_history_id`, `market`
- 显式控制：require_login(allow_sub_account=False); trade_permission_validate(is_spot=False, is_closing_or_reducing_position=True)
- 代码依据：`app/api/frontend/copy_trading.py:2071` · `FollowerMarketClosePositionResource`

### PLATFORM-869 · 跟单人-跟单详情-分润记录 

- 接口声明：`GET /follower/profit-share-history`
- 输入字段：`follow_history_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/copy_trading.py:2090` · `FollowerProfitShareHistoryResource`

### PLATFORM-870 · 获取资产托管平台列表

- 接口声明：`GET /platforms`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/custody.py:16` · `AssetCustodyPlatformsResource`

### PLATFORM-871 · AssetCustodyUserInfoResource.get（用途待确认）

- 接口声明：`GET /user/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/custody.py:33` · `AssetCustodyUserInfoResource`

### PLATFORM-872 · 紧急联系人-获取

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/emergency_contact.py:26` · `EmergencyContactResource`

### PLATFORM-873 · 紧急联系人-添加

- 接口声明：`POST `
- 输入字段：`name`, `email`, `user_message`, `dormancy_period`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/emergency_contact.py:44` · `EmergencyContactResource`

### PLATFORM-874 · 紧急联系人-修改

- 接口声明：`PUT `
- 输入字段：`name`, `email`, `user_message`, `dormancy_period`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/emergency_contact.py:79` · `EmergencyContactResource`

### PLATFORM-875 · 紧急联系人-删除

- 接口声明：`DELETE `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/emergency_contact.py:104` · `EmergencyContactResource`

### PLATFORM-876 · FileUrlsResource.get（用途待确认）

- 接口声明：`GET /urls`
- 输入字段：`file_ids`
- 显式控制：require_login
- 代码依据：`app/api/frontend/file.py:24` · `FileUrlsResource`

### PLATFORM-877 · JsonFileResource.get（用途待确认）

- 接口声明：`GET /json`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/file_config.py:17` · `JsonFileResource`

### PLATFORM-878 · 获取搜索栏限时活动

- 接口声明：`GET /limited-time-activity`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/global_search.py:22` · `LimitedTimeActivityResource`

### PLATFORM-879 · GlobalSearchContentResource.get（用途待确认）

- 接口声明：`GET /content`
- 输入字段：`q`, `code`, `last_id`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/global_search.py:42` · `GlobalSearchContentResource`

### PLATFORM-880 · GlobalSearchInvestmentResource.get（用途待确认）

- 接口声明：`GET /investment`
- 输入字段：`q`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/global_search.py:92` · `GlobalSearchInvestmentResource`

### PLATFORM-881 · 获取搜索栏相关功能配置

- 接口声明：`GET /related-functions`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/global_search.py:140` · `GlobalSearchRelatedFunctionResource`

### PLATFORM-882 · InsightPublicAreaResource.get（用途待确认）

- 接口声明：`GET /public-area`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:62` · `InsightPublicAreaResource`

### PLATFORM-883 · ListResource.get（用途待确认）

- 接口声明：`GET /<article_type>`
- 输入字段：`last_id`, `report_type`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:77` · `ListResource`

### PLATFORM-884 · LastListResource.get（用途待确认）

- 接口声明：`GET /last`
- 输入字段：`last_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:106` · `LastListResource`

### PLATFORM-885 · DetailsResource.get（用途待确认）

- 接口声明：`GET /<article_type>/<object_id>`
- 输入字段：`report_type`, `rss_channel`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:120` · `DetailsResource`

### PLATFORM-886 · SearchResource.get（用途待确认）

- 接口声明：`GET /search`
- 输入字段：`search_key`, `last_id`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:210` · `SearchResource`

### PLATFORM-887 · SitemapResource.get（用途待确认）

- 接口声明：`GET /sitemap`
- 输入字段：`limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:235` · `SitemapResource`

### PLATFORM-888 · HotInsightResource.get（用途待确认）

- 接口声明：`GET /hot`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:263` · `HotInsightResource`

### PLATFORM-889 · Insight RSS

- 接口声明：`GET /feed/<lang>/<channel>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/insight.py:277` · `InsightRSSResource`

### PLATFORM-890 · LaunchPool 项目列表 

- 接口声明：`GET /projects`
- 输入字段：`ids`, `scope`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/launch_pool.py:90` · `LaunchPoolProjectsResource`

### PLATFORM-891 · LaunchPool 项目详情 

- 接口声明：`GET /project/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/launch_pool.py:171` · `LaunchPoolProjectDetailResource`

### PLATFORM-892 · LaunchPool 奖励币种列表 

- 接口声明：`GET /reward-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/launch_pool.py:186` · `LaunchPoolRewardAssetsResource`

### PLATFORM-893 · 用户挖矿协议状态 

- 接口声明：`GET /opening-agreement`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/launch_pool.py:198` · `UserOpeningAgreementResource`

### PLATFORM-894 · 用户同意挖矿协议 

- 接口声明：`POST /opening-agreement`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/launch_pool.py:208` · `UserOpeningAgreementResource`

### PLATFORM-895 · 用户参与信息 

- 接口声明：`GET /user-info`
- 输入字段：`project_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/launch_pool.py:221` · `LaunchPoolUserInfoResource`

### PLATFORM-896 · 用户存入质押币 

- 接口声明：`POST /stake`
- 输入字段：`pool_id`, `amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/launch_pool.py:293` · `LaunchPoolStakeOperateResource`

### PLATFORM-897 · 用户取出质押币 

- 接口声明：`DELETE /stake`
- 输入字段：`pool_id`, `amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/launch_pool.py:337` · `LaunchPoolStakeOperateResource`

### PLATFORM-898 · 历史收益记录 

- 接口声明：`GET /reward-history`
- 输入字段：`reward_asset`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/launch_pool.py:373` · `LaunchPoolRewardHistoryResource`

### PLATFORM-899 · 挖矿操作记录 

- 接口声明：`GET /operate-history`
- 输入字段：`reward_asset`, `type`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/launch_pool.py:437` · `LaunchPoolOperateHistoryResource`

### PLATFORM-900 · 获取直播页信息

- 接口声明：`GET /<string:live_page_uid>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/live.py:14` · `QuestionnaireResource`

### PLATFORM-901 · 充值关闭信息 

- 接口声明：`GET /deposit`
- 输入字段：`asset`, `chain`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:32` · `DepositMaintainInfosResource`

### PLATFORM-902 · 提现关闭信息 

- 接口声明：`GET /withdrawal`
- 输入字段：`asset`, `chain`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:54` · `WithdrawMaintainInfosResource`

### PLATFORM-903 · 所有充值/提现关闭信息（仅当所有链都关闭时）

- 接口声明：`GET /deposit-withdrawal`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:76` · `DepositWithdrawMaintainInfosResource`

### PLATFORM-904 · 充值、提现恢复邮件通知, 用户订阅状态 

- 接口声明：`GET /<type_>/subscription`
- 输入字段：`asset`, `chain`
- 显式控制：require_login
- 代码依据：`app/api/frontend/maintain.py:85` · `DepositWithdrawMaintainSubscriptionResource`

### PLATFORM-905 · 充值、提现-设置恢复邮件提醒 

- 接口声明：`POST /<type_>/subscription`
- 输入字段：`asset`, `chain`
- 显式控制：require_login
- 代码依据：`app/api/frontend/maintain.py:107` · `DepositWithdrawMaintainSubscriptionResource`

### PLATFORM-906 · 充值、提现恢复-取消邮件提醒 

- 接口声明：`DELETE /<type_>/subscription`
- 输入字段：`asset`, `chain`
- 显式控制：require_login
- 代码依据：`app/api/frontend/maintain.py:135` · `DepositWithdrawMaintainSubscriptionResource`

### PLATFORM-907 · 充值、提现 弹窗列表 

- 接口声明：`GET /<trigger_page>/popup-windows`
- 输入字段：`asset`, `chain`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:161` · `DepositPopupWindowsResource`

### PLATFORM-908 · DepositPopupWindowsOfflineResource.get（用途待确认）

- 接口声明：`GET /popup-windows/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:208` · `DepositPopupWindowsOfflineResource`

### PLATFORM-909 · 临时维护信息(用于维护时前端蒙层) 

- 接口声明：`GET /temp`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:223` · `MaintainTempResource`

### PLATFORM-910 · 临时维护信息详情（用于维护前10分钟给用户弹窗） 

- 接口声明：`GET /temp/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:237` · `MaintainTempDetailResource`

### PLATFORM-911 · 单市场停服护信息(用于维护时前端蒙层) 

- 接口声明：`GET /market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/maintain.py:268` · `MarketMaintainResource`

### PLATFORM-912 · OnchainConfigResource.get（用途待确认）

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/config.py:44` · `OnchainConfigResource`

### PLATFORM-913 · OnchainConfigChainResource.get（用途待确认）

- 接口声明：`GET /chain`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/config.py:64` · `OnchainConfigChainResource`

### PLATFORM-914 · DailyBuyLimitResource.post（用途待确认）

- 接口声明：`POST /daily/buy/limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/config.py:90` · `DailyBuyLimitResource`

### PLATFORM-915 · OnchainTokenHotResource.get（用途待确认）

- 接口声明：`GET /hot`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/token.py:67` · `OnchainTokenHotResource`

### PLATFORM-916 · OnchainTokenRWAResource.get（用途待确认）

- 接口声明：`GET /rwa`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/token.py:89` · `OnchainTokenRWAResource`

### PLATFORM-917 · OnchainTokenResource.get（用途待确认）

- 接口声明：`GET /<int:token_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/token.py:152` · `OnchainTokenResource`

### PLATFORM-918 · OnchainTokenSearchResource.get（用途待确认）

- 接口声明：`GET /search`
- 输入字段：`contract`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/token.py:279` · `OnchainTokenSearchResource`

### PLATFORM-919 · OnchainTokenIDResource.get（用途待确认）

- 接口声明：`GET /id`
- 输入字段：`chain`, `contract`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/token.py:336` · `OnchainTokenIDResource`

### PLATFORM-920 · OnchainTokenKlineResource.get（用途待确认）

- 接口声明：`GET /<int:token_id>/kline`
- 输入字段：`start_time`, `end_time`, `interval`, `currency`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/token.py:354` · `OnchainTokenKlineResource`

### PLATFORM-921 · OnchainTokenBalanceResource.get（用途待确认）

- 接口声明：`GET /balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/token.py:388` · `OnchainTokenBalanceResource`

### PLATFORM-922 · OnchainTokenFavoriteResource.get（用途待确认）

- 接口声明：`GET /favorite`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/token.py:418` · `OnchainTokenFavoriteResource`

### PLATFORM-923 · OnchainTokenFavoriteResource.post（用途待确认）

- 接口声明：`POST /favorite`
- 输入字段：`token_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/token.py:423` · `OnchainTokenFavoriteResource`

### PLATFORM-924 · OnchainTokenFavoriteResource.delete（用途待确认）

- 接口声明：`DELETE /favorite`
- 输入字段：`token_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/onchain/token.py:435` · `OnchainTokenFavoriteResource`

### PLATFORM-925 · OnchainTokenQuoteBatchResource.get（用途待确认）

- 接口声明：`GET /quote/batch`
- 输入字段：`token_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/onchain/token.py:453` · `OnchainTokenQuoteBatchResource`

### PLATFORM-926 · 发行币种列表 

- 接口声明：`GET /token-list`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/pre_trading.py:72` · `PreTokenListResource`

### PLATFORM-927 · 发行币种详情 

- 接口声明：`GET /token-detail`
- 输入字段：`asset`, `market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/pre_trading.py:137` · `PreTokenDetailResource`

### PLATFORM-928 · 发行操作 

- 接口声明：`POST /issue`
- 输入字段：`asset`, `pledge_amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pre_trading.py:216` · `UserPreIssueResource`

### PLATFORM-929 · 赎回操作 

- 接口声明：`POST /redeem`
- 输入字段：`asset`, `amount`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/pre_trading.py:272` · `UserPreRedeemResource`

### PLATFORM-930 · 我的PreToken 

- 接口声明：`GET /position`
- 输入字段：`asset`
- 显式控制：require_login
- 代码依据：`app/api/frontend/pre_trading.py:316` · `UserPrePositionResource`

### PLATFORM-931 · 全部的已质押的资产，用于前端总资产计算 

- 接口声明：`GET /pledge-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/pre_trading.py:383` · `UserPledgeAssetsResource`

### PLATFORM-932 · 用户操作明细记录 

- 接口声明：`GET /operate-history`
- 输入字段：`asset`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/pre_trading.py:407` · `PreTradingOperateHistoryResource`

### PLATFORM-933 · MarketDataResource.get（用途待确认）

- 接口声明：`GET /market`
- 输入字段：`market`, `margin`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:49` · `MarketDataResource`

### PLATFORM-934 · DealDataResource.get（用途待确认）

- 接口声明：`GET /deal`
- 输入字段：`market`, `start_time`, `end_time`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:72` · `DealDataResource`

### PLATFORM-935 · AccountProfitLossResource.get（用途待确认）

- 接口声明：`GET /account`
- 输入字段：`account_type`, `start_time`, `end_time`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:95` · `AccountProfitLossResource`

### PLATFORM-936 · AccountRealtimeProfitLossResource.get（用途待确认）

- 接口声明：`GET /account/realtime`
- 输入字段：`account_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:168` · `AccountRealtimeProfitLossResource`

### PLATFORM-937 · AccountSummaryResource.get（用途待确认）

- 接口声明：`GET /account/summary`
- 输入字段：`start_time`, `end_time`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:229` · `AccountSummaryResource`

### PLATFORM-938 · AccountAssetPercentResource.get（用途待确认）

- 接口声明：`GET /account/asset/percent`
- 输入字段：`account_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:282` · `AccountAssetPercentResource`

### PLATFORM-939 · 盈亏分析-交易额曲线

- 接口声明：`GET /account/deal`
- 输入字段：`account_type`, `start_time`, `end_time`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:305` · `AccountDealValueResource`

### PLATFORM-940 · 盈亏分析-币种维度盈亏(现货)

- 接口声明：`GET /asset`
- 输入字段：`asset`, `start_time`, `end_time`, `series_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/profit_loss.py:447` · `AssetProfitLossResource`

### PLATFORM-941 · 币种资料

- 接口声明：`GET /project`
- 输入字段：`online_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:85` · `CoinInformationList`

### PLATFORM-942 · 币种申请

- 接口声明：`POST /project`
- 输入字段：`logo`, `short_name`, `full_name`, `chain_type`, `issue_type`, `issue_time`, `issue_amount`, `total_circulate`, `usd_circulate`, `issue_price`, `website_url`, `white_paper_url`, `src_url`, `browser_url`, `social_url`, `introduction_en`, `introduction_cn`, `introduction`, `fundraising`, `token_distribution`, `linkedin_or_cv`, `applicant_name`, `applicant_role`, `applicant_email`, `applicant_mobile`, `vote_type`, `coin_id`, `securities_id`, `commitment_id`, `law_ids`, `audit_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:124` · `CoinInformationList`

### PLATFORM-943 · 币种检查

- 接口声明：`GET /project/check`
- 输入字段：`full_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:272` · `ProjectCheckResource`

### PLATFORM-944 · ProjectIdMappingResource.get（用途待确认）

- 接口声明：`GET /project/idmap`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:291` · `ProjectIdMappingResource`

### PLATFORM-945 · CoinInformationResource.get（用途待确认）

- 接口声明：`GET /project/<coin_str>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:307` · `CoinInformationResource`

### PLATFORM-946 · CoinIncomeRateResource.get（用途待确认）

- 接口声明：`GET /project/<coin_str>/income-rate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:337` · `CoinIncomeRateResource`

### PLATFORM-947 · FileUploadResource.post（用途待确认）

- 接口声明：`POST /upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:357` · `FileUploadResource`

### PLATFORM-948 · 融资申请

- 接口声明：`POST /ieo`
- 输入字段：`logo`, `short_name`, `full_name`, `chain_type`, `issue_type`, `issue_time`, `issue_amount`, `total_circulate`, `usd_circulate`, `website_url`, `white_paper_url`, `src_url`, `browser_url`, `social_url`, `introduction_en`, `introduction_cn`, `introduction`, `fundraising`, `token_distribution`, `linkedin_or_cv`, `applicant_name`, `applicant_role`, `applicant_email`, `applicant_telegram`, `vote_type`, `coin_id`, `securities_id`, `commitment_id`, `law_ids`, `audit_id`, `avg_price`, `issue_price`, `discount`, `is_locked`, `unlock_condition`, `product_url`, `test_code`, `support_chain_url`
- 显式控制：require_login
- 代码依据：`app/api/frontend/project.py:401` · `IeoInformationList`

### PLATFORM-949 · KolApplyResource.get（用途待确认）

- 接口声明：`GET /kol`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/project.py:554` · `KolApplyResource`

### PLATFORM-950 · KolApplyResource.post（用途待确认）

- 接口声明：`POST /kol`
- 输入字段：`account_platform`, `account_link`, `fans_range`, `average_views`, `update_frequency`, `account_created_at`, `country_and_city`, `other_contact`, `expected_salary`, `expectations`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/project.py:576` · `KolApplyResource`

### PLATFORM-951 · KolApplyDetailResource.put（用途待确认）

- 接口声明：`PUT /kol/<int:apply_id>`
- 输入字段：`account_platform`, `account_link`, `fans_range`, `average_views`, `update_frequency`, `account_created_at`, `country_and_city`, `other_contact`, `expected_salary`, `expectations`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/project.py:631` · `KolApplyDetailResource`

### PLATFORM-952 · 币种资料页-币种是否存在价格、区间涨跌幅、市场信息及币种活动信息

- 接口声明：`GET /coin-info/<string:coin>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/project.py:684` · `CoinPageInfoResource`

### PLATFORM-953 · 获取问卷

- 接口声明：`GET /<string:q_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/questionnaire.py:31` · `QuestionnaireResource`

### PLATFORM-954 · 提交问卷

- 接口声明：`POST /<string:q_id>`
- 输入字段：`time`, `platform`, `answers`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/questionnaire.py:73` · `QuestionnaireResource`

### PLATFORM-955 · 问卷上传文件

- 接口声明：`POST /upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/questionnaire.py:175` · `QuestionnaireUploadResource`

### PLATFORM-956 · 用户自选币种

- 接口声明：`GET /favorite/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/quotes.py:56` · `FavoriteAssets`

### PLATFORM-957 · FavoriteAssets.post（用途待确认）

- 接口声明：`POST /favorite/assets`
- 输入字段：`assets`
- 显式控制：require_login
- 代码依据：`app/api/frontend/quotes.py:63` · `FavoriteAssets`

### PLATFORM-958 · FavoriteAssets.put（用途待确认）

- 接口声明：`PUT /favorite/assets`
- 输入字段：`assets`
- 显式控制：require_login
- 代码依据：`app/api/frontend/quotes.py:78` · `FavoriteAssets`

### PLATFORM-959 · FavoriteAssets.delete（用途待确认）

- 接口声明：`DELETE /favorite/assets`
- 输入字段：`asset`
- 显式控制：require_login
- 代码依据：`app/api/frontend/quotes.py:94` · `FavoriteAssets`

### PLATFORM-960 · 用户持仓币种 

- 接口声明：`GET /own/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/quotes.py:134` · `OwnAssets`

### PLATFORM-961 · 编辑持仓币种的排序 

- 接口声明：`POST /own/assets`
- 输入字段：`assets`
- 显式控制：require_login
- 代码依据：`app/api/frontend/quotes.py:144` · `OwnAssets`

### PLATFORM-962 · 单个币种的k线数据

- 接口声明：`GET /asset/<asset>`
- 输入字段：`start`, `end`, `period`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:166` · `AssetQuotes`

### PLATFORM-963 · AssetsVolatility.get（用途待确认）

- 接口声明：`GET /asset/volatility/<asset>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:194` · `AssetsVolatility`

### PLATFORM-964 · AssetsVolatilityList.get（用途待确认）

- 接口声明：`GET /asset/volatility/list`
- 输入字段：`assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:212` · `AssetsVolatilityList`

### PLATFORM-965 · 所有币种

- 接口声明：`GET /assets`
- 输入字段：`sort_type`, `tag_id`, `query_type`, `offset`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:276` · `AssetsQuotes`

### PLATFORM-966 · 首页币种排行榜

- 接口声明：`GET /rank/assets`
- 输入字段：`sort_type`, `is_kline`, `offset`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:438` · `HomePageAssetsQuotes`

### PLATFORM-967 · 涨幅榜单被限制币种

- 接口声明：`GET /rank/restricted-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:486` · `RestrictedAssetsQuotes`

### PLATFORM-968 · 所有标签，已废弃，兼容APP保留 

- 接口声明：`GET /tags`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:501` · `Tags`

### PLATFORM-969 · 所有标签的信息 

- 接口声明：`GET /tags/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:512` · `TagsInfo`

### PLATFORM-970 · 所有标签的行情数据 

- 接口声明：`GET /tags/data`
- 输入字段：`tag_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:536` · `TagsData`

### PLATFORM-971 · 新币专区-即将上线

- 接口声明：`GET /new/soon/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:557` · `NewSoonAssetsQuotes`

### PLATFORM-972 · 新币专区-最近上线

- 接口声明：`GET /new/recent/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:582` · `NewRecentAssetsQuotes`

### PLATFORM-973 · 所有专题 

- 接口声明：`GET /topics`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:605` · `Topics`

### PLATFORM-974 · AssetTrendingResource.get（用途待确认）

- 接口声明：`GET /asset/trending`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:615` · `AssetTrendingResource`

### PLATFORM-975 · MarketTrendingResource.get（用途待确认）

- 接口声明：`GET /market/trending`
- 输入字段：`trade_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:643` · `MarketTrendingResource`

### PLATFORM-976 · AssetsShowResource.get（用途待确认）

- 接口声明：`GET /assets/show`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:662` · `AssetsShowResource`

### PLATFORM-977 · DepositWithdrawalTrendingResource.get（用途待确认）

- 接口声明：`GET /deposit/withdrawal/trending`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:714` · `DepositWithdrawalTrendingResource`

### PLATFORM-978 · SearchClickResource.post（用途待确认）

- 接口声明：`POST /search/click`
- 输入字段：`value`, `search_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/quotes.py:774` · `SearchClickResource`

### PLATFORM-979 · 币种是否被标记为st（即将下架币种）

- 接口声明：`GET /st-check/<coin>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:803` · `StCheckResource`

### PLATFORM-980 · 现货资产历史流通市值

- 接口声明：`GET /circulation/series`
- 输入字段：`interval`, `assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:899` · `CirculationHistoryResource`

### PLATFORM-981 · 现货资产历史成交

- 接口声明：`GET /deal/series`
- 输入字段：`interval`, `assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:940` · `DealHistoryResource`

### PLATFORM-982 · UpDownDistribution.get（用途待确认）

- 接口声明：`GET /up-down-distribution`
- 输入字段：`interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:976` · `UpDownDistribution`

### PLATFORM-983 · BuySellDistribution.get（用途待确认）

- 接口声明：`GET /buy-sell-distribution`
- 输入字段：`interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:998` · `BuySellDistribution`

### PLATFORM-984 · return：给定币种列表近实时价格。如果给定列表中有币种不存在，则返回字典会忽略这个币种。

- 接口声明：`GET /real-time/assets`
- 输入字段：`assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:1029` · `AssetsPricesResource`

### PLATFORM-985 · return：给定币种列表近实时价格。如果给定列表中有币种不存在，则返回字典会忽略这个币种。

- 接口声明：`POST /real-time/assets`
- 输入字段：`assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:1041` · `AssetsPricesResource`

### PLATFORM-986 · ToOnlineAssetResource.get（用途待确认）

- 接口声明：`GET /to-online/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:1082` · `ToOnlineAssetResource`

### PLATFORM-987 · 币种行情信息概览-目前用于学院文章

- 接口声明：`GET /assets/overview`
- 输入字段：`assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:1095` · `AssetsQuotesOverview`

### PLATFORM-988 · 批量获取币种实时行情，用于 客户端行情组件 展示  Args:     assets (str): 逗号分隔的币种列表，如 CET,ETH,BTC，最多 10 个  Returns:     asset (str): 币种名称     price_usd (str): 当前 USD 价格     change_rate (str): 24小时涨跌幅     

- 接口声明：`GET /asset/widget`
- 输入字段：`assets`, `with_kline`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/quotes.py:1125` · `AssetWidgetResource`

### PLATFORM-989 · 首页-CoinEx 招聘-职位列表

- 接口声明：`GET /jobs`
- 输入字段：`job_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/recruit.py:50` · `JobsResource`

### PLATFORM-990 · JobResource.get（用途待确认）

- 接口声明：`GET /job/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/recruit.py:95` · `JobResource`

### PLATFORM-991 · 任务中心-我的奖励 

- 接口声明：`GET /rewards`
- 输入字段：`reward_type`, `status`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:80` · `RewardCenterRewardsResource`

### PLATFORM-992 · 任务中心-我的奖励详情 

- 接口声明：`GET /reward-detail`
- 输入字段：`reward_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:544` · `RewardCenterRewardDetailResource`

### PLATFORM-993 · 任务中心-我的奖励总额 

- 接口声明：`GET /total-reward`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:573` · `RewardCenterTotalRewardResource`

### PLATFORM-994 · 任务中心-剩余返现USD额度汇总 

- 接口声明：`GET /remain-cashback`
- 输入字段：`cashback_scope`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:675` · `RewardCenterRemainCashbackResource`

### PLATFORM-995 · 任务中心-返现权益奖励弹窗列表 

- 接口声明：`GET /cashback-rewards`
- 输入字段：`cashback_scope`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:727` · `CashBackRewardsResource`

### PLATFORM-996 · 任务中心-理财加息权益奖励弹窗列表 

- 接口声明：`GET /invest-increase-rewards`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:791` · `InvestIncreaseRewardsResource`

### PLATFORM-997 · 用户选择理财加息币种

- 接口声明：`POST /invest-increase-asset`
- 输入字段：`user_equity_id`, `asset`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:812` · `InvestIncreaseAssetResource`

### PLATFORM-998 · 任务中心-合约体验金权益奖励弹窗列表 展示逻辑: 1. 如果有正在使用中的体验金，则展示在当前仓位的市场 2. 如果没有正在使用中的体验金，则展示在所有市场的体验金中，按照过期时间倒序，金额降序倒序 market为空时，展示所有市场的体验金

- 接口声明：`GET /perpetual-trial-rewards`
- 输入字段：`market`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:878` · `PerpetualTrialRewardsResource`

### PLATFORM-999 · 合约体验金-当前已实现盈亏

- 接口声明：`GET /perpetual-trial/current-balance`
- 输入字段：`reward_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:975` · `PerpetualTrialCurrentBalanceResource`

### PLATFORM-1000 · 合约体验金-简单详情

- 接口声明：`GET /perpetual-trial/simple-detail`
- 输入字段：`reward_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/reward_center.py:1061` · `PerpetualTrialSimpleDetailResource`

### PLATFORM-1001 · EmailUnsubscriptionResource.post（用途待确认）

- 接口声明：`POST /email/unsubscribe`
- 输入字段：`unsub`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/safety.py:47` · `EmailUnsubscriptionResource`

### PLATFORM-1002 · NoticeResource.get（用途待确认）

- 接口声明：`GET /notice`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/safety.py:73` · `NoticeResource`

### PLATFORM-1003 · NoticeResource.put（用途待确认）

- 接口声明：`PUT /notice`
- 输入字段：`has_announcement_notice`, `has_activity_notice`, `has_blog_notice`
- 显式控制：require_login
- 代码依据：`app/api/frontend/safety.py:84` · `NoticeResource`

### PLATFORM-1004 · SettingResource.get（用途待确认）

- 接口声明：`GET /setting`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/safety.py:126` · `SettingResource`

### PLATFORM-1005 · SettingResource.put（用途待确认）

- 接口声明：`PUT /setting`
- 输入字段：`allows_announcement_navigation`, `allows_announcement_emails`, `allows_activity_emails`, `allows_blog_emails`, `allows_deposit_withdrawal_emails`, `opening_account_profit_loss`, `auto_put_margin_loan_order`, `auto_flat_margin_loan_order`, `perpetual_pricing_basis`, `spot_order_confirmation`, `perpetual_order_confirmation`, `allows_announcement_app`, `allows_activity_app`, `allows_blog_app`, `app_spot_margin_prediction_new_asset_notice`, `app_perpetual_new_asset_notice`, `app_product_new_notice`, `app_reward_center_notice`, `app_deposit_withdrawal_notice`, `app_deposit_notice`, `app_withdrawal_notice`, `app_payment_received_notice`, `app_exchange_notice`, `app_ieo_notice`, `app_holding_asset_notice`, `app_favorite_asset_notice`, `app_spot_limit_order_notice`, `app_spot_stop_order_notice`, `app_perpetual_limit_order_notice`, `app_perpetual_stop_order_notice`, `app_perpetual_profit_loss_notice`, `app_big_customer_receive_manager_message_notice`, `app_manager_receive_big_customer_message_notice`, `opening_sub_account_function`, `guide_type`, `opening_withdraw_password`, `opening_withdraw_password_for_payment`, `opening_trade_password`, `opening_web_login_ip_locking`, `opening_web_security_login_duration`, `opening_direct_fiat`, `withdraw_password`, `news_popup_display`, `app_information_notice`, `withdrawal_fee_asset`, `p2p_trade_fiat`, `p2p_question`, `app_spot_grid_take_profit_notice`, `app_spot_grid_stop_loss_notice`, `app_spot_grid_exceed_price_notice`, `app_auto_invest_profit_arrive_notice`, `view_coinex_protocol`, `only_allow_sms_verification`, `app_asset_level_break_notice`, `app_new_asset_rise_notice`, `view_comment_user_tos`, `view_comment_user_agreement`, `user_info_confirmed_for_comment`, `app_comment_message_up_notice`, `app_comment_message_reply_notice`, `app_comment_message_at_notice`, `app_comment_message_tip_notice`, `opening_onchain_trade_function`, `opening_onchain_rwa_function`, `finish_perpetual_tutorial_question`, `finish_margin_tutorial_question`, `perpetual_dormancy_days`
- 显式控制：require_login; ns.use_kwargs(dict(allows_announcement_navigation=fields.Boolean(), allows_announcement_emails=fields.Boolean(), allows_activity_emails=fields.Boolean(), allows_blog
- 代码依据：`app/api/frontend/safety.py:135` · `SettingResource`

### PLATFORM-1006 · 短链接重定向 

- 接口声明：`GET /<short_url>`
- 输入字段：`device_id`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/short_link.py:31` · `ShortLinksApiResource`

### PLATFORM-1007 · 前端上报，短连接打开新页面的次数

- 接口声明：`POST /push/<short_url>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/short_link.py:72` · `ShortLinksPushNextPageResource`

### PLATFORM-1008 · 推送重定向 

- 接口声明：`GET /redirect`
- 输入字段：`token`, `business_id`, `business`, `url_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/short_link.py:85` · `PushRedirectResource`

### PLATFORM-1009 · 统一下单接口

- 接口声明：`POST /order`
- 输入字段：`business_ref_id`, `business_type`, `market`, `side`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/simulation/position.py:113` · `PositionOrderResource`

### PLATFORM-1010 · 手动平仓

- 接口声明：`POST /close`
- 输入字段：`position_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/simulation/position.py:161` · `PositionCloseResource`

### PLATFORM-1011 · 调整杠杆倍数

- 接口声明：`POST /adjust-leverage`
- 输入字段：`market`, `leverage`, `business_ref_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/simulation/position.py:189` · `PositionAdjustLeverageResource`

### PLATFORM-1012 · 获取当前持仓仓位列表

- 接口声明：`GET /current`
- 输入字段：`business_ref_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/simulation/position.py:225` · `CurrentPositionResource`

### PLATFORM-1013 · 获取历史仓位列表

- 接口声明：`GET /history`
- 输入字段：`business_ref_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/simulation/position.py:288` · `HistoryPositionResource`

### PLATFORM-1014 · 获取仓位的仓位变化明细

- 接口声明：`GET /deal-history`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/simulation/position.py:359` · `PositionDealHistoryResource`

### PLATFORM-1015 · 获取市场杠杆配置

- 接口声明：`GET /settings/market-leverage`
- 输入字段：`business_ref_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/simulation/position.py:428` · `MarketLeverageConfigResource`

### PLATFORM-1016 · ArticlesResource.get（用途待确认）

- 接口声明：`GET /zendesk/articles`
- 输入字段：`limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:98` · `ArticlesResource`

### PLATFORM-1017 · zendesk公告-类别信息 

- 接口声明：`GET /zendesk/categories`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:115` · `ZendeskCategoriesResource`

### PLATFORM-1018 · zendesk公告-二级分类下的文章（APP），只按时间排序 

- 接口声明：`GET /zendesk/sections/<int:section_id>/articles`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:129` · `ZendeskSectionArticlesResource`

### PLATFORM-1019 · zendesk公告-一级分类下的文章（APP），只按时间排序 

- 接口声明：`GET /zendesk/category/<int:category_id>/articles`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:169` · `ZendeskCategoryArticlesResource`

### PLATFORM-1020 · 最新公告列表/分类公告列表（Web），按置顶和时间排序 

- 接口声明：`GET /zendesk/articles/new`
- 输入字段：`page`, `limit`, `section_id`, `category_id`, `order_by`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:209` · `ZendeskNewArticlesResource`

### PLATFORM-1021 · 推荐公告列表（Web） 

- 接口声明：`GET /zendesk/articles/recommend`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:262` · `ZendeskRecommendArticlesResource`

### PLATFORM-1022 · 公告详情（Web）

- 接口声明：`GET /zendesk/articles/<int:article_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:294` · `ZendeskArticleDetailResource`

### PLATFORM-1023 · 公告搜索（Web） 

- 接口声明：`GET /zendesk/articles/search`
- 输入字段：`keyword`, `category_id`, `sort_by`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:331` · `ZendeskArticlesSearchResource`

### PLATFORM-1024 · 帮助中心公告-类别信息 

- 接口声明：`GET /zendesk/help_center/categories`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:391` · `ZendeskHelpCenterCategoriesResource`

### PLATFORM-1025 · 帮助中心列表 

- 接口声明：`GET /zendesk/help_center/articles`
- 输入字段：`page`, `limit`, `section_id`, `category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:405` · `ZendeskHelpCenterArticlesResource`

### PLATFORM-1026 · 帮助中心推荐文章列表（Web） 

- 接口声明：`GET /zendesk/help_center/articles/recommend`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:454` · `ZendeskHelpCenterRecommendArticlesResource`

### PLATFORM-1027 · 帮助中心文章详情

- 接口声明：`GET /zendesk/help_center/articles/<int:article_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:506` · `ZendeskHelpCenterArticleDetailResource`

### PLATFORM-1028 · 帮助中心搜索（zendesk api） 

- 接口声明：`GET /zendesk/help_center/articles/search`
- 输入字段：`keyword`, `category_id`, `sort_by`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:535` · `ZendeskHelpCenterArticlesSearchResource`

### PLATFORM-1029 · ZendeskJwtTokenResource.get（用途待确认）

- 接口声明：`GET /zendesk/user-token`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/support.py:594` · `ZendeskJwtTokenResource`

### PLATFORM-1030 · 新手必读列表 

- 接口声明：`GET /zendesk/help_center/newbie-must-read/articles`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:624` · `NewbieMustReadArticlesResource`

### PLATFORM-1031 · 新手必读详情 

- 接口声明：`GET /zendesk/help_center/newbie-must-read/articles/<int:article_id>/<string:sub_type>, /zendesk/help_center/newbie-must-read/articles/<int:article_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:653` · `NewbieMustReadArticleDetailResource`

### PLATFORM-1032 · TicketsResource.get（用途待确认）

- 接口声明：`GET /coin919`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:715` · `TicketsResource`

### PLATFORM-1033 · CetInfoResource.get（用途待确认）

- 接口声明：`GET /cet/remain`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:725` · `CetInfoResource`

### PLATFORM-1034 · CetBuyBackInfoResource.get（用途待确认）

- 接口声明：`GET /buy_back/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:745` · `CetBuyBackInfoResource`

### PLATFORM-1035 · GetBuyBackAmountChartResource.get（用途待确认）

- 接口声明：`GET /buy_back/amount/chart`
- 输入字段：`time_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:799` · `GetBuyBackAmountChartResource`

### PLATFORM-1036 · CetBuyBackDetailsResource.get（用途待确认）

- 接口声明：`GET /buy_back/details`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:864` · `CetBuyBackDetailsResource`

### PLATFORM-1037 · CetDestroyDetailsResource.get（用途待确认）

- 接口声明：`GET /buy_back/destroy/details`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:920` · `CetDestroyDetailsResource`

### PLATFORM-1038 · SelfServiceCategoryResource.get（用途待确认）

- 接口声明：`GET /self_service/category`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:1027` · `SelfServiceCategoryResource`

### PLATFORM-1039 · SelfServiceQuestionResource.get（用途待确认）

- 接口声明：`GET /self_service/question/<int:question_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:1089` · `SelfServiceQuestionResource`

### PLATFORM-1040 · SelfServiceMethodResource.get（用途待确认）

- 接口声明：`GET /self_service/method`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:1101` · `SelfServiceMethodResource`

### PLATFORM-1041 · 获取当前展示的欢迎语 

- 接口声明：`GET /welcome-message`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/support.py:1111` · `WelcomeMessageResource`

### PLATFORM-1042 · TimeResource.get（用途待确认）

- 接口声明：`GET /time`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:52` · `TimeResource`

### PLATFORM-1043 · 首页市场

- 接口声明：`GET /market`
- 输入字段：`business_type`, `market_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:66` · `HomeMarketResource`

### PLATFORM-1044 · 首页市场排行

- 接口声明：`GET /market/rank`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:154` · `HomeMarketRankResource`

### PLATFORM-1045 · 币种流通市值

- 接口声明：`GET /asset/circulation`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:166` · `AssetCirculationUsdResource`

### PLATFORM-1046 · AppVersionResource.get（用途待确认）

- 接口声明：`GET /app/version`
- 输入字段：`platform`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:186` · `AppVersionResource`

### PLATFORM-1047 · IPResource.get（用途待确认）

- 接口声明：`GET /ip`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:277` · `IPResource`

### PLATFORM-1048 · is_forbidden 用于前端/APP判断地区限制访问

- 接口声明：`GET /ip/country`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:469` · `IpCountryResource`

### PLATFORM-1049 · SiteTradeInfoResponse.get（用途待确认）

- 接口声明：`GET /trade/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:526` · `SiteTradeInfoResponse`

### PLATFORM-1050 · SiteVerifyChannel.post（用途待确认）

- 接口声明：`POST /verify/channel`
- 输入字段：`type`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:538` · `SiteVerifyChannel`

### PLATFORM-1051 · CountriesResource.get（用途待确认）

- 接口声明：`GET /countries`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:776` · `CountriesResource`

### PLATFORM-1052 · LanguageCountriesResource.get（用途待确认）

- 接口声明：`GET /lang/countries`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:795` · `LanguageCountriesResource`

### PLATFORM-1053 · TradeHistoricalDataResource.get（用途待确认）

- 接口声明：`GET /historical-data`
- 输入字段：`market`, `market_type`, `start_time`, `type`, `kline_type`, `kline_interval`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:869` · `TradeHistoricalDataResource`

### PLATFORM-1054 · UserIpResource.get（用途待确认）

- 接口声明：`GET /user/ip`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/system.py:897` · `UserIpResource`

### PLATFORM-1055 · BeginnerTutorialQuestionResource.get（用途待确认）

- 接口声明：`GET /perpetual/questions`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/tutorial.py:349` · `BeginnerTutorialQuestionResource`

### PLATFORM-1056 · BeginnerTutorialResource.get（用途待确认）

- 接口声明：`GET /perpetual/video`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/tutorial.py:378` · `BeginnerTutorialResource`

### PLATFORM-1057 · TutorialResource.get（用途待确认）

- 接口声明：`GET /video`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/tutorial.py:396` · `TutorialResource`

### PLATFORM-1058 · TutorialVideoWithSubtitleResource.get（用途待确认）

- 接口声明：`GET /video-with-subtitle`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/tutorial.py:412` · `TutorialVideoWithSubtitleResource`

### PLATFORM-1059 · GeneralUploadResource.get（用途待确认）

- 接口声明：`GET `
- 输入字段：`size`, `key`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/upload.py:56` · `GeneralUploadResource`

### PLATFORM-1060 · 通用的图片及视频上传接口 

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/upload.py:116` · `GeneralUploadResource`

### PLATFORM-1061 · for image only

- 接口声明：`POST /file`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/upload.py:144` · `FileUploadResource`

### PLATFORM-1062 · IeoFileUploadResource.post（用途待确认）

- 接口声明：`POST /ieo/file`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/upload.py:171` · `IeoFileUploadResource`

### PLATFORM-1063 · KYTFileUploadResource.post（用途待确认）

- 接口声明：`POST /kyt/file`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/upload.py:232` · `KYTFileUploadResource`

### PLATFORM-1064 · EDDFileUploadResource.post（用途待确认）

- 接口声明：`POST /edd/file`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/upload.py:251` · `EDDFileUploadResource`

### PLATFORM-1065 · 尊享客户申请证明材料上传接口 

- 接口声明：`POST /big-customer-application/file`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/upload.py:265` · `BigCustomerApplicationFileUploadResource`

### PLATFORM-1066 · PublicUploadResource.get（用途待确认）

- 接口声明：`GET /public`
- 输入字段：`size`, `key`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/upload.py:358` · `PublicUploadResource`

### PLATFORM-1067 · FileWithThumbnailUploadResource.post（用途待确认）

- 接口声明：`POST /file-with-thumbnail`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/upload.py:494` · `FileWithThumbnailUploadResource`

### PLATFORM-1068 · 上传图片、PDF 或视频，叠加水印后写入私有桶并生成多档缩略图。  请求为 multipart/form-data： - my_file（必填）：上传文件。 - type（可选）：   - pdf：PDF（最大 20MB）   - video：视频 mp4/mov（最大 50MB）   - 不传：按图片校验 png/jpeg/jpg/webp（最大 5MB）

- 接口声明：`POST /file-with-watermark-thumbnail`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/upload.py:506` · `FileWithWatermarkThumbnailUploadResource`

### PLATFORM-1069 · FileWithThumbnailPublicUploadResource.post（用途待确认）

- 接口声明：`POST /file-with-thumbnail/public`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/upload.py:550` · `FileWithThumbnailPublicUploadResource`

### PLATFORM-1070 · VipLevel.get（用途待确认）

- 接口声明：`GET /level`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/vip.py:39` · `VipLevel`

### PLATFORM-1071 · VipInfo.get（用途待确认）

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=True)
- 代码依据：`app/api/frontend/vip.py:70` · `VipInfo`

### PLATFORM-1072 · BindingAddressResource.get（用途待确认）

- 接口声明：`GET /binding-address`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/vip.py:112` · `BindingAddressResource`

### PLATFORM-1073 · BindingAddressResource.delete（用途待确认）

- 接口声明：`DELETE /binding-address`
- 输入字段：`address`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/vip.py:127` · `BindingAddressResource`

### PLATFORM-1074 · BindingAddressResource.post（用途待确认）

- 接口声明：`POST /binding-address`
- 输入字段：`address`, `sign_body`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/vip.py:142` · `BindingAddressResource`

### PLATFORM-1075 · 兼容 APP 保留

- 接口声明：`GET /cet-position`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/vip.py:192` · `CETPositionResource`

### PLATFORM-1076 · VipLevelCurrentResource.get（用途待确认）

- 接口声明：`GET /level-current`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/vip.py:204` · `VipLevelCurrentResource`

### PLATFORM-1077 · GlobalSettingsResource.get（用途待确认）

- 接口声明：`GET /global-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:56` · `GlobalSettingsResource`

### PLATFORM-1078 · MarketsResource.get（用途待确认）

- 接口声明：`GET /markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:252` · `MarketsResource`

### PLATFORM-1079 · ApiUsersResource.get（用途待确认）

- 接口声明：`GET /api-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:447` · `ApiUsersResource`

### PLATFORM-1080 · FeeRatesResource.get（用途待确认）

- 接口声明：`GET /fee-rates`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:517` · `FeeRatesResource`

### PLATFORM-1081 · UserSettingsResource.post（用途待确认）

- 接口声明：`POST /user-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:553` · `UserSettingsResource`

### PLATFORM-1082 · PriceVerifySettingsResource.get（用途待确认）

- 接口声明：`GET /price-verify-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:565` · `PriceVerifySettingsResource`

### PLATFORM-1083 · ForbiddenAccountResource.get（用途待确认）

- 接口声明：`GET /forbidden-account/<int:user_id>`
- 输入字段：`account`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:584` · `ForbiddenAccountResource`

### PLATFORM-1084 · UserApiFrequencyLimitResource.get（用途待确认）

- 接口声明：`GET /frequency-limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:599` · `UserApiFrequencyLimitResource`

### PLATFORM-1085 · UserApiLongPeriodResource.get（用途待确认）

- 接口声明：`GET /long-period`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:655` · `UserApiLongPeriodResource`

### PLATFORM-1086 · UserApiSpeedResource.get（用途待确认）

- 接口声明：`GET /speed`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sync.py:695` · `UserApiSpeedResource`

### PLATFORM-1087 · IPResource.get（用途待确认）

- 接口声明：`GET /ip`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/system.py:25` · `IPResource`

### PLATFORM-1088 · AdminPermissionResource.post（用途待确认）

- 接口声明：`POST /admin/permissions`
- 输入字段：`app`, `rules`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/system.py:59` · `AdminPermissionResource`

### PLATFORM-1089 · CountryResource.get（用途待确认）

- 接口声明：`GET /country`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/system.py:99` · `CountryResource`

### PLATFORM-1090 · TestResource.get（用途待确认）

- 接口声明：`GET /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/test.py:13` · `TestResource`

### PLATFORM-1091 · InstitutionCheckAccount.post（用途待确认）

- 接口声明：`POST /check/account`
- 输入字段：`address`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/institution.py:25` · `InstitutionCheckAccount`

### PLATFORM-1092 · InstitutionOrderNotify.post（用途待确认）

- 接口声明：`POST /order/notify`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/institution.py:57` · `InstitutionOrderNotify`

### PLATFORM-1093 · RiskControlResource.get（用途待确认）

- 接口声明：`GET /transfer_enabled`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/institution.py:70` · `RiskControlResource`

### PLATFORM-1094 · CreditInfoResource.get（用途待确认）

- 接口声明：`GET /loan-assets`
- 输入字段：`asset`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/internal.py:21` · `CreditInfoResource`

### PLATFORM-1095 · CreditToFlat.post（用途待确认）

- 接口声明：`POST /credit-flat`
- 输入字段：`coin_type`, `flat_amount`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/internal.py:38` · `CreditToFlat`

### PLATFORM-1096 · AssetBalanceResource.post（用途待确认）

- 接口声明：`POST /asset-balance`
- 输入字段：`data`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/quantification.py:25` · `AssetBalanceResource`

### PLATFORM-1097 · WalletBalanceResource.get（用途待确认）

- 接口声明：`GET /hot-wallet-balance`
- 输入字段：`asset`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/quantification.py:44` · `WalletBalanceResource`

### PLATFORM-1098 · MakersResource.get（用途待确认）

- 接口声明：`GET /makers`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/quantification.py:71` · `MakersResource`

### PLATFORM-1099 · PerpetualUsersResouce.get（用途待确认）

- 接口声明：`GET /perpetual-users`
- 输入字段：`month`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/quantification.py:91` · `PerpetualUsersResouce`

### PLATFORM-1100 · PerpetualPositionsResouce.get（用途待确认）

- 接口声明：`GET /perpetual-positions`
- 输入字段：`market`, `cursor`, `limit`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/quantification.py:106` · `PerpetualPositionsResouce`

### PLATFORM-1101 · CMC: 合约市场信息

- 接口声明：`GET /perpetual/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:48` · `PerpetualInfoResource`

### PLATFORM-1102 · CoinGecko: 合约市场信息

- 接口声明：`GET /perpetual/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:63` · `PerpetualListResource`

### PLATFORM-1103 · PerpetualMarketDepthResource.get（用途待确认）

- 接口声明：`GET /perpetual/orderbook`
- 输入字段：`market`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:86` · `PerpetualMarketDepthResource`

### PLATFORM-1104 · PerpetualLiquidationResource.get（用途待确认）

- 接口声明：`GET /perpetual/liquidation`
- 输入字段：`market`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:115` · `PerpetualLiquidationResource`

### PLATFORM-1105 · CMC: 现货市场汇总信息

- 接口声明：`GET /spot/summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:165` · `SpotMarketSummaryResource`

### PLATFORM-1106 · CMC: 现货市场交易数据

- 接口声明：`GET /spot/ticker`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:206` · `SpotTickerResource`

### PLATFORM-1107 · CMC: 现货市场订单簿

- 接口声明：`GET /spot/orderbook`
- 输入字段：`market_pair`, `depth`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:233` · `SpotOrderBookResource`

### PLATFORM-1108 · CMC: 现货交易订单信息

- 接口声明：`GET /spot/trades`
- 输入字段：`market_pair`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:267` · `SpotMarketTradesResource`

### PLATFORM-1109 · CoinGecko: 现货交易对币种信息

- 接口声明：`GET /spot/pairs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:302` · `SpotMarketPairsResource`

### PLATFORM-1110 · CoinGecko: 现货市场汇总信息

- 接口声明：`GET /spot/market_info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:322` · `SpotMarketInfoResource`

### PLATFORM-1111 · CoinGecko: 现货市场订单簿

- 接口声明：`GET /spot/orders`
- 输入字段：`ticker_id`, `depth`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:355` · `SpotOrdersResource`

### PLATFORM-1112 · CoinGecko: 现货历史订单信息

- 接口声明：`GET /spot/historical_trades`
- 输入字段：`ticker_id`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:389` · `SpotMarketHistoricalTradesResource`

### PLATFORM-1113 · ZendeskUserInfoResource.get（用途待确认）

- 接口声明：`GET /zendesk/user`
- 输入字段：`external_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:429` · `ZendeskUserInfoResource`

### PLATFORM-1114 · CoinGlass: BTC钱包余额

- 接口声明：`GET /wallet/balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:464` · `WalletBalanceResource`

### PLATFORM-1115 · CurrencyRateResource.get（用途待确认）

- 接口声明：`GET /currency/rate`
- 输入字段：`from_asset`, `to_asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v1/third_party.py:533` · `CurrencyRateResource`

### PLATFORM-1116 · CustodyPingResource.get（用途待确认）

- 接口声明：`GET /ping`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:16` · `CustodyPingResource`

### PLATFORM-1117 · 在第三方托管平台为用户绑定子账号，用于资产托管

- 接口声明：`POST /user/bind`
- 输入字段：`platform_user_id`, `access_id`, `signature`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:25` · `CustodyUserBindResource`

### PLATFORM-1118 · 在第三方托管平台为用户绑定子账号是否可用

- 接口声明：`GET /user/is_valid`
- 输入字段：`user_id`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:43` · `CustodyUserValidResource`

### PLATFORM-1119 · 查询用户在第三方托管平台的资产余额

- 接口声明：`GET /user/balance`
- 输入字段：`user_id`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:61` · `CustodyUserBalanceResource`

### PLATFORM-1120 · 在第三方托管平台为用户充值

- 接口声明：`POST /user/deposit`
- 输入字段：`user_id`, `asset`, `amount`, `order_id`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:81` · `CustodyUserDepositResource`

### PLATFORM-1121 · 在第三方托管平台为用户充值查询

- 接口声明：`GET /user/deposit`
- 输入字段：`user_id`, `asset`, `order_id`, `page`, `limit`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:97` · `CustodyUserDepositResource`

### PLATFORM-1122 · 在第三方托管平台为用户提现

- 接口声明：`POST /user/withdraw`
- 输入字段：`user_id`, `asset`, `amount`, `order_id`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:128` · `CustodyUserWithdrawResource`

### PLATFORM-1123 · 在第三方托管平台为用户提现查询

- 接口声明：`GET /user/withdraw`
- 输入字段：`user_id`, `asset`, `order_id`, `page`, `limit`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:144` · `CustodyUserWithdrawResource`

### PLATFORM-1124 · 获取结算单数据

- 接口声明：`GET /settlement/list`
- 输入字段：`settlement_id`, `user_settlement_id`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:176` · `CustodySettlementListResource`

### PLATFORM-1125 · 充值预检查接口

- 接口声明：`POST /user/deposit/pre-check`
- 输入字段：`user_id`, `asset`, `amount`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:197` · `CustodyUserDepositPreCheckResource`

### PLATFORM-1126 · 提现预检查接口

- 接口声明：`POST /user/withdraw/pre-check`
- 输入字段：`user_id`, `asset`, `amount`
- 显式控制：require_custody_platform_auth
- 代码依据：`app/api/v2/custody.py:223` · `CustodyUserWithdrawPreCheckResource`

### PLATFORM-1127 · MaintainInfoResource.get（用途待确认）

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/v2/maintain.py:71` · `MaintainInfoResource`

## 相关测试文件（路径归类，未执行）

- `tests/__init__.py`
- `tests/api/__init__.py`
- `tests/api/admin/__init__.py`
- `tests/api/admin/test_ai_translation.py`
- `tests/api/admin/test_big_customer.py`
- `tests/api/admin/test_questionnaire.py`
- `tests/api/admin/test_questionnaire_language_names.py`
- `tests/api/admin/test_sms_report.py`
- `tests/api/admin/test_translation_supported_languages.py`
- `tests/api/common/test_use_kwargs.py`
- `tests/api/frontend/__init__.py`
- `tests/api/frontend/test_ai_analysis.py`
- `tests/api/frontend/test_analytics.py`
- `tests/api/frontend/test_app_api.py`
- `tests/api/frontend/test_comment.py`
- `tests/api/frontend/test_insight.py`
- `tests/api/frontend/test_maintain_popup_windows.py`
- `tests/api/frontend/test_quotes.py`
- `tests/api/frontend/test_safety.py`
- `tests/api/frontend/test_support.py`
- `tests/api/frontend/test_system.py`
- `tests/api/frontend/test_tutorial.py`
- `tests/api/frontend/test_upload.py`
- `tests/api/internal/test_system.py`
- `tests/base.py`
- `tests/base_api_test.py`
- `tests/business/__init__.py`
- `tests/business/big_customer/test_application.py`
- `tests/business/big_customer/test_big_customer.py`
- `tests/business/clients/__init__.py`
- `tests/business/clients/test_ai_translate.py`
- `tests/business/clients/test_api_gateway.py`
- `tests/business/clients/test_chainalysis.py`
- `tests/business/clients/test_server.py`
- `tests/business/equity_center/test_inc_eq_api.py`
- `tests/business/equity_center/test_inc_eq_biz.py`
- `tests/business/external_table_migration_framework.py`
- `tests/business/lock/test_lock.py`
- `tests/business/question/test_question.py`
- `tests/business/test_admin_tag.py`
- `tests/business/test_ai_analysis_mapping.py`
- `tests/business/test_ai_analysis_snapshot.py`
- `tests/business/test_alert.py`
- `tests/business/test_analytics.py`
- `tests/business/test_appsflyer.py`
- `tests/business/test_audit_status.py`
- `tests/business/test_blacklist.py`
- `tests/business/test_blacklist_helper.py`
- `tests/business/test_chainalysis_alert.py`
- `tests/business/test_country_settings_validation.py`
- `tests/business/test_edd_material.py`
- `tests/business/test_host.py`
- `tests/business/test_multilang_content.py`
- `tests/business/test_novice.py`
- `tests/business/test_page_inset_cache.py`
- `tests/business/test_prices.py`
- `tests/business/test_questionnaire.py`
- `tests/business/test_share_winodws.py`
- `tests/business/test_site_config.py`
- `tests/business/test_sqlalchemy_autoflush.py`
- `tests/business/test_t33_backup_cleanup_raw_table_maintenance.py`
- `tests/business/test_vip.py`
- `tests/business/test_zendesk.py`
- `tests/caches/test_insight.py`
- `tests/caches/test_inverted_index.py`
- `tests/caches/test_popup_window_cache.py`
- `tests/caches/test_slack.py`
- `tests/caches/test_system.py`
- `tests/common/mock_mongo.py`
- `tests/common/mock_mysql.py`
- `tests/common/mock_redis.py`
- `tests/common/mock_server_client.py`
- `tests/common/patch_celery.py`
- `tests/common/patch_g_map.py`
- `tests/common/t_common.py`
- `tests/common/test_check_layer_imports.py`
- `tests/common/test_mock_mongo.py`
- `tests/common/test_mock_mysql.py`
- `tests/common/test_mock_redis.py`
- `tests/common/test_mock_server_client.py`
- `tests/common/test_op_log_registry.py`
- `tests/common/test_patch_g_map.py`
- `tests/common/test_request_context_imports.py`
- `tests/common/test_reverse_import_layers.py`
- `tests/common/test_reverse_import_smoke.py`
- `tests/common/test_supported_languages.py`
- `tests/concurrent_api_test.py`
- `tests/consumer/__init__.py`
- `tests/deployment/test_backfill_audit_dual_status.py`
- `tests/deployment/test_check_audit_dual_status_not_null.py`
- `tests/lang/__init__.py`
- `tests/lang/my_import/__init__.py`
- `tests/lang/my_import/a/__init__.py`
- `tests/lang/my_import/a/my_enum.py`
- `tests/lang/my_import/test_import_eque.py`
- `tests/mock/TestMockRedis.py`
- `tests/mock/__init__.py`
- `tests/models/__init__.py`
- `tests/models/mongo/__init__.py`
- `tests/models/mongo/test_insight.py`
- `tests/models/mongo/test_translation.py`
- `tests/models/test_apple_ads.py`
- `tests/models/test_base.py`
- `tests/models/test_batch_query.py`
- `tests/models/test_daily.py`
- `tests/models/test_kol.py`
- `tests/schedules/__init__.py`
- `tests/schedules/reports/test_short_link.py`
- `tests/schedules/test_ai_analysis.py`
- `tests/schedules/test_global_search.py`
- `tests/schedules/test_translation.py`
- `tests/test_app/__init__.py`
- `tests/test_app/test_coupon/__init__.py`
- `tests/test_app/test_coupon/test_coupon_api.py`
- `tests/test_app/test_coupon/test_coupon_distribution.py`
- `tests/test_app/test_coupon/test_coupon_pool.py`
- `tests/test_app/test_templates/__init__.py`
- `tests/test_app/test_templates/test_email/__init__.py`
- `tests/test_app/test_templates/test_email/test_confirmation.py`
- `tests/test_app/test_templates/test_email/test_verification_code.py`
- `tests/test_app/test_templates/test_sms/__init__.py`
- `tests/utils/__init__.py`
- `tests/utils/test_cache.py`
- `tests/utils/test_config.py`
- `tests/utils/test_config_new.py`
- `tests/utils/test_config_serializer.py`
- `tests/utils/test_config_storage.py`
- `tests/utils/test_date.py`
- `tests/utils/test_file.py`
- `tests/utils/test_files.py`
- `tests/utils/test_importer.py`
- `tests/utils/test_iterable.py`
- `tests/utils/test_iterable_helpers.py`
- `tests/utils/test_net.py`
- `tests/utils/test_watermark.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
