# 运营与消息 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### OPERATION-001 · 运营>活动>空投管理>活动管理-列表 

- 接口声明：`GET /activity`
- 输入字段：`id`, `airdrop_mode`, `asset`, `status`, `active_status`, `label_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:135` · `AirdropActivityResource`

### OPERATION-002 · 运营>活动>空投管理>活动管理-添加空投活动 

- 接口声明：`POST /activity`
- 输入字段：`airdrop_mode`, `VIP`, `KYC`, `NEED_HOLDING`, `ASSET_HOLDING`, `TRADE_OP_TYPE`, `TRADE_BUSINESS_TYPE`, `TRADE_VALUE`, `TRADE_TYPE_RANGE`, `TRADE_DAY_RANGE`, `BALANCE_OP_TYPE`, `BALANCE_VALUE`, `REGISTERED_OP_TYPE`, `REGISTERED_VALUE`, `USED_VALUE`, `assets`, `info_url`, `name`, `more_reward_url`, `asset`, `start_time`, `end_time`, `label_type`, `details`, `lock_day`, `amount`, `total_count`, `question_configs`, `funding_source`, `estimate_type`, `asset_rewards`, `coupon_rewards`, `equity_rewards`
- 显式控制：lock_request()
- 代码依据：`app/api/admin/activity/airdrop.py:613` · `AirdropActivityResource`

### OPERATION-003 · 运营>空投活动>空投管理>活动管理-编辑保存空投活动 

- 接口声明：`PUT /activity`
- 输入字段：`id`, `VIP`, `KYC`, `NEED_HOLDING`, `ASSET_HOLDING`, `TRADE_OP_TYPE`, `TRADE_BUSINESS_TYPE`, `TRADE_VALUE`, `TRADE_TYPE_RANGE`, `TRADE_DAY_RANGE`, `BALANCE_OP_TYPE`, `BALANCE_VALUE`, `REGISTERED_OP_TYPE`, `REGISTERED_VALUE`, `USED_VALUE`, `assets`, `info_url`, `asset`, `name`, `more_reward_url`, `start_time`, `end_time`, `label_type`, `details`, `lock_day`, `amount`, `total_count`, `question_configs`, `introduction_configs`, `funding_source`, `estimate_type`, `asset_rewards`, `coupon_rewards`, `equity_rewards`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:820` · `AirdropActivityResource`

### OPERATION-004 · 运营>活动>空投管理>活动管理-空投活动-操作上下架以及提交审核 

- 接口声明：`PATCH /activity`
- 输入字段：`id`, `status`
- 显式控制：lock_request()
- 代码依据：`app/api/admin/activity/airdrop.py:1047` · `AirdropActivityResource`

### OPERATION-005 · 运营>活动>空投管理>活动详情

- 接口声明：`GET /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1158` · `AirdropActivityDetailResource`

### OPERATION-006 · 运营-活动-空投活动-提交审核

- 接口声明：`PATCH /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1326` · `AirdropActivityDetailResource`

### OPERATION-007 · 运营-活动-空投活动-审核

- 接口声明：`POST /activity/<int:id_>/audit`
- 输入字段：`status`, `audit_remark`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/activity/airdrop.py:1349` · `AirdropActivityAuditResource`

### OPERATION-008 · 运营>活动>空投管理>活动管理-空投详情 

- 接口声明：`GET /random-record`
- 输入字段：`id`, `status`, `state`, `user`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1493` · `AirdropActivityLotteryHistoryResource`

### OPERATION-009 · 运营-活动-空投活动-编辑中签状态

- 接口声明：`PUT /random-record`
- 输入字段：`airdrop_activity_id`, `user_id`, `state`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1643` · `AirdropActivityLotteryHistoryResource`

### OPERATION-010 · 运营>活动>空投管理>活动管理-空投用户校验

- 接口声明：`POST /random-record`
- 输入字段：`airdrop_activity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1686` · `AirdropActivityLotteryHistoryResource`

### OPERATION-011 · 活动-空投奖励-活动用户批量上传

- 接口声明：`POST /upload-record/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1719` · `AirdropActivityUploadRecordResource`

### OPERATION-012 · 运营-活动-空投活动-派奖

- 接口声明：`POST /send-reward`
- 输入字段：`airdrop_activity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1783` · `AirdropActivitySendRewardResource`

### OPERATION-013 · 运营>活动>空投管理>活动管理-限时空投详情 

- 接口声明：`GET /realtime-record`
- 输入字段：`id`, `user`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1854` · `AirdropActivityRealtimeRecordResource`

### OPERATION-014 · 运营>活动>空投管理>活动管理-模板

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1943` · `AirdropQuestionTemplateResource`

### OPERATION-015 · 运营>活动>空投管理>活动管理-导入模板

- 接口声明：`POST /question-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1957` · `AirdropUploadResource`

### OPERATION-016 · 运营>活动>空投管理-学习内容-翻译

- 接口声明：`POST /detail/translation`
- 输入字段：`lang`, `target`, `title`, `summary`, `introductions`, `business`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:1974` · `DetailTranslationResource`

### OPERATION-017 · 运营>活动>空投管理-答题信息-翻译

- 接口声明：`POST /question/translation`
- 输入字段：`lang`, `target`, `configs`, `business`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/airdrop.py:2009` · `QuestionTranslationResource`

### OPERATION-018 · 运营>活动>日历管理>活动管理-列表 

- 接口声明：`GET /activity`
- 输入字段：`active_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/calendar.py:43` · `CalendarActivityResource`

### OPERATION-019 · 运营>活动>日历管理>活动管理-添加日历活动 

- 接口声明：`POST /activity`
- 输入字段：`name`, `activity_type`, `url`, `start_time`, `end_time`, `online_time`, `offline_time`, `details`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/calendar.py:209` · `CalendarActivityResource`

### OPERATION-020 · 运营>日历活动>日历管理>活动管理-编辑保存日历活动 

- 接口声明：`PUT /activity`
- 输入字段：`id`, `name`, `activity_type`, `url`, `start_time`, `end_time`, `online_time`, `offline_time`, `details`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/calendar.py:279` · `CalendarActivityResource`

### OPERATION-021 · 运营>日历活动>日历管理>活动管理-删除日历活动

- 接口声明：`DELETE /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/calendar.py:378` · `CalendarActivityDetailResource`

### OPERATION-022 · 运营>活动>日历管理>活动管理-模板

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/calendar.py:406` · `CalendarQuestionTemplateResource`

### OPERATION-023 · 运营>活动>日历管理>活动管理-导入模板

- 接口声明：`POST /template-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/calendar.py:422` · `CalendarUploadResource`

### OPERATION-024 · 运营>活动>Dibs管理>活动管理-列表 

- 接口声明：`GET /activity`
- 输入字段：`asset`, `status`, `active_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:58` · `DiscountActivityResource`

### OPERATION-025 · 运营>活动>Dibs管理>活动管理-添加Dibs活动 

- 接口声明：`POST /activity`
- 输入字段：`VIP`, `KYC`, `NEED_HOLDING`, `ASSET_HOLDING`, `TRADE_OP_TYPE`, `TRADE_BUSINESS_TYPE`, `TRADE_VALUE`, `TRADE_TYPE_RANGE`, `TRADE_DAY_RANGE`, `BALANCE_OP_TYPE`, `BALANCE_VALUE`, `REGISTERED_OP_TYPE`, `REGISTERED_VALUE`, `USED_VALUE`, `name`, `asset`, `start_time`, `end_time`, `discount_type`, `details`, `total_amount`, `total_count`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:276` · `DiscountActivityResource`

### OPERATION-026 · 运营>Dibs活动>Dibs管理>活动管理-编辑保存Dibs活动 

- 接口声明：`PUT /activity`
- 输入字段：`id`, `VIP`, `KYC`, `NEED_HOLDING`, `ASSET_HOLDING`, `TRADE_OP_TYPE`, `TRADE_BUSINESS_TYPE`, `TRADE_VALUE`, `TRADE_TYPE_RANGE`, `TRADE_DAY_RANGE`, `BALANCE_OP_TYPE`, `BALANCE_VALUE`, `REGISTERED_OP_TYPE`, `REGISTERED_VALUE`, `USED_VALUE`, `asset`, `name`, `start_time`, `end_time`, `discount_type`, `details`, `total_amount`, `total_count`, `introduction_configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:443` · `DiscountActivityResource`

### OPERATION-027 · 运营>活动>Dibs管理>活动管理-Dibs活动-操作上下架 

- 接口声明：`PATCH /activity`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:579` · `DiscountActivityResource`

### OPERATION-028 · 运营>活动>Dibs管理>活动详情

- 接口声明：`GET /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:641` · `DiscountActivityDetailResource`

### OPERATION-029 · 运营>活动>Dibs管理>活动管理-Dibs详情 

- 接口声明：`GET /record`
- 输入字段：`id`, `status`, `user`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:861` · `DiscountActivityLotteryHistoryResource`

### OPERATION-030 · 运营-活动-Dibs活动-编辑中签状态

- 接口声明：`PUT /record`
- 输入字段：`discount_activity_id`, `user_id`, `state`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:956` · `DiscountActivityLotteryHistoryResource`

### OPERATION-031 · 运营>活动>Dibs管理>活动管理-Dibs用户校验

- 接口声明：`POST /record`
- 输入字段：`discount_activity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:999` · `DiscountActivityLotteryHistoryResource`

### OPERATION-032 · 活动-DIbs奖励-活动用户批量上传

- 接口声明：`POST /upload-record/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:1032` · `DiscountActivityUploadRecordResource`

### OPERATION-033 · 运营-活动-Dibs活动-派奖

- 接口声明：`POST /send-reward`
- 输入字段：`discount_activity_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/discount.py:1089` · `DiscountActivitySendRewardResource`

### OPERATION-034 · 运营-活动-八周年抽奖领奖记录

- 接口声明：`GET /rewards`
- 输入字段：`user_id`, `user_lottery_level`, `status`, `draw_start_time`, `draw_end_time`, `received_start_time`, `received_end_time`, `prize`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/eighth.py:78` · `EighthRewardListResource`

### OPERATION-035 · 运营-活动-八周年抽奖领奖统计

- 接口声明：`GET /rewards/statistics`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/eighth.py:194` · `EighthRewardStatisticsResource`

### OPERATION-036 · 运营-活动-八周年抽奖审核记录

- 接口声明：`GET /rewards/audit`
- 输入字段：`user_id`, `status`, `prize`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/eighth.py:303` · `EighthRewardAuditResource`

### OPERATION-037 · 运营-活动-八周年抽奖审核实物奖励 

- 接口声明：`POST /rewards/audit`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/eighth.py:411` · `EighthRewardAuditResource`

### OPERATION-038 · 运营-活动-五周年-领取奖励列表 

- 接口声明：`GET /box-rewards`
- 输入字段：`export`, `start`, `end`, `user_id`, `type`, `reward`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/fifth.py:56` · `FifthBoxRewardListResource`

### OPERATION-039 · 运营-活动-五周年-限制名单列表 

- 接口声明：`GET /risk-list`
- 输入字段：`export`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/fifth.py:226` · `FifthRiskListResource`

### OPERATION-040 · 运营>活动>投资管理>活动管理-列表 

- 接口声明：`GET /activity`
- 输入字段：`asset`, `status`, `active_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:53` · `IeoActivityResource`

### OPERATION-041 · 运营>活动>融资管理>添加投资活动 

- 接口声明：`POST /activity`
- 输入字段：`name`, `subscribe_asset`, `subscribe_total_amount`, `subscribe_total_count`, `max_subscribe_count`, `pledge_asset`, `pledge_amount`, `pay_asset`, `pay_amount`, `start_time`, `end_time`, `ready_time`, `details`, `explorer_list`, `lock_hour`, `black_country_list`, `ieo_asset`, `ieo_name`, `ieo_icon`, `ieo_project_icon`, `cover`, `circulation`, `issued_time`, `total_supply`, `total_supply_value`, `white_paper`, `official_website`, `source_code`, `telegram`, `facebook`, `twitter`, `reddit`, `medium`, `discord`, `rule_url`, `rule_detail_url`, `VIP`, `KYC`, `NEED_HOLDING`, `ASSET_HOLDING`, `TRADE_OP_TYPE`, `TRADE_BUSINESS_TYPE`, `TRADE_VALUE`, `TRADE_DAY_RANGE`, `BALANCE_OP_TYPE`, `BALANCE_VALUE`, `REGISTERED_OP_TYPE`, `REGISTERED_VALUE`, `USED_VALUE`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:310` · `IeoActivityResource`

### OPERATION-042 · 运营>活动>融资管理>编辑投资活动 

- 接口声明：`PUT /activity`
- 输入字段：`name`, `id`, `subscribe_asset`, `subscribe_total_amount`, `subscribe_total_count`, `max_subscribe_count`, `pledge_asset`, `pledge_amount`, `pay_asset`, `pay_amount`, `start_time`, `end_time`, `ready_time`, `details`, `explorer_list`, `lock_hour`, `black_country_list`, `ieo_asset`, `ieo_name`, `ieo_icon`, `ieo_project_icon`, `cover`, `circulation`, `issued_time`, `total_supply`, `total_supply_value`, `white_paper`, `official_website`, `source_code`, `telegram`, `facebook`, `twitter`, `reddit`, `medium`, `discord`, `rule_url`, `rule_detail_url`, `VIP`, `KYC`, `NEED_HOLDING`, `ASSET_HOLDING`, `TRADE_OP_TYPE`, `TRADE_BUSINESS_TYPE`, `TRADE_VALUE`, `TRADE_DAY_RANGE`, `BALANCE_OP_TYPE`, `BALANCE_VALUE`, `REGISTERED_OP_TYPE`, `REGISTERED_VALUE`, `USED_VALUE`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:541` · `IeoActivityResource`

### OPERATION-043 · 运营>活动>融资管理>-操作上下架 

- 接口声明：`PATCH /activity`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:721` · `IeoActivityResource`

### OPERATION-044 · 运营>活动>融资管理>订单记录详情 

- 接口声明：`GET /record`
- 输入字段：`id`, `status`, `asset_status`, `asset_cancel_status`, `user`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:784` · `IeoActivityLotteryHistoryResource`

### OPERATION-045 · 运营>活动>投资管理>投资白名单 

- 接口声明：`GET /whitelist`
- 输入字段：`user`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:880` · `IeoActivityWhitelistResource`

### OPERATION-046 · 运营>活动>投资管理>添加投资白名单 

- 接口声明：`POST /whitelist`
- 输入字段：`user_id`, `activity_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:926` · `IeoActivityWhitelistResource`

### OPERATION-047 · 运营>活动>投资管理>编辑投资白名单 

- 接口声明：`PATCH /whitelist`
- 输入字段：`user_id`, `activity_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:967` · `IeoActivityWhitelistResource`

### OPERATION-048 · 运营>活动>投资管理>取消投资白名单 

- 接口声明：`DELETE /whitelist/<int:activity_id>/<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/ieo.py:1014` · `IeoActivityWhitelistDeleteResource`

### OPERATION-049 · 运营>活动>Ming>Ming管理-列表 

- 接口声明：`GET /project-list`
- 输入字段：`reward_asset`, `name`, `status`, `active_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:146` · `LaunchMiningProjectListResource`

### OPERATION-050 · 运营>活动>Ming>Ming管理-新增Mining配置 

- 接口声明：`POST /project-list`
- 输入字段：`name`, `start_time`, `end_time`, `auto_online_time`, `reward_asset`, `reward_total_amount`, `rule_url`, `pools`, `funding_source`
- 显式控制：lock_request('admin_launch_project')
- 代码依据：`app/api/admin/activity/launch_pool.py:247` · `LaunchMiningProjectListResource`

### OPERATION-051 · 运营>活动>Ming>Ming管理-详情页面 

- 接口声明：`GET /project-detail`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:323` · `LaunchMiningProjectDetailResource`

### OPERATION-052 · 运营>活动>Ming>Ming管理-修改Mining配置 

- 接口声明：`PUT /project-detail`
- 输入字段：`id`, `name`, `start_time`, `end_time`, `auto_online_time`, `reward_asset`, `reward_total_amount`, `rule_url`, `pools`, `funding_source`
- 显式控制：lock_request('admin_launch_project')
- 代码依据：`app/api/admin/activity/launch_pool.py:364` · `LaunchMiningProjectDetailResource`

### OPERATION-053 · 运营>活动>Ming>Ming管理-提交 

- 接口声明：`POST /project/submit`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:472` · `LaunchMiningProjectSubmitResource`

### OPERATION-054 · 运营>活动>Ming>Ming管理-审核 

- 接口声明：`POST /project/audit`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:504` · `LaunchMiningProjectAuditResource`

### OPERATION-055 · 运营>活动>Ming>Ming管理-上架 

- 接口声明：`POST /project/online`
- 输入字段：`id`
- 显式控制：lock_request('admin_launch_project')
- 代码依据：`app/api/admin/activity/launch_pool.py:534` · `LaunchMiningProjectOnlineResource`

### OPERATION-056 · 运营>活动>Ming>Ming管理-下架 

- 接口声明：`POST /project/offline`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:576` · `LaunchMiningProjectOfflineResource`

### OPERATION-057 · 运营>活动>Ming>Ming管理-关闭 

- 接口声明：`POST /project/close`
- 输入字段：`id`
- 显式控制：lock_request('admin_launch_project')
- 代码依据：`app/api/admin/activity/launch_pool.py:615` · `LaunchMiningProjectCloseResource`

### OPERATION-058 · 运营>活动>Ming>Ming管理-删除 

- 接口声明：`POST /project/delete`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:652` · `LaunchMiningProjectDeleteResource`

### OPERATION-059 · 运营>活动>Ming>Ming管理-用户参与明细 

- 接口声明：`GET /join-user-list`
- 输入字段：`project_id`, `pool_ids`, `user_id`, `reward_status`, `start_time`, `end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:700` · `LaunchMiningProjectJoinUsersResource`

### OPERATION-060 · 运营>活动>Ming>Ming管理-用户参与明细-质押流水 

- 接口声明：`GET /operate-history`
- 输入字段：`project_id`, `pool_id`, `pool_ids`, `user_id`, `type`, `start_time`, `end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:837` · `LaunchMiningProjectUserOperateHisResource`

### OPERATION-061 · 运营>活动>Ming>Ming管理-用户参与明细-收益历史 

- 接口声明：`GET /reward-history`
- 输入字段：`project_id`, `pool_id`, `user_id`, `type`, `start_time`, `end_time`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/launch_pool.py:933` · `LaunchMiningProjectUserRewardHisResource`

### OPERATION-062 · 运营-活动-挖矿管理-报名用户模板

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:74` · `MiningUserTemplateResource`

### OPERATION-063 · 运营-活动-挖矿管理-报名用户详情

- 接口声明：`GET /users`
- 输入字段：`activity_id`, `order`, `status`, `start_time`, `end_time`, `export`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:101` · `MiningUserResource`

### OPERATION-064 · 运营-活动-挖矿管理-用户上传

- 接口声明：`POST /users`
- 输入字段：`activity_id`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/activity/mining.py:314` · `MiningUserResource`

### OPERATION-065 · 运营-活动-挖矿管理-报名用户详情-编辑 

- 接口声明：`PUT /users`
- 输入字段：`user_id`, `activity_id`, `remark`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:387` · `MiningUserResource`

### OPERATION-066 · 运营-活动-挖矿管理-产量详情

- 接口声明：`GET /output`
- 输入字段：`activity_id`, `start_time`, `end_time`, `user_id`, `realtime`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:654` · `MiningOutputResource`

### OPERATION-067 · 运营>活动>挖矿管理>活动管理-列表 

- 接口声明：`GET /activity`
- 输入字段：`mining_mode`, `mining_asset`, `status`, `active_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:690` · `MiningActivityResource`

### OPERATION-068 · 运营>活动>挖矿管理>活动管理-添加挖矿活动 

- 接口声明：`POST /activity`
- 输入字段：`mining_mode`, `markets`, `mining_asset`, `start_date`, `duration`, `details`, `join_user_type`, `daily_output`, `hourly_output`, `business_type`, `trade_mode`, `pledge_asset`, `user_daily_max_output`, `user_max_pledge_amount`, `user_min_pledge_amount`, `user_max_liquidity_usd`, `pending_weight_configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:1178` · `MiningActivityResource`

### OPERATION-069 · 运营>活动>挖矿管理>活动管理-编辑保存挖矿活动 

- 接口声明：`PUT /activity`
- 输入字段：`id`, `markets`, `mining_asset`, `start_date`, `duration`, `details`, `join_user_type`, `daily_output`, `hourly_output`, `business_type`, `trade_mode`, `pledge_asset`, `user_daily_max_output`, `user_max_pledge_amount`, `user_min_pledge_amount`, `user_max_liquidity_usd`, `pending_weight_configs`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:1315` · `MiningActivityResource`

### OPERATION-070 · 运营>活动>挖矿管理>活动管理-挖矿活动-操作上下架 

- 接口声明：`PATCH /activity`
- 输入字段：`id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:1493` · `MiningActivityResource`

### OPERATION-071 · 运营-活动-挖矿管理-报名用户详情-用户操作历史 

- 接口声明：`GET /user-operate-history`
- 输入字段：`activity_id`, `operate_type`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/mining.py:1550` · `MiningUserOperateHistoryResource`

### OPERATION-072 · 运营-活动-七周年 

- 接口声明：`GET /user-rewards`
- 输入字段：`user_id`, `actual_reward`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/seventh.py:64` · `UserRewardListResource`

### OPERATION-073 · 运营-活动-六周年-周年闯关用户 

- 接口声明：`GET /user-rewards`
- 输入字段：`export`, `user_id`, `actual_reward`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/sixth.py:39` · `UserRewardListResource`

### OPERATION-074 · 运营-活动-六周年-周年闯关奖励 

- 接口声明：`GET /reward-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/activity/sixth.py:134` · `RewardInfoResource`

### OPERATION-075 · 系统-slack通知-获取通知配置

- 接口声明：`GET /slack`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/notice.py:21` · `SlackNotificationResource`

### OPERATION-076 · 系统-slack通知-修改通知配置

- 接口声明：`PUT /slack`
- 输入字段：`biz_name`, `config_name`, `config_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/notice.py:66` · `SlackNotificationResource`

### OPERATION-077 · 系统-slack通知-测试通知配置

- 接口声明：`POST /slack/test`
- 输入字段：`biz_name`, `config_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/notice.py:103` · `SlackNotificationTestResource`

### OPERATION-078 · 系统-slack通知-刷新缓存（频道和用户列表）

- 接口声明：`POST /slack/refresh-cache`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/notice.py:125` · `SlackCacheRefreshResource`

### OPERATION-079 · 系统-slack通知-还原通知文案

- 接口声明：`POST /slack/revert-content`
- 输入字段：`biz_name`, `config_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/notice.py:144` · `SlackNotificationRevertContentResource`

### OPERATION-080 · 运营-学院-类别管理

- 接口声明：`GET /categories`
- 输入字段：`parent_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:63` · `CategoryResource`

### OPERATION-081 · 运营-学院-类别详情

- 接口声明：`GET /category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:138` · `CategoryDetailResource`

### OPERATION-082 · 运营-学院-新建/编辑类别

- 接口声明：`PUT /category/<int:id_>`
- 输入字段：`parent_id`, `remark`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:154` · `CategoryDetailResource`

### OPERATION-083 · 运营-学院-删除类别

- 接口声明：`DELETE /category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:232` · `CategoryDetailResource`

### OPERATION-084 · 运营-学院-类别上移/下移

- 接口声明：`PUT /category/<int:id_>/sort`
- 输入字段：`sort_type`, `parent_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:263` · `CategorySortResource`

### OPERATION-085 · 运营-学院-类别拖拽排序

- 接口声明：`POST /category/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:310` · `CategorySortsResource`

### OPERATION-086 · 运营-学院-类别启用/禁用

- 接口声明：`PUT /category/<int:id_>/enable`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:334` · `CategoryEnableResource`

### OPERATION-087 · 运营-学院-标签管理

- 接口声明：`GET /tags`
- 输入字段：`name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:356` · `TagResource`

### OPERATION-088 · 运营-学院-标签详情

- 接口声明：`GET /tag/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:393` · `TagDetailResource`

### OPERATION-089 · 运营-学院-编辑/新建标签

- 接口声明：`PUT /tag/<int:id_>`
- 输入字段：`remark`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:409` · `TagDetailResource`

### OPERATION-090 · 运营-学院-标签删除

- 接口声明：`DELETE /tag/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:472` · `TagDetailResource`

### OPERATION-091 · 运营-学院-标签启用/禁用

- 接口声明：`PUT /tag/<int:id_>/enable`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:492` · `TagEnableResource`

### OPERATION-092 · 运营-学院-标签搜索框是否展示

- 接口声明：`PUT /tag/<int:id_>/display`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:515` · `TagDisplayResource`

### OPERATION-093 · 运营-学院-文章管理

- 接口声明：`GET /articles`
- 输入字段：`primary_category_id`, `secondary_category_id`, `status`, `start_time`, `end_time`, `lang`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:559` · `ArticleResource`

### OPERATION-094 · 运营-学院-文章是否热门

- 接口声明：`PUT /article/<int:id_>/hot`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:698` · `ArticleIsHotResource`

### OPERATION-095 · 运营-学院-文章是否展示首页

- 接口声明：`PUT /article/<int:id_>/front`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:720` · `ArticleIsFrontResource`

### OPERATION-096 · 运营-学院-文章详情

- 接口声明：`GET /article/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:753` · `ArticleDetailsResource`

### OPERATION-097 · 运营-学院-文章新建/编辑

- 接口声明：`PUT /article/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:842` · `ArticleDetailsResource`

### OPERATION-098 · 运营-学院-文章提交审核

- 接口声明：`PATCH /article/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:996` · `ArticleDetailsResource`

### OPERATION-099 · 运营-学院-文章删除

- 接口声明：`DELETE /article/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1032` · `ArticleDetailsResource`

### OPERATION-100 · 运营-学院-文章编辑（强制）

- 接口声明：`PUT /article/<int:id_>/force-submit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1057` · `ArticleDetailsSubmitResource`

### OPERATION-101 · 运营-学院-文章内容删除

- 接口声明：`DELETE /article/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1069` · `ArticleContentResource`

### OPERATION-102 · 运营-学院-文章审核

- 接口声明：`PATCH /article/<int:id_>/audit`
- 输入字段：`status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1095` · `ArticleDetailsAuditResource`

### OPERATION-103 · 运营-学院-文章取消审核

- 接口声明：`PATCH /article/<int:id_>/cancel-audit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1136` · `ArticleCancelAuditResource`

### OPERATION-104 · 运营-学院-文章下架

- 接口声明：`PATCH /article/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1164` · `ArticleDetailsOfflineResource`

### OPERATION-105 · 运营-学院-文章拖拽排序

- 接口声明：`POST /article/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1195` · `ArticleSortsResource`

### OPERATION-106 · 运营-学院-文章导航栏

- 接口声明：`GET /side/categories`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1219` · `SideCategoryResource`

### OPERATION-107 · 运营-学院-文章搜索

- 接口声明：`GET /article/search`
- 输入字段：`keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1264` · `ArticleSearchResource`

### OPERATION-108 · 运营-学院-批量上传文章

- 接口声明：`POST /articles/batch-upload`
- 输入字段：`articles`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1303` · `ArticleBatchUploadResource`

### OPERATION-109 · 运营-学院-批量提交审核

- 接口声明：`POST /articles/batch-submit`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1523` · `ArticleBatchSubmitResource`

### OPERATION-110 · 运营-学院-批量审核

- 接口声明：`POST /articles/batch-audit`
- 输入字段：`ids`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/academy.py:1585` · `ArticleBatchAuditResource`

### OPERATION-111 · 运营-活动-交易排名-交易赛分渠道统计

- 接口声明：`GET /perpetual-trade-rank/channel-statistic`
- 输入字段：`export`, `activity_id`, `time_type`, `start_time`, `end_time`, `channels`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:40` · `PerpetualTradeRankChannelStatisticResource`

### OPERATION-112 · 运营-运营管理-减半活动-列表

- 接口声明：`GET /coin-halving/list`
- 输入字段：`name`, `status`, `begin_at`, `end_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:217` · `CoinHalvingResource`

### OPERATION-113 · 运营-运营管理-减半活动-创建减半活动

- 接口声明：`POST /coin-halving/list`
- 输入字段：`name`, `begin_at`, `end_at`, `url`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:262` · `CoinHalvingResource`

### OPERATION-114 · 运营-运营管理-减半活动-获取单条活动

- 接口声明：`GET /coin-halving/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:302` · `CoinHalvingContentResource`

### OPERATION-115 · 运营-运营管理-减半活动-编辑活动

- 接口声明：`PATCH /coin-halving/<int:id_>`
- 输入字段：`name`, `begin_at`, `end_at`, `url`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:321` · `CoinHalvingContentResource`

### OPERATION-116 · 运营-运营管理-减半活动-删除活动

- 接口声明：`DELETE /coin-halving/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:363` · `CoinHalvingContentResource`

### OPERATION-117 · 运营-运营管理-减半活动-获取单条banner内容

- 接口声明：`GET /coin-halving/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:387` · `CoinHalvingContentLangResource`

### OPERATION-118 · 运营-运营管理-减半活动-编辑单条banner内容

- 接口声明：`POST /coin-halving/<int:id_>/langs/<lang>/img`
- 输入字段：`same_as`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:412` · `CoinHalvingContentImageResource`

### OPERATION-119 · 运营-运营管理-减半活动-删除banner

- 接口声明：`DELETE /coin-halving/<int:id_>/langs/<lang>/img`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/activity.py:492` · `CoinHalvingContentImageResource`

### OPERATION-120 · 运营-风控-KYC Pro-PDF AI分析

- 接口声明：`POST /kyc-pro/pdf`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ai_analyze.py:73` · `AIPDFAnalyze`

### OPERATION-121 · 运营-活动-大使活动-管理列表

- 接口声明：`GET /activities`
- 输入字段：`type`, `state`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:130` · `AmbassadorActivityListResource`

### OPERATION-122 · 运营-活动-大使活动-创建

- 接口声明：`POST /activities`
- 输入字段：`type`, `started_at`, `ended_at`, `applying_ended_at`, `min_gift_amount`, `gift_asset`, `rule_other`, `rule_top`, `gift_rules`, `titles`, `open_normal_amb_max_rate`, `normal_amb_max_rate`, `open_business_amb_max_rate`, `business_amb_max_rate`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:234` · `AmbassadorActivityListResource`

### OPERATION-123 · 运营-活动-大使活动-编辑

- 接口声明：`PUT /activity/<int:id_>`
- 输入字段：`type`, `started_at`, `ended_at`, `applying_ended_at`, `min_gift_amount`, `gift_asset`, `rule_other`, `rule_top`, `gift_rules`, `titles`, `open_normal_amb_max_rate`, `normal_amb_max_rate`, `open_business_amb_max_rate`, `business_amb_max_rate`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:324` · `AmbassadorActivityResource`

### OPERATION-124 · 运营-活动-大使活动-上下架

- 接口声明：`PATCH /activity/<int:id_>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:400` · `AmbassadorActivityResource`

### OPERATION-125 · 运营-活动-大使活动-报名用户

- 接口声明：`GET /activity/users`
- 输入字段：`user_id`, `activity_id`, `status`, `sort_type`, `amb_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:458` · `AmbassadorActivityJoinUsersResource`

### OPERATION-126 · 运营-活动-大使活动-添加/移除黑名单

- 接口声明：`PUT /activity/users`
- 输入字段：`user_id`, `activity_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:653` · `AmbassadorActivityJoinUsersResource`

### OPERATION-127 · 运营-活动-大使活动-报名用户-邀请用户明细

- 接口声明：`GET /activity/user-details`
- 输入字段：`user_id`, `ambassador_user_id`, `activity_id`, `status`, `type`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:712` · `AmbassadorActivityUserDetailsResource`

### OPERATION-128 · 运营-活动-大使活动-报名用户-邀请用户明细-修改

- 接口声明：`PUT /activity/user-details`
- 输入字段：`user_id`, `ambassador_user_id`, `activity_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:780` · `AmbassadorActivityUserDetailsResource`

### OPERATION-129 · 运营-活动-大使活动-模板下载

- 接口声明：`GET /activity/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:822` · `AmbassadorActivityTemplateResource`

### OPERATION-130 · 运营-活动-大使活动-黑名单用户批量上传

- 接口声明：`POST /activity/<int:activity_id>/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:838` · `AmbassadorActivityBatchResource`

### OPERATION-131 · 运营-活动-大使活动-派奖

- 接口声明：`POST /activity/<int:id_>/gift`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:899` · `AmbassadorActivityGiftResource`

### OPERATION-132 · 运营-活动-大使活动-派奖排除清退用户

- 接口声明：`PATCH /activity/<int:id_>/gift`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/ambassador.py:930` · `AmbassadorActivityGiftResource`

### OPERATION-133 · 运营-APP-证书管理列表

- 接口声明：`GET /app-cert`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/app.py:19` · `AppCertResource`

### OPERATION-134 · 运营-APP-指纹匹配设置

- 接口声明：`PATCH /app-cert`
- 输入字段：`check_enabled`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/app.py:47` · `AppCertResource`

### OPERATION-135 · 运营-APP-新增证书指纹

- 接口声明：`POST /app-cert`
- 输入字段：`platform`, `cert`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/app.py:56` · `AppCertResource`

### OPERATION-136 · 运营-APP-编辑证书指纹

- 接口声明：`PUT /app-cert`
- 输入字段：`id`, `platform`, `cert`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/app.py:92` · `AppCertResource`

### OPERATION-137 · 运营-APP-删除证书指纹

- 接口声明：`DELETE /app-cert`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/app.py:131` · `AppCertResource`

### OPERATION-138 · 慈善-获取banner

- 接口声明：`GET /banner`
- 输入字段：`status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:32` · `CharityBannerResource`

### OPERATION-139 · 慈善-新增banner

- 接口声明：`POST /banner`
- 输入字段：`status`, `name`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:52` · `CharityBannerResource`

### OPERATION-140 · 慈善-获取banner详情

- 接口声明：`GET /banner/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:96` · `CharityBannerDetailResource`

### OPERATION-141 · 慈善-修改banner

- 接口声明：`PUT /banner/<int:id_>`
- 输入字段：`status`, `name`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:114` · `CharityBannerDetailResource`

### OPERATION-142 · 慈善-删除banner

- 接口声明：`DELETE /banner/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:162` · `CharityBannerDetailResource`

### OPERATION-143 · 慈善-排序banner

- 接口声明：`PUT /banner/<int:id_>/sort`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:202` · `CharityBannerSortResource`

### OPERATION-144 · 慈善-获取捐赠数据

- 接口声明：`GET /donation`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:239` · `CharityDonationResource`

### OPERATION-145 · 慈善-修改捐赠数据

- 接口声明：`POST /donation`
- 输入字段：`id`, `data_type`, `data_value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:260` · `CharityDonationResource`

### OPERATION-146 · 慈善-获取活动

- 接口声明：`GET /activities`
- 输入字段：`status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:293` · `CharityActivitiesResource`

### OPERATION-147 · 慈善-增加活动

- 接口声明：`POST /activities`
- 输入字段：`name`, `status`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:314` · `CharityActivitiesResource`

### OPERATION-148 · 慈善-获取活动信息

- 接口声明：`GET /activities/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:355` · `CharityActivitiesDetailResource`

### OPERATION-149 · 慈善-修改活动

- 接口声明：`PUT /activities/<int:id_>`
- 输入字段：`name`, `status`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:375` · `CharityActivitiesDetailResource`

### OPERATION-150 · 慈善-删除活动

- 接口声明：`DELETE /activities/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:435` · `CharityActivitiesDetailResource`

### OPERATION-151 · 慈善-排序活动

- 接口声明：`PUT /activities/<int:id_>/sort`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:469` · `CharityActivitiesSortResource`

### OPERATION-152 · 慈善-获取 video

- 接口声明：`GET /video`
- 输入字段：`lang`, `category_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:663` · `CharityVideoResource`

### OPERATION-153 · 慈善-新增 video

- 接口声明：`POST /video`
- 输入字段：`name`, `category_id`, `status`, `lang`, `title`, `url`, `file_key`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:704` · `CharityVideoResource`

### OPERATION-154 · 慈善-获取 video 详情

- 接口声明：`GET /video/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:747` · `CharityVideoDetailResource`

### OPERATION-155 · 慈善-修改 video

- 接口声明：`PUT /video/<int:id_>`
- 输入字段：`name`, `category_id`, `status`, `lang`, `title`, `url`, `file_key`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:773` · `CharityVideoDetailResource`

### OPERATION-156 · 慈善-删除 video

- 接口声明：`DELETE /video/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:805` · `CharityVideoDetailResource`

### OPERATION-157 · 慈善-排序 video

- 接口声明：`PUT /video/<int:id_>/sort`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:831` · `CharityVideoSortResource`

### OPERATION-158 · 慈善-拖拽排序 video

- 接口声明：`POST /video/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:857` · `CharityVideoSortsResource`

### OPERATION-159 · 慈善-类别管理

- 接口声明：`GET /category`
- 输入字段：`page`, `limit`, `lang`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:875` · `CategoryResource`

### OPERATION-160 · 慈善-添加类别

- 接口声明：`POST /category`
- 输入字段：`name`, `remark`, `lang`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:905` · `CategoryResource`

### OPERATION-161 · 慈善-修改类别

- 接口声明：`PUT /category/<int:id_>`
- 输入字段：`name`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:939` · `CategoryDetailResource`

### OPERATION-162 · 慈善-删除类别

- 接口声明：`DELETE /category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:961` · `CategoryDetailResource`

### OPERATION-163 · 慈善-类别管理-移动

- 接口声明：`PUT /category/<int:id_>/sort_id`
- 输入字段：`sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:986` · `CategorySortResource`

### OPERATION-164 · 慈善-慈善足迹类别管理

- 接口声明：`GET /footprint/category`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1031` · `FootPrintCategoryResource`

### OPERATION-165 · 慈善-添加慈善足迹类别

- 接口声明：`POST /footprint/category`
- 输入字段：`cn_name`, `en_name`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1054` · `FootPrintCategoryResource`

### OPERATION-166 · 慈善-修改慈善足迹类别

- 接口声明：`PUT /footprint/category/<int:id_>`
- 输入字段：`cn_name`, `en_name`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1087` · `FootPrintCategoryDetailResource`

### OPERATION-167 · 慈善-删除慈善足迹类别

- 接口声明：`DELETE /footprint/category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1112` · `FootPrintCategoryDetailResource`

### OPERATION-168 · 慈善-慈善足迹类别管理-移动

- 接口声明：`PUT /footprint/category/<int:id_>/sort_id`
- 输入字段：`sort_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1137` · `FootPrintCategorySortResource`

### OPERATION-169 · 慈善-足迹

- 接口声明：`GET /footprints`
- 输入字段：`category_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1177` · `FootPrintResource`

### OPERATION-170 · 慈善-创建足迹

- 接口声明：`POST /footprints`
- 输入字段：`category_id`, `is_use_blog`, `status`, `translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1213` · `FootPrintResource`

### OPERATION-171 · 慈善-足迹详情

- 接口声明：`GET /footprint/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1282` · `FootprintDetailResource`

### OPERATION-172 · 慈善-足迹编辑

- 接口声明：`PATCH /footprint/<int:id_>`
- 输入字段：`category_id`, `is_use_blog`, `status`, `translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1325` · `FootprintDetailResource`

### OPERATION-173 · 慈善-足迹下架

- 接口声明：`DELETE /footprint/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1377` · `FootprintDetailResource`

### OPERATION-174 · 慈善-足迹上架

- 接口声明：`PUT /footprint/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1397` · `FootprintDetailResource`

### OPERATION-175 · 慈善-足迹排序

- 接口声明：`PUT /footprint/<int:id_>/sort`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1418` · `FootprintSortResource`

### OPERATION-176 · 慈善-足迹拖拽排序

- 接口声明：`POST /footprint/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/charity.py:1444` · `CharityFootprintSortResource`

### OPERATION-177 · 运营-WEB-首页插画

- 接口声明：`GET /new`
- 输入字段：`display_name`, `begin_at`, `end_at`, `activate_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/inset.py:79` · `NewInsetConfigListResource`

### OPERATION-178 · 运营-WEB-首页插画详情

- 接口声明：`GET /new/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/inset.py:142` · `NewInsetConfigResource`

### OPERATION-179 · 运营-WEB-新建/编辑首页插画

- 接口声明：`PUT /new/<int:id_>`
- 输入字段：`display_name`, `url`, `begin_at`, `end_at`, `content_style`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/inset.py:161` · `NewInsetConfigResource`

### OPERATION-180 · 运营-WEB-删除首页插画

- 接口声明：`DELETE /new/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/inset.py:202` · `NewInsetConfigResource`

### OPERATION-181 · 运营-WEB-下架首页插画

- 接口声明：`PATCH /new/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/inset.py:220` · `NewInsetConfigOfflineResource`

### OPERATION-182 · 运营-WEB-首页插画语言详情

- 接口声明：`GET /new/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/inset.py:239` · `NewInsetConfigContentResource`

### OPERATION-183 · 运营-WEB-编辑首页插画语言内容

- 接口声明：`PUT /new/<int:id_>/langs/<lang>`
- 输入字段：`title`, `sub_title`, `button_text`, `url`, `light_pic_id`, `dark_pic_id`, `light_background_color`, `light_title_color`, `light_subtitle_color`, `dark_background_color`, `dark_title_color`, `dark_subtitle_color`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/inset.py:282` · `NewInsetConfigContentResource`

### OPERATION-184 · 资讯-推送PUSH（洞察文章）

- 接口声明：`POST /push`
- 输入字段：`id`, `name`, `push_type`, `push_time`, `remark`, `ttl`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:51` · `PushResource`

### OPERATION-185 · Insight-内容管理

- 接口声明：`GET `
- 输入字段：`title`, `article_type`, `publish_start`, `publish_end`, `seo_url_keyword`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:133` · `ListResource`

### OPERATION-186 · Insight-内容启用/禁用

- 接口声明：`PUT /<object_id>/enable`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:209` · `InsightEnableResource`

### OPERATION-187 · Insight-广告位启用/禁用

- 接口声明：`PUT /<object_id>/ads/enable`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:268` · `InsightAdsEnableResource`

### OPERATION-188 · Insight-同步资讯数据

- 接口声明：`PUT /<object_id>/update-information`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:304` · `InsightUpdateInformationResource`

### OPERATION-189 · Insight-内容详情

- 接口声明：`GET /<object_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:318` · `DetailResource`

### OPERATION-190 · Insight-内容删除

- 接口声明：`DELETE /<object_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:379` · `DetailResource`

### OPERATION-191 · Insight-内容编辑

- 接口声明：`PUT /<object_id>`
- 输入字段：`title`, `seo_url_keyword`, `publish_at`, `article_type`, `report_type`, `coins`, `remark`, `contents`, `force_submit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:399` · `DetailResource`

### OPERATION-192 · Insight-内容置顶/取消置顶

- 接口声明：`PATCH /<object_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:530` · `DetailResource`

### OPERATION-193 · Insight-内容详情-分词

- 接口声明：`POST /participle`
- 输入字段：`lang`, `title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/insight.py:574` · `ParticipleResource`

### OPERATION-194 · 运营-视频文件列表

- 接口声明：`GET /video-list`
- 输入字段：`page`, `limit`, `id`, `name`, `business`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/media.py:49` · `MediaVideoListResource`

### OPERATION-195 · 获取视频相关枚举

- 接口声明：`GET /video/enums`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/media.py:148` · `MediaVideoEnumsResource`

### OPERATION-196 · 运营管理-视频新建

- 接口声明：`POST /video`
- 输入字段：`name`, `file_id`, `file_key`, `cover_key`, `business`, `platform`, `lang`, `subtitle`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/media.py:241` · `MediaVideoNewResource`

### OPERATION-197 · 业务视频管理-查询是否已经存在跟该视频同样语言，同样目标展示位的视频

- 接口声明：`GET /video/<video_id>`
- 输入字段：`business`, `platform`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/media.py:334` · `MediaVideoBusinessResource`

### OPERATION-198 · 业务视频管理-删除视频

- 接口声明：`DELETE /video/<video_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/media.py:351` · `MediaVideoBusinessResource`

### OPERATION-199 · 业务视频管理-分配展示位置

- 接口声明：`PUT /video/<video_id>`
- 输入字段：`platform`, `business`, `subtitle`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/media.py:441` · `MediaVideoBusinessResource`

### OPERATION-200 · 业务视频管理-分配展示位置

- 接口声明：`POST /video/<video_id>/translate`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/media.py:476` · `MediaVideoTranslateResource`

### OPERATION-201 · 运营-任务中心-新手任务推送列表

- 接口声明：`GET `
- 输入字段：`scene_type`, `plan_id`, `status`, `channel`, `business_party`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:440` · `MissionPlanListResource`

### OPERATION-202 · 运营-任务中心-创建新手任务推送

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:586` · `MissionPlanListResource`

### OPERATION-203 · 运营-任务中心-检查客群推送情况

- 接口声明：`POST /check-channel-params`
- 输入字段：`channel`, `logic_params`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:605` · `MissionPlanCheckChannelParams`

### OPERATION-204 · 运营-任务中心-获取新手任务推送详情

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:639` · `MissionPlanDetailResource`

### OPERATION-205 · 运营-任务中心-修改新手任务推送详情

- 接口声明：`PUT /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:652` · `MissionPlanDetailResource`

### OPERATION-206 · 运营-任务中心-新手任务-提交审核

- 接口声明：`PATCH /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:671` · `MissionPlanDetailResource`

### OPERATION-207 · 运营-任务中心-新手任务-删除推送

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:689` · `MissionPlanDetailResource`

### OPERATION-208 · 运营-任务中心-新手/老手任务推送-审核通过/拒绝审核

- 接口声明：`POST /<int:id_>/review`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:704` · `MissionPlanReviewResource`

### OPERATION-209 · 运营-任务中心-新手/老手任务推送-批量审核通过/拒绝审核

- 接口声明：`POST /batch-review`
- 输入字段：`ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:744` · `MissionPlanBatchReviewResource`

### OPERATION-210 · 运营-任务中心-新手任务-暂停推送

- 接口声明：`POST /<int:id_>/stop`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:808` · `MissionPlanStopResource`

### OPERATION-211 · 运营-任务中心-新手任务-暂停推送

- 接口声明：`POST /<int:id_>/pause`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:823` · `MissionPlanPauseResource`

### OPERATION-212 · 运营-任务中心-新手任务-恢复推送

- 接口声明：`POST /<int:id_>/resume`
- 输入字段：`event_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:838` · `MissionPlanResumeResource`

### OPERATION-213 · 运营-任务中心-新手任务-更新推送内容

- 接口声明：`PUT /<int:id_>/update-content`
- 输入字段：`deliver_content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:886` · `MissionPlanUpdateContentResource`

### OPERATION-214 · 运营-任务中心-新手任务明细列表

- 接口声明：`GET /user-mission`
- 输入字段：`scene_type`, `user_id`, `plan_id`, `mission_id`, `status`, `push_status`, `reward_type`, `reward_status`, `cursor`, `created_at_start`, `created_at_end`, `completed_at_start`, `completed_at_end`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1094` · `UserMissionInfoResource`

### OPERATION-215 · 运营-任务中心-失败用户列表

- 接口声明：`GET /failed-users`
- 输入字段：`plan_id`, `page`, `limit`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1192` · `MissionFailedUsersResource`

### OPERATION-216 · 运营-任务中心-新手任务统计列表

- 接口声明：`GET /statistics`
- 输入字段：`scene_type`, `report_date_start`, `report_date_end`, `plan_id`, `mission_id`, `reward_type`, `mission_condition`, `limit`, `page`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1349` · `MissionStatisticsResource`

### OPERATION-217 · 运营-任务中心-老用户任务-列表

- 接口声明：`GET /routine`
- 输入字段：`page`, `limit`, `scene_id`, `plan_id`, `group_id`, `business_party`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1410` · `MissionPlanRoutineListResource`

### OPERATION-218 · 运营-任务中心-老用户任务-获取详情

- 接口声明：`GET /routine/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1548` · `MissionPlanRoutineResource`

### OPERATION-219 · 运营-任务中心-场景列表

- 接口声明：`GET /scenes`
- 输入字段：`scene_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1567` · `MissionSceneResource`

### OPERATION-220 · 运营-任务中心-场景创建

- 接口声明：`POST /scenes`
- 输入字段：`name`, `remark`, `scene_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1610` · `MissionSceneResource`

### OPERATION-221 · 运营-任务中心-场景更新

- 接口声明：`PUT /scenes`
- 输入字段：`id`, `name`, `remark`, `scene_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1636` · `MissionSceneResource`

### OPERATION-222 · 运营-任务中心-检查客群接受情况

- 接口声明：`POST /check-reception`
- 输入字段：`scene_id`, `group_ids`, `whitelist_user_ids`, `is_export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1671` · `MissionCheckReceptionResource`

### OPERATION-223 · 运营-任务中心-下载客群未接受用户

- 接口声明：`POST /download-unreachable-users`
- 输入字段：`scene_id`, `group_ids`, `whitelist_user_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1718` · `MissionDownloadUnreachableUsersResource`

### OPERATION-224 · 运营-任务中心-新手任务风控设置

- 接口声明：`GET /newbie-risk-settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1791` · `MissionNewbieRiskSettingsResource`

### OPERATION-225 · 运营-任务中心-新手任务风控设置

- 接口声明：`PUT /newbie-risk-settings/<risk_key>`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1807` · `MissionNewbieRiskSettingsDetailResource`

### OPERATION-226 · 运营-任务中心-新手任务风控设置详情

- 接口声明：`GET /newbie-risk-settings/<risk_key>/items`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1852` · `MissionNewbieRiskSettingsItemsResource`

### OPERATION-227 · 运营-任务中心-新增新手任务风控设置详情

- 接口声明：`POST /newbie-risk-settings/<risk_key>/items`
- 输入字段：`value`, `extra`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1878` · `MissionNewbieRiskSettingsItemsResource`

### OPERATION-228 · 运营-任务中心-新手任务风控设置详情-修改

- 接口声明：`PUT /newbie-risk-settings/<risk_key>/items/<int:id_>`
- 输入字段：`value`, `extra`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:1989` · `MissionNewbieRiskSettingsItemDetailResource`

### OPERATION-229 · 运营-任务中心-新手任务风控设置详情-删除

- 接口声明：`DELETE /newbie-risk-settings/<risk_key>/items/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:2018` · `MissionNewbieRiskSettingsItemDetailResource`

### OPERATION-230 · 运营-任务中心-新手任务风控用户

- 接口声明：`GET /newbie-risk-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:2205` · `MissionNewbieRiskUsersResource`

### OPERATION-231 · 运营-任务中心-新用户任务风控用户明细-获取额外需恢复明细

- 接口声明：`GET /newbie-risk-users/batch`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:2245` · `MissionNewbieRiskUserDetailResource`

### OPERATION-232 · 运营-任务中心-新用户任务风控用户明细-批量恢复

- 接口声明：`PATCH /newbie-risk-users/batch`
- 输入字段：`ids`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:2281` · `MissionNewbieRiskUserDetailResource`

### OPERATION-233 · 运营-任务中心-新用户任务风控事件明细

- 接口声明：`GET /newbie-risk-events`
- 输入字段：`id`, `setting_name`, `plan_id`, `country`, `start_at`, `end_at`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:2351` · `NewbieMissionRiskEventResource`

### OPERATION-234 · 运营-任务中心-新用户任务风控事件明细-修改备注

- 接口声明：`PATCH /newbie-risk-events/<id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:2486` · `MissionNewbieRiskEventDetailResource`

### OPERATION-235 · 运营-任务中心-新用户任务风控事件明细-恢复

- 接口声明：`POST /newbie-risk-events/<id_>/resume`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/mission.py:2512` · `MissionNewbieRiskEventDetailResumeResource`

### OPERATION-236 · 运营-运营管理-用户名/账户名屏蔽词列表

- 接口声明：`GET `
- 输入字段：`block_type`, `word`, `lang`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/name_block.py:34` · `NameBlockListResource`

### OPERATION-237 · 运营-运营管理-新增用户名/账户名屏蔽词

- 接口声明：`POST `
- 输入字段：`block_type`, `word`, `lang_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/name_block.py:135` · `NameBlockListResource`

### OPERATION-238 · 运营-运营管理-获取用户名/账户名屏蔽词详情

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/name_block.py:177` · `NameBlockDetailResource`

### OPERATION-239 · 运营-运营管理-修改用户名/账户名屏蔽词详情

- 接口声明：`PUT /<int:id_>`
- 输入字段：`word`, `lang_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/name_block.py:196` · `NameBlockDetailResource`

### OPERATION-240 · 运营-运营管理-删除用户名/账户名屏蔽词

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/name_block.py:224` · `NameBlockDetailResource`

### OPERATION-241 · 运营-触达管理-生成渲染 url

- 接口声明：`PUT /push/url`
- 输入字段：`urls`, `business_id`, `business`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:155` · `PushUrlResource`

### OPERATION-242 · 运营-触达管理-PUSH跳转站内信清单

- 接口声明：`GET /push/inner-message-jumps`
- 输入字段：`id`, `name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:278` · `PushInnerMessageJumpResource`

### OPERATION-243 · 运营-触达管理-PUSH选择站内信并生成跳转项

- 接口声明：`POST /push/inner-message-jumps/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:332` · `PushInnerMessageJumpItemResource`

### OPERATION-244 · 运营-触达管理-邮件推送

- 接口声明：`GET /email-pushes`
- 输入字段：`name`, `status`, `start_time`, `end_time`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:375` · `EmailPushesResource`

### OPERATION-245 · 运营-触达管理-邮件推送-创建

- 接口声明：`POST /email-pushes`
- 输入字段：`name`, `push_type`, `push_scope_type`, `push_time_type`, `push_time`, `remark`, `user_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `url_ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:439` · `EmailPushesResource`

### OPERATION-246 · 运营-触达管理-邮件推送详情

- 接口声明：`GET /email-pushes/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:497` · `EmailPushResource`

### OPERATION-247 · 运营-触达管理-邮件推送-编辑

- 接口声明：`PATCH /email-pushes/<int:id_>`
- 输入字段：`name`, `push_type`, `push_scope_type`, `push_time_type`, `push_time`, `remark`, `user_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `url_ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:584` · `EmailPushResource`

### OPERATION-248 · 运营-触达管理-邮件推送-删除

- 接口声明：`DELETE /email-pushes/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:652` · `EmailPushResource`

### OPERATION-249 · 运营-触达管理-邮件推送用户下载

- 接口声明：`GET /email-pushes/<int:id_>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:681` · `EmailPushUserResource`

### OPERATION-250 · 运营-触达管理-邮件推送-保存 url_ids

- 接口声明：`PATCH /email-pushes/<int:id_>/urls`
- 输入字段：`url_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:715` · `EmailPushUrlsResource`

### OPERATION-251 · 运营-触达管理-邮件推送-提交审核

- 接口声明：`PATCH /email-pushes/<int:id_>/created`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:750` · `EmailPushDraftResource`

### OPERATION-252 · 运营-触达管理-邮件推送-审核

- 接口声明：`PATCH /email-pushes/<int:id_>/audit`
- 输入字段：`status`, `auditor_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:778` · `EmailPushAuditResource`

### OPERATION-253 · 运营-邮件推送-获取邮件推送内容

- 接口声明：`GET /email-pushes/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:823` · `EmailPushContentResource`

### OPERATION-254 · 运营-邮件推送-编辑邮件推送内容

- 接口声明：`PUT /email-pushes/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:837` · `EmailPushContentResource`

### OPERATION-255 · 邮件测试-检查

- 接口声明：`GET /email-pushes/<int:id_>/test`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:903` · `EmailPushContentTestResource`

### OPERATION-256 · 运营-触达管理-内容邮件测试

- 接口声明：`POST /email-pushes/<int:id_>/test`
- 输入字段：`accounts`, `push_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:916` · `EmailPushContentTestResource`

### OPERATION-257 · 运营-邮件推送-获取邮件退订列表

- 接口声明：`GET /email-push-unsubscriptions`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1022` · `EmailPushUnsubscriptionsResource`

### OPERATION-258 · 运营-邮件推送-筛选用户(仅用作历史记录展示)

- 接口声明：`GET /email-push/filter-configs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1055` · `EmailPushFilterConfigsResource`

### OPERATION-259 · EmailPushTemplateResource.get（用途待确认）

- 接口声明：`GET /email-push/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1084` · `EmailPushTemplateResource`

### OPERATION-260 · 运营-导入用户

- 接口声明：`POST /email-push/imports`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1102` · `EmailPushImportsResource`

### OPERATION-261 · 运营-触达管理-下架资产邮件推送

- 接口声明：`GET /asset-offline-push`
- 输入字段：`name`, `status`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1173` · `AssetOfflineEmailPushResource`

### OPERATION-262 · 运营-触达管理-下架资产邮件推送-创建

- 接口声明：`POST /asset-offline-push`
- 输入字段：`name`, `push_scope_type`, `remark`, `whitelist_enabled`, `user_whitelist`, `url_ids`, `status`, `key`, `type`, `started_at`, `ended_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1236` · `AssetOfflineEmailPushResource`

### OPERATION-263 · 运营-触达管理-下架资产邮件推送-详情

- 接口声明：`GET /asset-offline-push/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1303` · `AssetOfflineEmailPushDetailResource`

### OPERATION-264 · 运营-触达管理-下架资产邮件推送-编辑

- 接口声明：`PATCH /asset-offline-push/<int:id_>`
- 输入字段：`name`, `push_scope_type`, `started_at`, `ended_at`, `key`, `type`, `remark`, `whitelist_enabled`, `user_whitelist`, `url_ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1316` · `AssetOfflineEmailPushDetailResource`

### OPERATION-265 · 运营-触达管理-下架资产邮件推送-用户下载

- 接口声明：`GET /asset-offline-push/<int:id_>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1390` · `AssetOfflineEmailPushUserResource`

### OPERATION-266 · 运营-触达管理-邮件推送-上传文件生成邮件记录

- 接口声明：`POST /email-push/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1418` · `EmailPushUploadResource`

### OPERATION-267 · 运营-币种申请-币种申请列表

- 接口声明：`GET /coin-application-list`
- 输入字段：`type`, `status`, `is_first`, `id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1580` · `CoinApplicationListResource`

### OPERATION-268 · 运营-币种申请-批量审核

- 接口声明：`PATCH /coin-application-list`
- 输入字段：`ids`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1606` · `CoinApplicationListResource`

### OPERATION-269 · 运营-币种申请-币种申请搜索

- 接口声明：`GET /coin-application`
- 输入字段：`keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1650` · `CoinApplicationResource`

### OPERATION-270 · 运营-币种申请-修改币种申请状态

- 接口声明：`PATCH /coin-application/<int:id_>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1676` · `CoinApplicationDetailResource`

### OPERATION-271 · 运营-币种申请-融资申请列表

- 接口声明：`GET /ieo-application-list`
- 输入字段：`type`, `status`, `is_first`, `id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1779` · `IeoApplicationListResource`

### OPERATION-272 · 运营-融资申请-修改融资申请状态

- 接口声明：`PATCH /ieo-application-list/<int:id_>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1810` · `IeoApplicationDetailResource`

### OPERATION-273 · 运营-融资申请-融资申请搜索

- 接口声明：`GET /ieo-application`
- 输入字段：`keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1844` · `IeoApplicationResource`

### OPERATION-274 · 运营-cbox-主题列表

- 接口声明：`GET /c-box/themes`
- 输入字段：`category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1871` · `CBoxThemesResource`

### OPERATION-275 · 运营-cbox-新增主题

- 接口声明：`POST /c-box/themes`
- 输入字段：`cover_file_key`, `thumbnail_file_key`, `receive_file_key`, `style`, `lang`, `category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:1972` · `CBoxThemesResource`

### OPERATION-276 · 运营-cbox-删除主题

- 接口声明：`DELETE /c-box/theme/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2020` · `CBoxThemeResource`

### OPERATION-277 · 运营-cbox-主题类型编辑

- 接口声明：`PUT /c-box-theme-category`
- 输入字段：`category_id`, `title`, `begin_at`, `end_at`, `type`, `languages`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2055` · `CBoxThemeCategoryResource`

### OPERATION-278 · 运营-cbox-主题类型列表

- 接口声明：`GET /c-box-theme-category`
- 输入字段：`page`, `limit`, `title`, `languages`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2136` · `CBoxThemeCategoryResource`

### OPERATION-279 · 运营-cbox-下架/上架主题类型

- 接口声明：`PATCH /c-box-theme-category`
- 输入字段：`category_id`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2229` · `CBoxThemeCategoryResource`

### OPERATION-280 · 运营-cbox-删除主题类型

- 接口声明：`DELETE /c-box-theme-category`
- 输入字段：`category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2262` · `CBoxThemeCategoryResource`

### OPERATION-281 · 运营-cbox-上移主题类型排名

- 接口声明：`PATCH /c-box-theme-category-rank-up/<int:category_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2289` · `CBoxThemeCategoryRankResource`

### OPERATION-282 · 运营-cbox-新增配置

- 接口声明：`POST /c-box/conf/only_new_user`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2322` · `CBoxConfsResource`

### OPERATION-283 · 运营-cbox-查询配置

- 接口声明：`GET /c-box/conf/only_new_user`
- 输入字段：`user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2364` · `CBoxConfsResource`

### OPERATION-284 · 运营-cbox-删除配置

- 接口声明：`DELETE /c-box/conf/only_new_user/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2397` · `CBoxConfResource`

### OPERATION-285 · 运营-cbox-获取口令列表

- 接口声明：`GET /c-box/code`
- 输入字段：`code`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2419` · `CBoxCodesResource`

### OPERATION-286 · 运营-cbox-为指定用户新增口令

- 接口声明：`POST /c-box/code`
- 输入字段：`code`, `user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2448` · `CBoxCodesResource`

### OPERATION-287 · 运营-cbox-口令详情

- 接口声明：`GET /c-box/code/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2482` · `CBoxCodeResource`

### OPERATION-288 · 运营-cbox-删除口令

- 接口声明：`DELETE /c-box/code/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2490` · `CBoxCodeResource`

### OPERATION-289 · 运营-cbox-特殊额度配置列表

- 接口声明：`GET /c-box/white-list`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2513` · `CBoxWhiteListResource`

### OPERATION-290 · 运营-cbox-新增特殊额度配置

- 接口声明：`POST /c-box/white-list`
- 输入字段：`user_id`, `daily_send_amount_limit`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2530` · `CBoxWhiteListResource`

### OPERATION-291 · 运营-cbox-编辑特殊额度配置

- 接口声明：`PATCH /c-box/white-list/<int:id_>`
- 输入字段：`user_id`, `daily_send_amount_limit`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2566` · `CBoxWhiteListDetailResource`

### OPERATION-292 · 运营-cbox-删除特殊额度配置

- 接口声明：`DELETE /c-box/white-list/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2591` · `CBoxWhiteListDetailResource`

### OPERATION-293 · 运营-红包-红包币种

- 接口声明：`GET /red-packet-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2611` · `RedPacketInfoResource`

### OPERATION-294 · 运营-红包-红包总览

- 接口声明：`GET /red-packet-overall`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2630` · `RedPacketOverallResource`

### OPERATION-295 · 运营-红包-红包记录

- 接口声明：`GET /red-packets`
- 输入字段：`asset`, `type`, `receive_type`, `code`, `status`, `user_id`, `red_packet_id`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2661` · `RedPacketListResource`

### OPERATION-296 · 运营-红包-红包详情

- 接口声明：`GET /red-packet-detail`
- 输入字段：`red_packet_id`, `asset`, `receive_email`, `receive_status`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2809` · `RedPacketDetailResource`

### OPERATION-297 · 运营-cbox-活动区列表

- 接口声明：`GET /c-box/promotion/list`
- 输入字段：`name`, `status`, `languages`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:2937` · `CBoxPromotionResource`

### OPERATION-298 · 运营-cbox-新建活动区

- 接口声明：`POST /c-box/promotion/list`
- 输入字段：`name`, `platform`, `begin_at`, `end_at`, `type`, `languages`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3040` · `CBoxPromotionResource`

### OPERATION-299 · 运营-cbox-活动区详情

- 接口声明：`GET /c-box/promotion/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3070` · `CBoxPromotionDetailResource`

### OPERATION-300 · 运营-cbox-活动区-编辑

- 接口声明：`PUT /c-box/promotion/<int:id_>`
- 输入字段：`name`, `platform`, `begin_at`, `end_at`, `type`, `languages`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3098` · `CBoxPromotionDetailResource`

### OPERATION-301 · 运营-cbox-活动区-删除

- 接口声明：`DELETE /c-box/promotion/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3132` · `CBoxPromotionDetailResource`

### OPERATION-302 · 运营-cbox-活动区-上架

- 接口声明：`PATCH /c-box/promotion/<int:id_>/online-offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3154` · `CBoxPromotionOnOffLineResource`

### OPERATION-303 · 运营-cbox-活动区-下架

- 接口声明：`DELETE /c-box/promotion/<int:id_>/online-offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3172` · `CBoxPromotionOnOffLineResource`

### OPERATION-304 · 运营-cbox-活动区-获取活动区内容

- 接口声明：`GET /c-box/promotion/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3194` · `CBoxPromotionContentResource`

### OPERATION-305 · 运营-cbox-活动区-编辑内容

- 接口声明：`PUT /c-box/promotion/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3216` · `CBoxPromotionContentResource`

### OPERATION-306 · 运营-KYC-KYC列表

- 接口声明：`GET /kyc`
- 输入字段：`page`, `limit`, `start_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3520` · `KYCListResource`

### OPERATION-307 · 运营-KYC-KYC个人列表导出

- 接口声明：`GET /kyc/export`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3703` · `KYCListExportResource`

### OPERATION-308 · 运营-KYC-查看单条kyc记录

- 接口声明：`GET /kyc/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3779` · `KYCResource`

### OPERATION-309 · 运营-KYC-编辑kyc

- 接口声明：`PATCH /kyc/<int:id_>`
- 输入字段：`name`, `id_number`, `id_type`, `country`, `nationality`, `gender`, `date_of_birth`, `doc_expire_date`, `remark`, `doc_name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:3789` · `KYCResource`

### OPERATION-310 · 运营-KYC-审核kyc

- 接口声明：`PUT /kyc/<int:id_>`
- 输入字段：`status`, `rejection_reason`, `custom_reject_reason`, `is_custom_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4184` · `KYCResource`

### OPERATION-311 · 运营-KYC-更新当前编辑者

- 接口声明：`POST /kyc/<int:id_>/auditors`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4293` · `KycVerificationAuditorsResource`

### OPERATION-312 · 风控-KYC-个人初级认证-批量分配审核人

- 接口声明：`POST /kyc/auditors`
- 输入字段：`auditor_ids`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4315` · `KycVerificationAssignAuditorsResource`

### OPERATION-313 · 风控-KYC-个人初级认证-批量解绑审核人

- 接口声明：`PATCH /kyc/auditors`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4351` · `KycVerificationAssignAuditorsResource`

### OPERATION-314 · 运营-KYC-第三方审核记录

- 接口声明：`GET /kyc/history`
- 输入字段：`status`, `reason`, `service_type`, `doc_type`, `transaction_id`, `user`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4392` · `KYCHistoryListResource`

### OPERATION-315 · 运营-KYC-补充认证第三方审核记录

- 接口声明：`GET /kyc/extend/history`
- 输入字段：`transaction_id`, `user`, `nationality`, `id_type`, `id_number`, `doc_type`, `status`, `start`, `end`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4505` · `KYCExtendHistoryListResource`

### OPERATION-316 · 运营-KYC-按用户查询非文件认证冷静期重置记录

- 接口声明：`GET /kyc/extend/history/clear-cooldown`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4657` · `KYCExtendHistoryUserClearCooldownResource`

### OPERATION-317 · 运营-KYC-按用户重置非文件认证冷静期

- 接口声明：`POST /kyc/extend/history/clear-cooldown`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4691` · `KYCExtendHistoryUserClearCooldownResource`

### OPERATION-318 · 运营-KYC-配置表

- 接口声明：`GET /kyc/country-configs`
- 输入字段：`page`, `limit`, `country`, `service_type`, `pro_service_type`, `pro_supported`, `allow_kyc_nationality`, `allow_kyc_country`, `is_two_step_verification_required`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4735` · `KYCCountryConfigsResource`

### OPERATION-319 · 运营-KYC-修改配置

- 接口声明：`PATCH /kyc/country-configs`
- 输入字段：`country`, `service_type`, `is_audit_required`, `pro_supported`, `pro_service_type`, `pro_is_audit_required`, `allow_kyc_nationality`, `allow_kyc_country`, `is_two_step_verification_required`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4816` · `KYCCountryConfigsResource`

### OPERATION-320 · 运营-KYC-机构认证列表

- 接口声明：`GET /kyc-institution`
- 输入字段：`country`, `status`, `keyword`, `beneficiary_id_number`, `register_code`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:4891` · `KYCInstitutionListResource`

### OPERATION-321 · 运营-KYC-机构认证详情

- 接口声明：`GET /kyc-institution/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5021` · `KYCInstitutionResource`

### OPERATION-322 · 运营-KYC-机构认证审核

- 接口声明：`PUT /kyc-institution/<int:id_>`
- 输入字段：`reject_reason`, `is_custom_reason`, `custom_reject_reason`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5273` · `KYCInstitutionResource`

### OPERATION-323 · 运营-KYC-机构认证修改

- 接口声明：`POST /kyc-institution/<int:id_>`
- 输入字段：`company_info`, `beneficiary_info`, `non_beneficiary_info`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5328` · `KYCInstitutionResource`

### OPERATION-324 · 运营-KYC-机构认证备注

- 接口声明：`PATCH /kyc-institution/<int:id_>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5432` · `KYCInstitutionRemarkResource`

### OPERATION-325 · 运营-KYC 机构认证-更新当前编辑者

- 接口声明：`POST /kyc-institution/<int:id_>/auditors`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5461` · `KYCInstitutionAuditorsResource`

### OPERATION-326 · 运营-活动-活动信息

- 接口声明：`GET /activities/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5483` · `ActivitiesInfoResource`

### OPERATION-327 · 运营-活动-送币历史

- 接口声明：`GET /activities/gift-history`
- 输入字段：`activity_id`, `asset`, `status`, `start_time`, `end_time`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5516` · `GiftHistoryResource`

### OPERATION-328 · 运营-活动-充值送币活动列表

- 接口声明：`GET /activities/deposit`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5672` · `DepositListResource`

### OPERATION-329 · 运营-活动-创建充值送币活动

- 接口声明：`POST /activities/deposit`
- 输入字段：`name`, `zendesk_url`, `deposit_asset`, `gift_asset`, `type`, `rule_data`, `least_amount`, `total_amount`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5683` · `DepositListResource`

### OPERATION-330 · 运营-活动-充值活动统计信息

- 接口声明：`GET /activities/deposit/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5745` · `DepositActivityResource`

### OPERATION-331 · 运营-活动-编辑充值送币活动

- 接口声明：`PUT /activities/deposit/<int:id_>`
- 输入字段：`zendesk_url`, `deposit_asset`, `gift_asset`, `type`, `rule_data`, `least_amount`, `total_amount`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5792` · `DepositActivityResource`

### OPERATION-332 · 运营-活动-编辑充值送币状态

- 接口声明：`PATCH /activities/deposit/<int:id_>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5847` · `DepositActivityResource`

### OPERATION-333 · 运营-活动-充值送币派奖

- 接口声明：`POST /activities/deposit-send-gift/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5872` · `DepositSendGiftResource`

### OPERATION-334 · 运营-活动-充值送币排行

- 接口声明：`GET /activities/deposit-rank`
- 输入字段：`deposit_activity_id`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:5915` · `DepositRankResource`

### OPERATION-335 · 运营-活动-交易送币活动列表

- 接口声明：`GET /activities/trade/list`
- 输入字段：`type`, `gift_asset`, `state`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6042` · `TradeRankActivityListResource`

### OPERATION-336 · 运营-活动-创建交易送币活动

- 接口声明：`POST /activities/trade/list`
- 输入字段：`markets`, `exclude_markets`, `market_type`, `gift_asset`, `type`, `gift_rules`, `least_trade_amount`, `announce_url`, `max_split_reward_amount`, `gift_amount`, `start_time`, `end_time`, `user_group_condition`, `titles`, `cover`, `funding_source`, `broker_id`, `broker_logo`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6143` · `TradeRankActivityListResource`

### OPERATION-337 · 运营-活动-渠道奖励活动列表

- 接口声明：`GET /activities/channel/list`
- 输入字段：`languages`, `platforms`, `assets`, `started_at`, `ended_at`, `state`, `page`, `limit`, `export`, `activity_url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6298` · `ChannelActivityListResource`

### OPERATION-338 · 运营-活动-渠道奖励送币活动

- 接口声明：`POST /activities/channel/list`
- 输入字段：`languages`, `platforms`, `name`, `activity_url`, `reward_url`, `remark`, `message_temp_id`, `reward_type`, `message_type`, `gift_rules`, `started_at`, `ended_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6497` · `ChannelActivityListResource`

### OPERATION-339 · 运营-活动-编辑渠道奖励送币活动

- 接口声明：`PUT /activities/channel-reward/<int:id_>`
- 输入字段：`languages`, `platforms`, `name`, `reward_type`, `message_type`, `gift_rules`, `activity_url`, `reward_url`, `remark`, `message_temp_id`, `started_at`, `ended_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6557` · `ChannelRewardActivityDetailResource`

### OPERATION-340 · 运营-活动-编辑渠道奖励状态

- 接口声明：`PATCH /activities/channel-reward/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6604` · `ChannelRewardActivityDetailResource`

### OPERATION-341 · 运营-活动-删除渠道奖励活动

- 接口声明：`DELETE /activities/channel-reward/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6628` · `ChannelRewardActivityDetailResource`

### OPERATION-342 · 活动-渠道活动-参与用户

- 接口声明：`GET /activities/channel-reward/users`
- 输入字段：`user_id`, `assets`, `channel_reward_activity_id`, `status`, `page`, `limit`, `languages`, `reward_start_time`, `reward_end_time`, `activity_url`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:6691` · `ChannelRewardActivityJoinUsersResource`

### OPERATION-343 · 活动-渠道活动-编辑用户状态

- 接口声明：`PUT /activities/channel-reward/users`
- 输入字段：`id`, `channel_reward_activity_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7029` · `ChannelRewardActivityJoinUsersResource`

### OPERATION-344 · 活动-渠道活动-新增平台

- 接口声明：`POST /activities/channel-reward/platform`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7081` · `ActivityChannelPlatformResource`

### OPERATION-345 · 活动-渠道活动-模板下载

- 接口声明：`GET /activities/channel-reward/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7121` · `ChannelRewardActivityTemplateResource`

### OPERATION-346 · 活动-渠道奖励-活动用户批量上传

- 接口声明：`POST /activities/channel-reward/<int:channel_reward_activity_id>/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/operation/operation.py:7142` · `ChannelRewardActivityBatchResource`

### OPERATION-347 · 运营-活动-渠道活动审核

- 接口声明：`POST /activities/channel-reward/<int:id_>/audit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/operation/operation.py:7313` · `ChannelRewardAuditResource`

### OPERATION-348 · 运营-活动-渠道奖励派奖

- 接口声明：`POST /activities/channel-reward/<int:id_>/gift`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/operation/operation.py:7498` · `ChannelRewardGiftResource`

### OPERATION-349 · 运营-活动-渠道奖励校验用户

- 接口声明：`PATCH /activities/channel-reward/<int:id_>/gift`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7537` · `ChannelRewardGiftResource`

### OPERATION-350 · 运营-活动-渠道活动批量派奖

- 接口声明：`POST /activities/channel-reward/gift/batch`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/operation/operation.py:7582` · `ChannelRewardGiftBatchResource`

### OPERATION-351 · 运营-活动-渠道活动批量校验用户

- 接口声明：`PATCH /activities/channel-reward/gift/batch`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7632` · `ChannelRewardGiftBatchResource`

### OPERATION-352 · 运营-活动-渠道活动批量审核

- 接口声明：`POST /activities/channel-reward/audit/batch`
- 输入字段：`ids`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/operation/operation.py:7706` · `ChannelRewardAuditBatchResource`

### OPERATION-353 · 运营-活动-渠道活动批量导出

- 接口声明：`GET /activities/channel-reward/export/batch`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7775` · `ChannelRewardExportBatchResource`

### OPERATION-354 · 运营-活动-交易送币活动统计信息

- 接口声明：`GET /activities/trade/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7863` · `TradeRankActivityResource`

### OPERATION-355 · 运营-活动-编辑交易送币活动

- 接口声明：`PUT /activities/trade/<int:id_>`
- 输入字段：`gift_asset`, `markets`, `exclude_markets`, `market_type`, `type`, `gift_rules`, `announce_url`, `least_trade_amount`, `max_split_reward_amount`, `gift_amount`, `start_time`, `end_time`, `titles`, `user_group_condition`, `cover`, `funding_source`, `broker_id`, `broker_logo`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:7899` · `TradeRankActivityResource`

### OPERATION-356 · 运营-活动-编辑交易送币状态

- 接口声明：`PATCH /activities/trade/<int:id_>`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8000` · `TradeRankActivityResource`

### OPERATION-357 · 运营-活动-交易送币活动-活动标题模板

- 接口声明：`GET /activities/trade/title/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8030` · `ActivityTradeTemplateResource`

### OPERATION-358 · 运营-活动-交易送币活动-导入活动标题模板

- 接口声明：`POST /activities/trade/title/template-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8046` · `ActivityTradeUploadResource`

### OPERATION-359 · 运营-活动-交易送币排行

- 接口声明：`GET /activities/trade-rank`
- 输入字段：`trade_activity_id`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8070` · `TradeRankResource`

### OPERATION-360 · 运营-活动-交易送币排行-添加/移除黑名单

- 接口声明：`PUT /activities/trade-rank`
- 输入字段：`trade_activity_id`, `user_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8106` · `TradeRankResource`

### OPERATION-361 · 活动-交易排名-参与用户

- 接口声明：`GET /activities/trade/users`
- 输入字段：`user_id`, `trade_activity_id`, `status`, `page`, `limit`, `channel`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8161` · `TradeRankActivityJoinUsersResource`

### OPERATION-362 · 活动-交易排名-模板下载

- 接口声明：`GET /activities/trade/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8546` · `TradeRankActivityTemplateResource`

### OPERATION-363 · 活动-交易排名-黑名单用户批量上传

- 接口声明：`POST /activities/trade/<int:trade_activity_id>/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8563` · `TradeRankActivityBatchResource`

### OPERATION-364 · 运营-活动-交易排名活动-批量修改用户状态

- 接口声明：`POST /activities/trade/<int:trade_activity_id>/batch-update-users`
- 输入字段：`status`, `ids`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8649` · `BatchUpdateUsersResource`

### OPERATION-365 · 运营-活动-交易送币派奖

- 接口声明：`POST /activities/trade/<int:id_>/gift`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8704` · `TradeSendGiftResource`

### OPERATION-366 · 运营-活动-交易送币排除清退用户

- 接口声明：`PATCH /activities/trade/<int:id_>/gift`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8745` · `TradeSendGiftResource`

### OPERATION-367 · 交易排名-活动统计

- 接口声明：`GET /activities/trade/statistics`
- 输入字段：`page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8789` · `TradeStatisticsResource`

### OPERATION-368 · 运营-推荐图片-推荐图片列表

- 接口声明：`GET /referral-pictures`
- 输入字段：`lang`, `version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8879` · `ReferralPictureListResource`

### OPERATION-369 · 运营-推荐图片-添加推荐图片

- 接口声明：`POST /referral-picture`
- 输入字段：`lang`, `file_ids`, `version`, `picture_type`, `start_at`, `end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:8922` · `ReferralPictureResource`

### OPERATION-370 · 运营-推荐图片-删除推荐图片

- 接口声明：`DELETE /referral-picture/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9000` · `ReferralPictureDetailResource`

### OPERATION-371 · 运营-App版本-列表

- 接口声明：`GET /app-versions`
- 输入字段：`platform`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9026` · `AppVersionsResource`

### OPERATION-372 · 运营-App版本--新建app版本

- 接口声明：`POST /app-versions`
- 输入字段：`platform`, `version`, `build`, `update_type`, `file_url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9069` · `AppVersionsResource`

### OPERATION-373 · 运营-App版本-是否支持APP内升级

- 接口声明：`PATCH /app-versions`
- 输入字段：`support_app_update`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9096` · `AppVersionsResource`

### OPERATION-374 · 运营-App版本-获取单条app版本

- 接口声明：`GET /app-versions/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9110` · `AppVersionResource`

### OPERATION-375 · 运营-App版本-修改app版本

- 接口声明：`PATCH /app-versions/<int:id_>`
- 输入字段：`version`, `build`, `update_type`, `file_url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9165` · `AppVersionResource`

### OPERATION-376 · 运营-App版本-删除app版本

- 接口声明：`DELETE /app-versions/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9202` · `AppVersionResource`

### OPERATION-377 · 运营-App版本-修改备注

- 接口声明：`PATCH /app-versions/<int:id_>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9222` · `AppVersionRemarkResource`

### OPERATION-378 · 运营-App版本-上传app文件

- 接口声明：`POST /app-versions/<int:id_>/file`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9255` · `AppVersionFileResource`

### OPERATION-379 · 运营-App版本-获取app版本描述

- 接口声明：`GET /app-versions/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9343` · `AppVersionsDescResource`

### OPERATION-380 · 运营-App版本-编辑app版本描述

- 接口声明：`PUT /app-versions/<int:id_>/langs/<lang>`
- 输入字段：`desc`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9353` · `AppVersionsDescResource`

### OPERATION-381 · 运营-弹窗管理

- 接口声明：`GET /popup-windows`
- 输入字段：`page`, `limit`, `status`, `platform`, `name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9589` · `PopupWindowsResource`

### OPERATION-382 · 运营-弹窗管理-新增弹窗

- 接口声明：`POST /popup-windows`
- 输入字段：`name`, `started_at`, `ended_at`, `platform`, `trigger_pages`, `frequency`, `filter_type`, `login_status`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `jump_page_enabled`, `jump_type`, `jump_id`, `pop_position`, `content_style`
- 显式控制：ns.use_kwargs(dict(name=fields.String(required=True), started_at=TimestampField(required=True), ended_at=TimestampField(required=True), platform=EnumField(model.Platform, required=
- 代码依据：`app/api/admin/operation/operation.py:9648` · `PopupWindowsResource`

### OPERATION-383 · 运营-弹窗管理-弹窗详情

- 接口声明：`GET /popup-windows/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9717` · `PopupWindowResource`

### OPERATION-384 · 运营-弹窗管理-编辑弹窗

- 接口声明：`PATCH /popup-windows/<int:id_>`
- 输入字段：`name`, `started_at`, `ended_at`, `platform`, `trigger_pages`, `frequency`, `filter_type`, `login_status`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `jump_page_enabled`, `jump_type`, `jump_id`, `content_style`, `pop_position`
- 显式控制：ns.use_kwargs(dict(name=fields.String(required=True), started_at=TimestampField(required=True), ended_at=TimestampField(required=True), platform=EnumField(model.Platform, required=
- 代码依据：`app/api/admin/operation/operation.py:9849` · `PopupWindowResource`

### OPERATION-385 · 运营-弹窗管理-删除弹窗

- 接口声明：`DELETE /popup-windows/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9911` · `PopupWindowResource`

### OPERATION-386 · 运营-弹窗管理-编辑排序

- 接口声明：`PUT /popup-windows/<int:id_>/sort`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9932` · `PopupWindowSortResource`

### OPERATION-387 · 运营-弹窗管理-停止活动

- 接口声明：`PUT /popup-windows/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9960` · `PopupWindowOfflineResource`

### OPERATION-388 · 运营-弹窗管理-编辑弹窗内容

- 接口声明：`PUT /popup-windows/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`, `url`, `images`, `content_style`, `pop_position`, `summary`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:9981` · `PopupWindowContentResource`

### OPERATION-389 · 运营-2FA重置管理

- 接口声明：`GET /2fa-reset`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10491` · `Reset2FAResource`

### OPERATION-390 · 运营-2FA重置管理-审核

- 接口声明：`PATCH /2fa-reset`
- 输入字段：`result`, `application_id`, `reason`, `is_custom_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10677` · `Reset2FAResource`

### OPERATION-391 · 运营-2FA重置管理-复审

- 接口声明：`PUT /2fa-reset`
- 输入字段：`result`, `application_id`, `reason`, `is_custom_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10716` · `Reset2FAResource`

### OPERATION-392 · 运营-2FA重置管理-导出

- 接口声明：`GET /2fa-reset/export`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10757` · `Reset2FAExportResource`

### OPERATION-393 · 运营-安全工具重置-更新当前编辑者

- 接口声明：`POST /2fa-reset/<int:id_>/auditors`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10788` · `Reset2faAuditorsResource`

### OPERATION-394 · 运营-2FA重置管理-批量分配审核人

- 接口声明：`POST /2fa-reset/auditors`
- 输入字段：`auditor_ids`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10810` · `Reset2FAAssignAuditorsResource`

### OPERATION-395 · 运营-2FA重置管理-批量解绑审核人

- 接口声明：`PATCH /2fa-reset/auditors`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10849` · `Reset2FAAssignAuditorsResource`

### OPERATION-396 · 运营-2FA重置管理-修改备注

- 接口声明：`PATCH /2fa-reset/<int:id_>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10885` · `Reset2FARemarkResource`

### OPERATION-397 · 运营-2FA重置管理-修改跳转链接

- 接口声明：`PATCH /2fa-reset/<int:id_>/jump_url`
- 输入字段：`jump_url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10919` · `Reset2FAJumpUrlResource`

### OPERATION-398 · 风控-安全工具-安全工具重置审核-变更记录

- 接口声明：`GET /2fa-reset/change-log`
- 输入字段：`start_time`, `end_time`, `user_id`, `admin_user_id`, `application_id`, `change_type`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:10952` · `SecurityResetApplyChangeLogResource`

### OPERATION-399 · 运营-2FA重置管理-详情页面

- 接口声明：`GET /2fa-reset/detail`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11102` · `Reset2FADetailResource`

### OPERATION-400 · 运营-2FA重置管理-自动审核记录

- 接口声明：`GET /2fa-reset/answer-history`
- 输入字段：`status`, `kyc_status`, `type`, `start_date`, `end_date`, `new_email`, `keyword`, `user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11308` · `Reset2FAQuestionHistoryResource`

### OPERATION-401 · 运营-2FA重置管理-新邮箱搜索

- 接口声明：`GET /2fa-reset/new-email-search`
- 输入字段：`email`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11437` · `Reset2FANewEmailSearchResource`

### OPERATION-402 · 运营-官方渠道校验-渠道列表

- 接口声明：`GET /verify-channel`
- 输入字段：`type`, `page`, `limit`, `user_id`, `name`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11500` · `VerifyChannelResource`

### OPERATION-403 · 运营-官方渠道校验-新增渠道

- 接口声明：`POST /verify-channel`
- 输入字段：`type`, `name`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11557` · `VerifyChannelResource`

### OPERATION-404 · 运营-官方渠道校验-批量上传

- 接口声明：`POST /verify-channel/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11595` · `VerifyChannelBatchUploadResource`

### OPERATION-405 · 运营-官方渠道校验-修改渠道

- 接口声明：`PUT /verify-channel/<int:id_>`
- 输入字段：`type`, `name`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11644` · `VerifyChannelDetailResource`

### OPERATION-406 · 运营-官方渠道校验-删除渠道

- 接口声明：`DELETE /verify-channel/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11678` · `VerifyChannelDetailResource`

### OPERATION-407 · 运营-查看Zendesk手动拉取记录

- 接口声明：`GET /zendesk-article-update-record`
- 输入字段：`last_id`, `first_id`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11699` · `ZendeskArticleUpdateRecordResource`

### OPERATION-408 · 运营-查看Zendesk手动拉取记录最近更新时间

- 接口声明：`GET /zendesk-article-update`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11720` · `ZendeskArticleUpdateResource`

### OPERATION-409 · 运营-手动拉取更新Zendesk文章

- 接口声明：`POST /zendesk-article-update`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11731` · `ZendeskArticleUpdateResource`

### OPERATION-410 · 安全工具变更记录

- 接口声明：`GET /security-tools-history`
- 输入字段：`search_keyword`, `history_email_or_mobile`, `change_type`, `start_date`, `end_date`, `page`, `limit`, `op_role`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11755` · `SecurityHistoryToolHistoryResource`

### OPERATION-411 · 用户特殊配置-变更记录

- 接口声明：`GET /sp-config-change-log`
- 输入字段：`search_keyword`, `config_type`, `op_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11842` · `UserSpConfigChangeLogResource`

### OPERATION-412 · 运营-App配置-头像配置-头像列表

- 接口声明：`GET /portrait-list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:11938` · `PortraitListResource`

### OPERATION-413 · 运营-App配置-头像配置-获取头像

- 接口声明：`GET /portrait`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12009` · `PortraitResource`

### OPERATION-414 · 运营-App配置-头像配置-删除头像

- 接口声明：`DELETE /portrait`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12021` · `PortraitResource`

### OPERATION-415 · 运营-App配置-头像配置-编辑头像

- 接口声明：`PUT /portrait`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12042` · `PortraitResource`

### OPERATION-416 · 运营-App配置-头像配置-创建头像

- 接口声明：`POST /portrait`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12072` · `PortraitResource`

### OPERATION-417 · 触达管理-通知栏-列表

- 接口声明：`GET /notification-bars`
- 输入字段：`name`, `platform`, `trigger_page`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12250` · `NotificationBars`

### OPERATION-418 · 运营-触达管理-通知栏-新建

- 接口声明：`POST /notification-bars`
- 输入字段：`name`, `platform`, `trigger_pages`, `begin_at`, `end_at`, `jump_page_enabled`, `jump_type`, `jump_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12334` · `NotificationBars`

### OPERATION-419 · 运营-通知栏-详情

- 接口声明：`GET /notification-bar/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12384` · `NotificationBarResource`

### OPERATION-420 · 运营-触达管理-通知栏-编辑

- 接口声明：`PUT /notification-bar/<int:id_>`
- 输入字段：`name`, `platform`, `trigger_pages`, `begin_at`, `end_at`, `jump_page_enabled`, `jump_type`, `jump_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12420` · `NotificationBarResource`

### OPERATION-421 · 运营-触达管理-通知栏-删除

- 接口声明：`DELETE /notification-bar/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12478` · `NotificationBarResource`

### OPERATION-422 · 运营-触达管理-通知栏-提交审核

- 接口声明：`PATCH /notification-bar/<int:id_>/created`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12505` · `NotificationBarCreated`

### OPERATION-423 · 运营-触达管理-通知栏-审核

- 接口声明：`PATCH /notification-bar/<int:id_>/audit`
- 输入字段：`status`, `auditor_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12538` · `NotificationBarAudit`

### OPERATION-424 · 运营-触达管理-通知栏-通知中提前结束

- 接口声明：`PATCH /notification-bar/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12590` · `NotificationBarOffline`

### OPERATION-425 · 运营-触达管理-通知栏-时间范围重复数量

- 接口声明：`GET /notification-bar/duplicates`
- 输入字段：`id`, `platform`, `trigger_pages`, `begin_at`, `end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12623` · `NotificationBarDuplicates`

### OPERATION-426 · 运营-通知栏-获取通知栏内容

- 接口声明：`GET /notification-bar/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12679` · `NotificationBarContentResource`

### OPERATION-427 · 运营-通知栏-编辑内容

- 接口声明：`PUT /notification-bar/<int:id_>/langs/<lang>`
- 输入字段：`title`, `summary`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12694` · `NotificationBarContentResource`

### OPERATION-428 · 运营管理-模板列表

- 接口声明：`GET /templates`
- 输入字段：`title`, `enabled`, `start_time`, `end_time`, `business`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12753` · `OperationTemplates`

### OPERATION-429 · 运营管理-模板新建

- 接口声明：`POST /templates`
- 输入字段：`business`, `title`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12805` · `OperationTemplates`

### OPERATION-430 · 运营管理-模板启用开关

- 接口声明：`PUT /template/<int:id_>/on_off`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12838` · `OperationTemplateOnOffResource`

### OPERATION-431 · 运营管理-模板详情

- 接口声明：`GET /template/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12864` · `OperationTemplateResource`

### OPERATION-432 · 运营管理-模板编辑

- 接口声明：`PUT /template/<int:id_>`
- 输入字段：`title`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12879` · `OperationTemplateResource`

### OPERATION-433 · 运营管理-模板删除

- 接口声明：`DELETE /template/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12902` · `OperationTemplateResource`

### OPERATION-434 · 运营管理-模板内容

- 接口声明：`GET /template-content/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12930` · `OperationTemplateContentResource`

### OPERATION-435 · 运营管理-模板内容编辑

- 接口声明：`PUT /template-content/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`, `summary`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:12948` · `OperationTemplateContentResource`

### OPERATION-436 · 运营-视频文件列表

- 接口声明：`GET /videos`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13013` · `VideosResource`

### OPERATION-437 · 运营-主副标题形式-下载模板

- 接口声明：`GET /title-subtitle/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13065` · `TitleSubtitleTemplateResource`

### OPERATION-438 · 运营-主副标题形式-上传文件

- 接口声明：`POST /title-subtitle/upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13082` · `TitleSubtitleUploadResource`

### OPERATION-439 · 运营-主标题形式-下载模板

- 接口声明：`GET /title/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13113` · `TitleTemplateResource`

### OPERATION-440 · 运营-主标题形式-上传文件

- 接口声明：`POST /title/upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13130` · `TitleUploadResource`

### OPERATION-441 · 风控-自助解冻管理

- 接口声明：`GET /unfreeze`
- 输入字段：`status`, `identity_type`, `balance_choice`, `kyc_status`, `pass_type`, `start_date`, `end_date`, `user_id`, `keyword`, `page`, `limit`, `order`, `order_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13147` · `UnfreezeUserListResource`

### OPERATION-442 · 风控-自助解冻管理-初核通过

- 接口声明：`PATCH /unfreeze/<int:id_>/audit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13249` · `UnfreezeUserAuditResource`

### OPERATION-443 · 风控-自助解冻管理-复核通过

- 接口声明：`PATCH /unfreeze/<int:id_>/pass`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13285` · `UnfreezeUserPassResource`

### OPERATION-444 · 风控-自助解冻管理-拒绝

- 接口声明：`PATCH /unfreeze/<int:id_>/reject`
- 输入字段：`reason`, `is_custom_reason`, `custom_reject_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13319` · `UnfreezeUserRejectResource`

### OPERATION-445 · 风控-自助解冻管理-修改备注

- 接口声明：`PATCH /unfreeze/<int:id_>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13384` · `UnfreezeUserRemarkResource`

### OPERATION-446 · 风控-自助解冻管理-详情页面

- 接口声明：`GET /unfreeze/detail`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13483` · `UnfreezeUserDetailResource`

### OPERATION-447 · 风控-自助解冻-变更记录

- 接口声明：`GET /unfreeze-log`
- 输入字段：`search_keyword`, `start_date`, `end_date`, `operate_type`, `op_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13619` · `UnfreezeLogResource`

### OPERATION-448 · 运营-KYC-个人高级认证列表

- 接口声明：`GET /kyc-pro`
- 输入字段：`country`, `status`, `audit_type`, `flow`, `user_id`, `platform`, `start_at`, `end_at`, `start_id`, `auditor_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13961` · `KycVerificationProResource`

### OPERATION-449 · 运营-KYC-个人高级认证下载

- 接口声明：`GET /kyc-pro/download`
- 输入字段：`country`, `status`, `user_id`, `start_at`, `end_at`, `flow`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:13986` · `KycVerificationProDownloadResource`

### OPERATION-450 · 运营-高级KYC-更新当前编辑者

- 接口声明：`POST /kyc-pro/<int:id_>/auditors`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14007` · `KycProVerificationAuditorsResource`

### OPERATION-451 · 风控-KYC-个人高级认证-批量分配审核人

- 接口声明：`POST /kyc-pro/auditors`
- 输入字段：`auditor_ids`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14029` · `KycVerificationProAssignAuditorsResource`

### OPERATION-452 · 风控-KYC-个人高级认证-批量解绑审核人

- 接口声明：`PATCH /kyc-pro/auditors`
- 输入字段：`ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14065` · `KycVerificationProAssignAuditorsResource`

### OPERATION-453 · 运营-KYC-个人高级认证-配置查询

- 接口声明：`GET /kyc-pro/settings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14098` · `KycVerificationProSettingsResource`

### OPERATION-454 · 运营-KYC-个人高级认证-配置修改

- 接口声明：`PATCH /kyc-pro/settings`
- 输入字段：`third_max_count`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14105` · `KycVerificationProSettingsResource`

### OPERATION-455 · kyc高级认证-认证详情

- 接口声明：`GET /kyc-pro/<int:kyc_pro_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14258` · `KycVerificationProDetailResource`

### OPERATION-456 · kyc高级认证-编辑审核

- 接口声明：`PATCH /kyc-pro/<int:kyc_pro_id>`
- 输入字段：`status`, `rejection_reason`, `custom_rejection_reason`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14267` · `KycVerificationProDetailResource`

### OPERATION-457 · kyc高级认证-修改备注

- 接口声明：`PUT /kyc-pro/<int:kyc_pro_id>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14349` · `KycVerificationProDetailResource`

### OPERATION-458 · 运营-KYC-高级认证第三方审核记录

- 接口声明：`GET /kyc-pro/history`
- 输入字段：`status`, `reason`, `service_type`, `transaction_id`, `user`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14375` · `KYCProHistoryListResource`

### OPERATION-459 · 生物识别认证-认证记录

- 接口声明：`GET /liveness-check/history`
- 输入字段：`status`, `business`, `audit_type`, `transaction_id`, `start_id`, `auditor_id`, `user`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14462` · `LivenessCheckHistoryResource`

### OPERATION-460 · 生物识别认证-发送认证邮件

- 接口声明：`POST /liveness-check/history`
- 输入字段：`user_id`, `email`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14599` · `LivenessCheckHistoryResource`

### OPERATION-461 · 风控-生物识别认证-下载模板

- 接口声明：`GET /liveness-check/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14644` · `LivenessCheckTemplateResource`

### OPERATION-462 · 生物识别认证-批量发送认证邮件

- 接口声明：`POST /liveness-check/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14653` · `LivenessCheckTemplateResource`

### OPERATION-463 · 生物识别认证-认证详情

- 接口声明：`GET /liveness-check/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14804` · `LivenessCheckDetailResource`

### OPERATION-464 · 生物识别验证-审核

- 接口声明：`PUT /liveness-check/<int:id_>`
- 输入字段：`admin_reason`, `is_custom_reason`, `custom_admin_reason`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14812` · `LivenessCheckDetailResource`

### OPERATION-465 · 生物识别认证-修改备注

- 接口声明：`PATCH /liveness-check/<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14862` · `LivenessCheckDetailResource`

### OPERATION-466 · 风控-KYC-生物识别验证-批量分配审核人

- 接口声明：`POST /liveness-check/auditors`
- 输入字段：`auditor_ids`, `ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/operation.py:14887` · `LivenessCheckAssignAuditorsResource`

### OPERATION-467 · 运营-Banner-获取banners列表

- 接口声明：`GET /banners`
- 输入字段：`status`, `platform`, `name`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:72` · `BannersResource`

### OPERATION-468 · 运营-Banner-创建banners

- 接口声明：`POST /banners`
- 输入字段：`name`, `affect_homepage`, `affect_calendar`, `started_at`, `ended_at`, `platform`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:127` · `BannersResource`

### OPERATION-469 · 运营-Banner-获取单条banner

- 接口声明：`GET /banners/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:196` · `BannerContentResource`

### OPERATION-470 · 运营-Banner-编辑banner

- 接口声明：`PATCH /banners/<int:id_>`
- 输入字段：`name`, `affect_homepage`, `affect_calendar`, `started_at`, `ended_at`, `platform`, `url`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:220` · `BannerContentResource`

### OPERATION-471 · 运营-Banner-banner拖拽排序

- 接口声明：`POST /banners/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:295` · `BannerSortResource`

### OPERATION-472 · 运营-Banner-banners上移

- 接口声明：`POST /banners/<int:id_>/sort_id`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:318` · `BannerSortIDResource`

### OPERATION-473 · 运营-Banner-获取单条banner内容

- 接口声明：`GET /banners/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:352` · `BannerContentLangResource`

### OPERATION-474 · 运营-Banner-编辑banner内容

- 接口声明：`POST /banners/<int:id_>/langs/<lang>/img`
- 输入字段：`file_key`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:385` · `BannerContentImageResource`

### OPERATION-475 · 运营-Banner-删除banner

- 接口声明：`DELETE /banners/<int:id_>/langs/<lang>/img`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:484` · `BannerContentImageResource`

### OPERATION-476 · 运营-APP-新快捷入口-跳转列表

- 接口声明：`GET /new-app-entrances/jump-list`
- 输入字段：`jump_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:506` · `NewAppEntranceJumpListResource`

### OPERATION-477 · 运营-APP-新快捷入口-添加跳转

- 接口声明：`POST /new-app-entrances/jump-list`
- 输入字段：`remark`, `jump_type`, `jump_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:533` · `NewAppEntranceJumpListResource`

### OPERATION-478 · 运营-APP-新快捷入口-编辑跳转

- 接口声明：`PUT /new-app-entrances/jump-list`
- 输入字段：`id`, `remark`, `jump_type`, `jump_data`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:558` · `NewAppEntranceJumpListResource`

### OPERATION-479 · 运营-APP-新快捷入口-删除跳转

- 接口声明：`DELETE /new-app-entrances/jump-list/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:592` · `NewAppEntranceJumpResource`

### OPERATION-480 · 运营-APP-新版快捷入口列表

- 接口声明：`GET /new-app-entrances`
- 输入字段：`entrance_type`, `platform`, `version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:709` · `NewAppEntranceListResource`

### OPERATION-481 · 运营-APP-新建新版快捷入口

- 接口声明：`POST /new-app-entrances`
- 输入字段：`api_field`, `translations`, `jump_type`, `jump_id`, `light_pic_id`, `dark_pic_id`, `status`, `entrance_type`, `platform`, `version`, `is_default`, `is_first`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:801` · `NewAppEntranceListResource`

### OPERATION-482 · 运营-APP-修改新版快捷入口

- 接口声明：`PUT /new-app-entrance/<int:id_>`
- 输入字段：`api_field`, `translations`, `jump_type`, `jump_id`, `light_pic_id`, `dark_pic_id`, `status`, `entrance_type`, `is_default`, `is_first`, `platform`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:882` · `NewAppEntranceResource`

### OPERATION-483 · 运营-APP-删除新版快捷入口

- 接口声明：`DELETE /new-app-entrance/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:973` · `NewAppEntranceResource`

### OPERATION-484 · 运营-金刚区-拖拽排序

- 接口声明：`POST /new-app-entrance/sorts`
- 输入字段：`old_data`, `old_index`, `new_index`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1008` · `AppEntranceDragSortsResource`

### OPERATION-485 · 运营-APP-修改新版快捷入口排序

- 接口声明：`PUT /new-app-entrance-order/<int:id_>`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1052` · `AppEntranceOrderResource`

### OPERATION-486 · 运营-APP-活动宣传/功能介绍列表

- 接口声明：`GET /app-activate`
- 输入字段：`display_name`, `begin_at`, `end_at`, `activate_status`, `activate_type`, `platform`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1170` · `AppActivateListResource`

### OPERATION-487 · 运营-APP-新建活动宣传/功能介绍入口

- 接口声明：`POST /app-activate`
- 输入字段：`begin_at`, `end_at`, `jump_type`, `jump_id`, `light_pic_id`, `dark_pic_id`, `platform`, `activate_type`, `translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1208` · `AppActivateListResource`

### OPERATION-488 · 运营-APP-新建活动宣传/功能介绍详情

- 接口声明：`GET /app-activate/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1285` · `AppActivateResource`

### OPERATION-489 · 运营-APP-修改活动宣传/功能介绍详情

- 接口声明：`PUT /app-activate/<int:id_>`
- 输入字段：`begin_at`, `end_at`, `jump_type`, `jump_id`, `light_pic_id`, `dark_pic_id`, `translations`, `activate_type`, `platform`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1309` · `AppActivateResource`

### OPERATION-490 · 运营-APP-删除活动宣传/功能介绍

- 接口声明：`DELETE /app-activate/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1356` · `AppActivateResource`

### OPERATION-491 · 运营-APP-下架活动宣传/功能介绍

- 接口声明：`PATCH /app-activate/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1375` · `AppActivateOfflineResource`

### OPERATION-492 · 运营-APP-修改活动宣传/功能介绍排序

- 接口声明：`PUT /app-activate-order/<int:id_>`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1411` · `AppActivateOrderResource`

### OPERATION-493 · 运营-APP-功能介绍列表(新)

- 接口声明：`GET /app-activate-new`
- 输入字段：`display_name`, `begin_at`, `end_at`, `activate_status`, `activate_type`, `platform`, `version`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1486` · `NewAppActivateListResource`

### OPERATION-494 · 运营-APP-功能介绍详情(新)

- 接口声明：`GET /app-activate-new/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1555` · `NewAppActivateResource`

### OPERATION-495 · 运营-APP-新建/编辑功能介绍入口(新)

- 接口声明：`PUT /app-activate-new/<int:id_>`
- 输入字段：`display_name`, `platform`, `activate_type`, `begin_at`, `end_at`, `jump_type`, `jump_id`, `content_style`, `light_pic_id`, `dark_pic_id`, `rtl_light_pic_id`, `rtl_dark_pic_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1588` · `NewAppActivateResource`

### OPERATION-496 · 运营-APP-删除功能介绍(新)

- 接口声明：`DELETE /app-activate-new/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1651` · `NewAppActivateResource`

### OPERATION-497 · 运营-APP-下架功能介绍(新)

- 接口声明：`PATCH /app-activate-new/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1669` · `NewAppActivateOfflineResource`

### OPERATION-498 · 运营-APP-修改功能介绍排序(新)

- 接口声明：`PUT /app-activate-new-order/<int:id_>`
- 输入字段：`up`, `version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1705` · `NewAppActivateOrderResource`

### OPERATION-499 · 运营-APP-获取功能介绍内容(新)

- 接口声明：`GET /app-activate-new/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1749` · `NewAppActivateContentResource`

### OPERATION-500 · 运营-APP-编辑功能介绍内容(新)

- 接口声明：`PUT /app-activate-new/<int:id_>/langs/<lang>`
- 输入字段：`title`, `sub_title`, `light_pic_id`, `dark_pic_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1776` · `NewAppActivateContentResource`

### OPERATION-501 · 运营-APP-活动介绍详情 v3

- 接口声明：`GET /app-activate-v3/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1837` · `NewAppActivateV3Resource`

### OPERATION-502 · 运营-APP-新建/编辑活动介绍入口 v3

- 接口声明：`PUT /app-activate-v3/<int:id_>`
- 输入字段：`display_name`, `platform`, `begin_at`, `end_at`, `jump_type`, `jump_id`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:1877` · `NewAppActivateV3Resource`

### OPERATION-503 · 运营-Web配置-新手专题页Banner-列表

- 接口声明：`GET /newbie-hub-banners`
- 输入字段：`display_name`, `begin_at`, `end_at`, `activate_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2072` · `NewbieHubBannerListResource`

### OPERATION-504 · 运营-Web配置-新手专题页Banner-详情

- 接口声明：`GET /newbie-hub-banners/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2113` · `NewbieHubBannerResource`

### OPERATION-505 · 运营-Web配置-新手专题页Banner-新建/编辑

- 接口声明：`PUT /newbie-hub-banners/<int:id_>`
- 输入字段：`display_name`, `begin_at`, `end_at`, `jump_type`, `jump_id`, `content_style`, `light_pic_id`, `dark_pic_id`, `rtl_light_pic_id`, `rtl_dark_pic_id`, `h5_light_pic_id`, `h5_dark_pic_id`, `h5_rtl_light_pic_id`, `h5_rtl_dark_pic_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2129` · `NewbieHubBannerResource`

### OPERATION-506 · 运营-Web配置-新手专题页Banner-删除

- 接口声明：`DELETE /newbie-hub-banners/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2177` · `NewbieHubBannerResource`

### OPERATION-507 · 运营-Web配置-新手专题页Banner-下架

- 接口声明：`PATCH /newbie-hub-banners/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2195` · `NewbieHubBannerOfflineResource`

### OPERATION-508 · 运营-Web配置-新手专题页Banner-排序

- 接口声明：`PUT /newbie-hub-banners/<int:id_>/sort`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2213` · `NewbieHubBannerSortResource`

### OPERATION-509 · 运营-Web配置-新手专题页Banner-获取多语言内容

- 接口声明：`GET /newbie-hub-banners/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2246` · `NewbieHubBannerContentResource`

### OPERATION-510 · 运营-Web配置-新手专题页Banner-编辑多语言内容

- 接口声明：`PUT /newbie-hub-banners/<int:id_>/langs/<lang>`
- 输入字段：`title`, `sub_title`, `light_title_color`, `dark_title_color`, `light_pic_id`, `dark_pic_id`, `h5_light_pic_id`, `h5_dark_pic_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2281` · `NewbieHubBannerContentResource`

### OPERATION-511 · 运营-APP-获取活动介绍插画

- 接口声明：`GET /app-activate-pic`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2333` · `NewAppActivatePicResource`

### OPERATION-512 · 运营-APP-添加/修改活动介绍插画

- 接口声明：`PUT /app-activate-pic`
- 输入字段：`pic_file_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2347` · `NewAppActivatePicResource`

### OPERATION-513 · 运营-APP-启动页列表

- 接口声明：`GET /start-page`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2361` · `StartPageResource`

### OPERATION-514 · 运营-APP-启动页创建

- 接口声明：`POST /start-page`
- 输入字段：`name`, `show_time`, `return_url`, `start_at`, `end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2377` · `StartPageResource`

### OPERATION-515 · 运营-APP-获取启动页详情

- 接口声明：`GET /start-page/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2417` · `StartPageInfoResource`

### OPERATION-516 · 运营-APP-修改启动页

- 接口声明：`PUT /start-page/<int:id_>`
- 输入字段：`name`, `show_time`, `return_url`, `start_at`, `end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2437` · `StartPageInfoResource`

### OPERATION-517 · 运营-APP-删除启动页

- 接口声明：`DELETE /start-page/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2469` · `StartPageInfoResource`

### OPERATION-518 · 运营-APP-编辑启动页内容

- 接口声明：`POST /start-page/<int:id_>/langs/<lang>/img`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2492` · `StartPageImageResource`

### OPERATION-519 · 运营-APP-删除启动页内容

- 接口声明：`DELETE /start-page/<int:id_>/langs/<lang>/img`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2543` · `StartPageImageResource`

### OPERATION-520 · 运营-启动页管理

- 接口声明：`GET /app-start-page`
- 输入字段：`page`, `limit`, `status`, `platform`, `name`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2621` · `AppStartPageResource`

### OPERATION-521 · 运营-启动页管理-新增启动页

- 接口声明：`POST /app-start-page`
- 输入字段：`name`, `return_url`, `show_time`, `started_at`, `ended_at`, `platform`, `frequency`, `filter_type`, `groups`, `whitelist_enabled`, `user_whitelist`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2671` · `AppStartPageResource`

### OPERATION-522 · 运营-启动页管理-启动页详情

- 接口声明：`GET /app-start-page/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2731` · `AppStartPageDetailResource`

### OPERATION-523 · 运营-启动页管理-编辑启动页

- 接口声明：`PATCH /app-start-page/<int:id_>`
- 输入字段：`name`, `started_at`, `ended_at`, `return_url`, `show_time`, `platform`, `frequency`, `filter_type`, `groups`, `whitelist_enabled`, `user_whitelist`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2786` · `AppStartPageDetailResource`

### OPERATION-524 · 运营-启动页管理-删除启动页

- 接口声明：`DELETE /app-start-page/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2839` · `AppStartPageDetailResource`

### OPERATION-525 · 运营-启动页管理-编辑排序

- 接口声明：`PUT /app-start-page/<int:id_>/sort`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2860` · `APpStartPageSortResource`

### OPERATION-526 · 运营-启动页管理-停止活动

- 接口声明：`PUT /app-start-page/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2888` · `APpStartPageOfflineResource`

### OPERATION-527 · 运营-启动页管理-编辑启动页内容

- 接口声明：`PUT /app-start-page/<int:id_>/langs/<lang>`
- 输入字段：`images`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2909` · `AppStartPageContentResource`

### OPERATION-528 · 运营-市场配置-登录页市场列表

- 接口声明：`GET /login-page-markets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2967` · `LoginPageMarketListResource`

### OPERATION-529 · 运营-市场配置-新建登录页市场

- 接口声明：`POST /login-page-markets`
- 输入字段：`market`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2973` · `LoginPageMarketListResource`

### OPERATION-530 · 运营-市场配置-修改登录页市场

- 接口声明：`PATCH /login-page-market/<int:id_>`
- 输入字段：`market`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:2995` · `LoginPageMarketResource`

### OPERATION-531 · 运营-市场配置-删除登录页市场

- 接口声明：`DELETE /login-page-market/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3014` · `LoginPageMarketResource`

### OPERATION-532 · 运营-市场配置-修改登录页市场排序

- 接口声明：`PUT /login-page-market-order/<int:id_>`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3032` · `LoginPageMarketOrderResource`

### OPERATION-533 · 获取运营-运营管理-WEB配置-首页-新手指引记录列表

- 接口声明：`GET /primary-page/newer-guide`
- 输入字段：`lang`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3056` · `NewerGuideListResource`

### OPERATION-534 · 创建运营-运营管理-WEB配置-首页-新手指引

- 接口声明：`POST /primary-page/newer-guide`
- 输入字段：`lang`, `cover`, `title`, `content_type`, `url`, `category`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3072` · `NewerGuideListResource`

### OPERATION-535 · 获取运营-运营管理-WEB配置-首页-新手指引记录

- 接口声明：`GET /primary-page/newer-guide/<int:item_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3108` · `NewerGuideDetailResource`

### OPERATION-536 · 更新运营-运营管理-WEB配置-首页-新手指引记录

- 接口声明：`PUT /primary-page/newer-guide/<int:item_id>`
- 输入字段：`lang`, `cover`, `title`, `content_type`, `url`, `category`, `sort_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3116` · `NewerGuideDetailResource`

### OPERATION-537 · 删除运营-运营管理-WEB配置-首页-新手指引记录

- 接口声明：`DELETE /primary-page/newer-guide/<int:item_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3154` · `NewerGuideDetailResource`

### OPERATION-538 · 运营-运营管理-WEB配置-首页-新手指引排序

- 接口声明：`PUT /newer-guide-reorder/<int:id_>`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3186` · `NewerGuideOrderResource`

### OPERATION-539 · 运营管理-web配置-登录页、注册页-插画列表

- 接口声明：`GET /insets`
- 输入字段：`page_type`, `start_time`, `end_time`, `name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3249` · `PageInsetsResource`

### OPERATION-540 · 运营管理-web配置-登录页、注册页-创建插画

- 接口声明：`POST /insets`
- 输入字段：`name`, `begin_at`, `end_at`, `page_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3304` · `PageInsetsResource`

### OPERATION-541 · 运营管理-web配置-登录页、注册页-插画详情

- 接口声明：`GET /insets/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3359` · `PageInsetDetailResource`

### OPERATION-542 · 运营管理-web配置-登录页、注册页-编辑插画

- 接口声明：`PATCH /insets/<int:id_>`
- 输入字段：`name`, `begin_at`, `end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3381` · `PageInsetDetailResource`

### OPERATION-543 · 运营管理-web配置-登录页、注册页-删除、下架

- 接口声明：`DELETE /insets/<int:id_>`
- 输入字段：`is_offline`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3414` · `PageInsetDetailResource`

### OPERATION-544 · 运营管理-web配置-登录页、注册页-获取插画内容

- 接口声明：`GET /insets/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3455` · `PageInsetContentLangResource`

### OPERATION-545 · 运营管理-web配置-登录页、注册页-编辑插画内容

- 接口声明：`POST /insets/<int:id_>/langs/<lang>`
- 输入字段：`light_pic_id`, `dark_pic_id`, `light_background_color`, `dark_background_color`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3470` · `PageInsetContentLangResource`

### OPERATION-546 · 运营管理-web配置-登录页、注册页-删除插画内容

- 接口声明：`DELETE /insets/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3520` · `PageInsetContentLangResource`

### OPERATION-547 · 运营-运营管理-SNS 配置列表

- 接口声明：`GET /sns-config`
- 输入字段：`lang`, `media`, `display_position`, `business`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3547` · `SNSConfigsResource`

### OPERATION-548 · 运营-运营管理-编辑/新建 SNS 配置

- 接口声明：`PATCH /sns-config/<int:id_>`
- 输入字段：`business`, `media`, `display_positions`, `lang`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3609` · `SNSConfigResource`

### OPERATION-549 · 运营-运营管理-删除 SNS 配置

- 接口声明：`DELETE /sns-config/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3676` · `SNSConfigResource`

### OPERATION-550 · 运营-通用运营配置-Footer Learn 配置列表

- 接口声明：`GET /learn-configs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3699` · `LearnConfigsResource`

### OPERATION-551 · 运营-通用运营配置-Footer Learn 排序

- 接口声明：`PUT /learn-configs/<int:id_>/sort`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3724` · `LearnConfigSortResource`

### OPERATION-552 · 运营-通用运营配置-Footer Learn 修改状态

- 接口声明：`PUT /learn-configs/<int:id_>/status`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3771` · `LearnConfigStatusResource`

### OPERATION-553 · 运营-通用运营配置-Footer Learn 详情

- 接口声明：`GET /learn-configs/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3798` · `LearnConfigResource`

### OPERATION-554 · 运营-通用运营配置-Footer Learn 修改

- 接口声明：`PATCH /learn-configs/<int:id_>`
- 输入字段：`title_i18n`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3811` · `LearnConfigResource`

### OPERATION-555 · 运营-通用运营配置-Footer Learn 删除

- 接口声明：`DELETE /learn-configs/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3856` · `LearnConfigResource`

### OPERATION-556 · 运营-WEB配置-合约交易页-活动专区活动列表

- 接口声明：`GET /perpetual-activity`
- 输入字段：`display_name`, `begin_at`, `end_at`, `activate_status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:3936` · `PerpetualActivityListResource`

### OPERATION-557 · 运营-WEB配置-合约交易页-新建活动

- 接口声明：`POST /perpetual-activity`
- 输入字段：`begin_at`, `end_at`, `jump_id`, `light_pic_id`, `dark_pic_id`, `translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4005` · `PerpetualActivityListResource`

### OPERATION-558 · 运营-WEB配置-合约交易页-活动介绍详情

- 接口声明：`GET /perpetual-activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4052` · `PerpetualActivityResource`

### OPERATION-559 · 运营-WEB配置-合约交易页-修改活动

- 接口声明：`PUT /perpetual-activity/<int:id_>`
- 输入字段：`begin_at`, `end_at`, `jump_id`, `light_pic_id`, `dark_pic_id`, `translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4079` · `PerpetualActivityResource`

### OPERATION-560 · 运营-WEB配置-合约交易页-删除活动

- 接口声明：`DELETE /perpetual-activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4175` · `PerpetualActivityResource`

### OPERATION-561 · 运营-WEB配置-合约交易页-下架活动

- 接口声明：`PATCH /perpetual-activity/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4195` · `PerpetualActivityOfflineResource`

### OPERATION-562 · 运营管理-app配置-动效飘落列表

- 接口声明：`GET /dynamic-falling`
- 输入字段：`op_platform`, `name`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4267` · `DynamicFallingResource`

### OPERATION-563 · 运营管理-app配置-动效飘落创建

- 接口声明：`POST /dynamic-falling`
- 输入字段：`name`, `platform`, `type`, `light_file_id`, `light_file_name`, `dark_file_id`, `dark_file_name`, `begin_at`, `end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4340` · `DynamicFallingResource`

### OPERATION-564 · 运营管理-app配置-动效飘落编辑

- 接口声明：`PUT /dynamic-falling/<int:id_>`
- 输入字段：`name`, `platform`, `type`, `light_file_id`, `light_file_name`, `dark_file_id`, `dark_file_name`, `begin_at`, `end_at`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4383` · `DynamicFallingDetailResource`

### OPERATION-565 · 运营管理-app配置-动效飘落删除

- 接口声明：`DELETE /dynamic-falling/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4422` · `DynamicFallingDetailResource`

### OPERATION-566 · 运营管理-app/web配置-动效上传

- 接口声明：`POST /dynamic-falling/upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4442` · `DynamicFallingUploadResource`

### OPERATION-567 · 运营>运营管理>WEB配置>站内功能曝光标识 

- 接口声明：`GET /exposure/activity/settings`
- 输入字段：`active_status`, `page`, `limit`, `id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4512` · `ExposureActivitySettingsResource`

### OPERATION-568 · 运营>运营管理>WEB配置>添加站内功能曝光标识 

- 接口声明：`POST /exposure/activity/settings`
- 输入字段：`name`, `start_time`, `end_time`, `menu`, `submenu`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4578` · `ExposureActivitySettingsResource`

### OPERATION-569 · 运营>运营管理>WEB配置>编辑站内功能曝光标识 

- 接口声明：`PUT /exposure/activity/settings`
- 输入字段：`id`, `name`, `start_time`, `end_time`, `menu`, `submenu`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4610` · `ExposureActivitySettingsResource`

### OPERATION-570 · 运营>运营管理>WEB配置>删除站内功能曝光标识 

- 接口声明：`PATCH /exposure/activity/settings`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4647` · `ExposureActivitySettingsResource`

### OPERATION-571 · 运营>运营管理>WEB配置>站内功能曝光标识详情

- 接口声明：`GET /exposure/activity/settings/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/page.py:4675` · `ExposureDetailResource`

### OPERATION-572 · 运营-触达管理-APP推送

- 接口声明：`GET /pushes`
- 输入字段：`id`, `name`, `status`, `push_type`, `start_time`, `end_time`, `keyword`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:158` · `AppPushesResource`

### OPERATION-573 · 运营-触达管理-APP推送-创建

- 接口声明：`POST /pushes`
- 输入字段：`name`, `push_type`, `push_time`, `remark`, `user_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `jump_id`, `ttl`, `market_association_enabled`, `market_asset`, `market_condition`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:230` · `AppPushesResource`

### OPERATION-574 · 运营-触达管理-APP推送详情

- 接口声明：`GET /pushes/<int:id_>`
- 输入字段：`is_export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:316` · `AppPushResource`

### OPERATION-575 · 运营-触达管理-APP推送-编辑

- 接口声明：`PATCH /pushes/<int:id_>`
- 输入字段：`name`, `push_type`, `push_time`, `remark`, `user_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `jump_id`, `ttl`, `market_association_enabled`, `market_asset`, `market_condition`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:357` · `AppPushResource`

### OPERATION-576 · 运营-触达管理-APP推送-删除

- 接口声明：`DELETE /pushes/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:432` · `AppPushResource`

### OPERATION-577 · 运营-触达管理-APP推送用户下载

- 接口声明：`GET /pushes/<int:id_>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:461` · `AppPushUserResource`

### OPERATION-578 · 运营-触达管理-APP推送-提交审核

- 接口声明：`PATCH /pushes/<int:id_>/created`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:490` · `AppPushDraftResource`

### OPERATION-579 · 运营-触达管理-APP推送-暂停推送

- 接口声明：`PATCH /pushes/<int:id_>/suspended`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:517` · `AppPushSuspendResource`

### OPERATION-580 · 运营-触达管理-APP推送-审核

- 接口声明：`PATCH /pushes/<int:id_>/audit`
- 输入字段：`status`, `auditor_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:551` · `AppPushAuditResource`

### OPERATION-581 · 运营-APP推送-获取APP推送内容

- 接口声明：`GET /pushes/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:594` · `AppPushContentResource`

### OPERATION-582 · 运营-APP推送-编辑APP推送内容

- 接口声明：`PUT /pushes/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:610` · `AppPushContentResource`

### OPERATION-583 · APP测试-检查

- 接口声明：`GET /pushes/<int:id_>/test`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:659` · `AppPushContentTestResource`

### OPERATION-584 · 运营-触达管理-内容APP测试

- 接口声明：`POST /pushes/<int:id_>/test`
- 输入字段：`accounts`, `push_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:665` · `AppPushContentTestResource`

### OPERATION-585 · 运营-APP推送-导入用户

- 接口声明：`POST /pushes/imports`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:788` · `AppPushImportsResource`

### OPERATION-586 · 运营-APP推送-自动触达

- 接口声明：`GET /auto-pushes`
- 输入字段：`type`, `start_time`, `end_time`, `key`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:829` · `AppAutoPushHistoryResource`

### OPERATION-587 · 运营-触达管理-站内信推送列表

- 接口声明：`GET /messages`
- 输入字段：`name`, `channel`, `status`, `start_time`, `end_time`, `creator`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:884` · `MessagePushListResource`

### OPERATION-588 · 运营-触达管理-站内信推送-创建

- 接口声明：`POST /messages`
- 输入字段：`name`, `channel`, `display_type`, `push_time`, `jump_page_enabled`, `web_jump_type`, `web_jump_id`, `android_jump_type`, `android_jump_id`, `remark`, `status`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:951` · `MessagePushListResource`

### OPERATION-589 · 运营-触达管理-站内信推送-详情

- 接口声明：`GET /messages/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1007` · `MessagePushDetailResource`

### OPERATION-590 · 运营-触达管理-站内信推送-编辑

- 接口声明：`PATCH /messages/<int:id_>`
- 输入字段：`name`, `channel`, `display_type`, `push_time`, `jump_page_enabled`, `web_jump_type`, `web_jump_id`, `android_jump_type`, `android_jump_id`, `remark`, `status`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1063` · `MessagePushDetailResource`

### OPERATION-591 · 运营-触达管理-站内信推送-删除

- 接口声明：`DELETE /messages/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1132` · `MessagePushDetailResource`

### OPERATION-592 · 运营-触达管理-站内信推送-提交审核

- 接口声明：`PATCH /messages/<int:id_>/created`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1157` · `MessagePushDraftResource`

### OPERATION-593 · 运营-触达管理-站内信推送-审核

- 接口声明：`PATCH /messages/<int:id_>/audit`
- 输入字段：`status`, `auditor_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1188` · `MessagePushAuditResource`

### OPERATION-594 · 运营-触达管理-站内信推送-获取推送内容

- 接口声明：`GET /messages/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1232` · `MessagePushLangContentResource`

### OPERATION-595 · 运营-触达管理-站内信推送-编辑推送内容

- 接口声明：`PUT /messages/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1246` · `MessagePushLangContentResource`

### OPERATION-596 · 运营-触达管理-站内信推送-测试推送内容检查

- 接口声明：`GET /messages/<int:id_>/test`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1302` · `MessagePushTestResource`

### OPERATION-597 · 运营-触达管理-站内信推送-推送测试

- 接口声明：`POST /messages/<int:id_>/test`
- 输入字段：`accounts`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1311` · `MessagePushTestResource`

### OPERATION-598 · 运营-触达管理-站内信推送-推送用户下载

- 接口声明：`GET /messages/<int:id_>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1377` · `MessagePushUserResource`

### OPERATION-599 · 运营-触达管理-自动push-push策略列表

- 接口声明：`GET /strategy-pushes`
- 输入字段：`push_group`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1413` · `StrategyPushResource`

### OPERATION-600 · 自动push-创建push策略

- 接口声明：`POST /strategy-pushes`
- 输入字段：`name`, `type`, `push_group`, `assets_type`, `assets`, `bill_board`, `bill_board_rank`, `exclude_assets`, `volume_usd_1d`, `trigger_price_interval`, `trigger_rise_threshold`, `trigger_fall_threshold`, `user_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `execute_duration`, `start_time`, `end_time`, `timestamp_offset`, `push_limit_interval`, `jump_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1459` · `StrategyPushResource`

### OPERATION-601 · 运营-触达管理-PUSH策略推送-删除

- 接口声明：`DELETE /strategy-pushes/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1562` · `StrategyPushDetailResource`

### OPERATION-602 · 运营-触达管理-PUSH策略推送-获取策略详情

- 接口声明：`GET /strategy-pushes/<int:id_>`
- 输入字段：`is_export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1581` · `StrategyPushDetailResource`

### OPERATION-603 · 运营-触达管理-PUSH策略推送-编辑PUSH策略

- 接口声明：`PATCH /strategy-pushes/<int:id_>`
- 输入字段：`name`, `type`, `push_group`, `assets_type`, `assets`, `bill_board`, `bill_board_rank`, `exclude_assets`, `volume_usd_1d`, `trigger_price_interval`, `trigger_rise_threshold`, `trigger_fall_threshold`, `user_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `execute_duration`, `start_time`, `end_time`, `timestamp_offset`, `push_limit_interval`, `jump_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1697` · `StrategyPushDetailResource`

### OPERATION-604 · APP自动push测试-校验

- 接口声明：`GET /strategy-pushes/<int:id_>/test`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1799` · `AppStrategyPushContentTestResource`

### OPERATION-605 · 运营-触达管理-内容APP自动push测试

- 接口声明：`POST /strategy-pushes/<int:id_>/test`
- 输入字段：`accounts`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1814` · `AppStrategyPushContentTestResource`

### OPERATION-606 · 运营-触达管理-PUSH策略推送-审核

- 接口声明：`PATCH /strategy-pushes/<int:id_>/audit`
- 输入字段：`status`, `auditor_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1895` · `StrategyPushAuditResource`

### OPERATION-607 · 运营-触达管理-PUSH策略推送-下架策略

- 接口声明：`PATCH /strategy-pushes/<int:id_>/created`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1945` · `StrategyPushDraftResource`

### OPERATION-608 · 运营-触达管理-PUSH策略推送-暂停策略

- 接口声明：`PATCH /strategy-pushes/<int:id_>/suspended`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1972` · `StrategyPushSuspendResource`

### OPERATION-609 · 运营-APP推送-获取APP推送内容

- 接口声明：`GET /strategy-pushes/<int:id_>/langs/<lang>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:1999` · `StrategyPushContentResource`

### OPERATION-610 · 运营-APP推送-编辑APP推送内容

- 接口声明：`PUT /strategy-pushes/<int:id_>/langs/<lang>`
- 输入字段：`title`, `content`, `url`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:2021` · `StrategyPushContentResource`

### OPERATION-611 · 运营-触达管理-自动push策略报表

- 接口声明：`GET /strategy-pushes/report`
- 输入字段：`strategy_id`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/push.py:2078` · `StrategyPushReportResource`

### OPERATION-612 · 运营-通用运营配置-客服机器人-常见问题配置

- 接口声明：`GET /qa_category`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:274` · `QAResource`

### OPERATION-613 · 运营-通用运营配置-客服机器人-常见问题配置-新增

- 接口声明：`POST /qa_category`
- 输入字段：`names`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:279` · `QAResource`

### OPERATION-614 · 运营-通用运营配置-客服机器人-常见问题配置-详情

- 接口声明：`GET /qa_category/<int:category_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:323` · `QADetailResource`

### OPERATION-615 · 运营-通用运营配置-客服机器人-常见问题配置-编辑

- 接口声明：`PUT /qa_category/<int:category_id>`
- 输入字段：`names`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:337` · `QADetailResource`

### OPERATION-616 · 运营-通用运营配置-客服机器人-常见问题配置-删除

- 接口声明：`DELETE /qa_category/<int:category_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:387` · `QADetailResource`

### OPERATION-617 · 运营-通用运营配置-客服机器人-常见问题配置-是否展示

- 接口声明：`PUT /qa_category/<int:category_id>/show`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:419` · `QAShowResource`

### OPERATION-618 · 运营-通用运营配置-客服机器人-常见问题配置-移动

- 接口声明：`PUT /qa_category/<int:category_id>/move`
- 输入字段：`is_up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:461` · `QAMoveResource`

### OPERATION-619 · 运营-通用运营配置-客服机器人-单个问题配置

- 接口声明：`GET /qa_category/<int:category_id>/question`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:513` · `QAQuestionResource`

### OPERATION-620 · 运营-通用运营配置-客服机器人-单个问题配置-新增

- 接口声明：`POST /qa_category/<int:category_id>/question`
- 输入字段：`help_url_1`, `help_url_2`, `self_service_url`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:518` · `QAQuestionResource`

### OPERATION-621 · 运营-通用运营配置-客服机器人-单个问题配置

- 接口声明：`GET /qa_category/<int:category_id>/question/<int:question_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:575` · `QAQuestionDetailResource`

### OPERATION-622 · 运营-通用运营配置-客服机器人-单个问题配置-编辑

- 接口声明：`PUT /qa_category/<int:category_id>/question/<int:question_id>`
- 输入字段：`help_url_1`, `help_url_2`, `self_service_url`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:580` · `QAQuestionDetailResource`

### OPERATION-623 · 运营-通用运营配置-客服机器人-单个问题配置-删除

- 接口声明：`DELETE /qa_category/<int:category_id>/question/<int:question_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:653` · `QAQuestionDetailResource`

### OPERATION-624 · 运营-通用运营配置-客服机器人-单个问题配置-是否展示

- 接口声明：`PUT /qa_category/<int:category_id>/question/<int:question_id>/show`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:691` · `QAQuestionShowResource`

### OPERATION-625 · 运营-通用运营配置-客服机器人-单个问题配置-是否热门

- 接口声明：`PUT /qa_category/<int:category_id>/question/<int:question_id>/hot`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:727` · `QAQuestionHotResource`

### OPERATION-626 · 运营-通用运营配置-客服机器人-单个问题配置-移动

- 接口声明：`PUT /qa_category/<int:category_id>/question/<int:question_id>/move`
- 输入字段：`is_up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/self_service.py:779` · `QAQuestionMoveResource`

### OPERATION-627 · 触达管理-提示条-列表

- 接口声明：`GET `
- 输入字段：`name`, `type`, `platform`, `trigger_page`, `status`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:230` · `TipBarsResource`

### OPERATION-628 · 运营-提示条管理-新增提示条

- 接口声明：`POST `
- 输入字段：`name`, `type`, `started_at`, `ended_at`, `platform`, `trigger_pages`, `filter_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `jump_page_enabled`, `jump_type`, `jump_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:327` · `TipBarsResource`

### OPERATION-629 · 运营-提示条管理-提示条详情

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:412` · `TipBarResource`

### OPERATION-630 · 运营-提示条管理-编辑提示条

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`name`, `type`, `started_at`, `ended_at`, `platform`, `trigger_pages`, `filter_type`, `groups`, `whitelist_enabled`, `user_whitelist`, `abnormal_user_filters`, `jump_page_enabled`, `jump_type`, `jump_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:495` · `TipBarResource`

### OPERATION-631 · 运营-提示条管理-删除提示条

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:570` · `TipBarResource`

### OPERATION-632 · 运营-提示条管理-停止提示条

- 接口声明：`PUT /<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:590` · `TipBarOfflineResource`

### OPERATION-633 · 运营-提示条管理-编辑提示条内容

- 接口声明：`PUT /<int:id_>/langs/<lang>`
- 输入字段：`content`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:610` · `TipBarContentResource`

### OPERATION-634 · 运营-触达管理-提示条-提交审核

- 接口声明：`PATCH /<int:id_>/created`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:659` · `TipBarCreated`

### OPERATION-635 · 运营-触达管理-提示条-审核

- 接口声明：`PATCH /<int:id_>/audit`
- 输入字段：`status`, `auditor_remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:690` · `TipBarAudit`

### OPERATION-636 · 运营-触达管理-提示条-通知中提前结束

- 接口声明：`PATCH /<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:740` · `TipBarOffline`

### OPERATION-637 · 运营-触达管理-提示条-白名单设置

- 接口声明：`PATCH /whitelist`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/tip_bar.py:772` · `TipBarWhitelist`

### OPERATION-638 · 获取欢迎语列表

- 接口声明：`GET `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/welcome_message.py:19` · `WelcomeMessageListResource`

### OPERATION-639 · 新建欢迎语

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/welcome_message.py:39` · `WelcomeMessageListResource`

### OPERATION-640 · 获取欢迎语详情 

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/welcome_message.py:88` · `WelcomeMessageResource`

### OPERATION-641 · 编辑欢迎语 

- 接口声明：`PATCH /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/welcome_message.py:102` · `WelcomeMessageResource`

### OPERATION-642 · 删除欢迎语 

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/welcome_message.py:162` · `WelcomeMessageResource`

### OPERATION-643 · 运营-推荐返佣管理-推荐文案-列表 

- 接口声明：`GET /copy-writing`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:45` · `ReferralCopyWritingResource`

### OPERATION-644 · 运营-推荐返佣管理-推荐文案-添加文案 

- 接口声明：`POST /copy-writing`
- 输入字段：`translations`, `remark`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:106` · `ReferralCopyWritingResource`

### OPERATION-645 · 运营-推荐返佣管理-推荐文案-编辑文案 

- 接口声明：`PUT /copy-writing`
- 输入字段：`id`, `translations`, `remark`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:154` · `ReferralCopyWritingResource`

### OPERATION-646 · 运营-推荐返佣管理-推荐文案-修改排序 

- 接口声明：`PATCH /copy-writing`
- 输入字段：`id`, `change`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:223` · `ReferralCopyWritingResource`

### OPERATION-647 · 运营-推荐返佣管理-活动配置列表

- 接口声明：`GET /activities`
- 输入字段：`display_name`, `begin_at`, `end_at`, `activate_status`, `platform`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:349` · `ReferralActivityListResource`

### OPERATION-648 · 运营-推荐返佣管理-活动配置创建

- 接口声明：`POST /activities`
- 输入字段：`begin_at`, `end_at`, `web_jump_type`, `app_jump_type`, `web_jump_id`, `app_jump_id`, `light_pic_id`, `dark_pic_id`, `translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:386` · `ReferralActivityListResource`

### OPERATION-649 · 运营-推荐返佣管理-活动配置详情

- 接口声明：`GET /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:484` · `ReferralActivityResource`

### OPERATION-650 · 运营-推荐返佣管理-活动配置编辑

- 接口声明：`PUT /activity/<int:id_>`
- 输入字段：`begin_at`, `end_at`, `web_jump_type`, `app_jump_type`, `web_jump_id`, `app_jump_id`, `light_pic_id`, `dark_pic_id`, `translations`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:506` · `ReferralActivityResource`

### OPERATION-651 · 运营-推荐返佣管理-活动配置删除

- 接口声明：`DELETE /activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:578` · `ReferralActivityResource`

### OPERATION-652 · 运营-推荐返佣管理-活动配置下架

- 接口声明：`PATCH /activity/<int:id_>/offline`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:597` · `ReferralActivityOfflineResource`

### OPERATION-653 · 运营-推荐返佣管理-活动配置排序

- 接口声明：`PUT /activity-order/<int:id_>`
- 输入字段：`up`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:631` · `ReferralActivityOrderResource`

### OPERATION-654 · 被邀请API用户列表 

- 接口声明：`GET /special-referree-rates`
- 输入字段：`referree_id`, `referrer_id`, `referrer_type`, `status`, `min_rate`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:683` · `SpecialReferreeRatesResource`

### OPERATION-655 · 被邀请API用户-修改新返佣比例 

- 接口声明：`PUT /special-referree-rates`
- 输入字段：`id`, `rate`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:747` · `SpecialReferreeRatesResource`

### OPERATION-656 · AF自动绑定列表

- 接口声明：`GET /af-auto-bind-list`
- 输入字段：`user_id`, `referrer_id`, `af_channel`, `refer_code`, `register_time_start`, `register_time_end`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/referral.py:799` · `AfAutoBindListResource`

### OPERATION-657 · 用户-邀请返佣-KOL邀请数据导出-下载模板

- 接口声明：`GET /template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kol_referral.py:36` · `KOLReferralTemplateResource`

### OPERATION-658 · 用户-邀请返佣-KOL邀请数据导出-列表展示

- 接口声明：`GET `
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kol_referral.py:50` · `KOLReferralResource`

### OPERATION-659 · 用户-邀请返佣-KOL邀请数据导出-批量上传

- 接口声明：`POST `
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kol_referral.py:91` · `KOLReferralResource`

### OPERATION-660 · 用户-邀请返佣-KOL邀请数据导出-删除

- 接口声明：`DELETE `
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kol_referral.py:213` · `KOLReferralResource`

### OPERATION-661 · 用户-邀请返佣-KOL邀请数据导出-下载数据

- 接口声明：`GET /download`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kol_referral.py:238` · `KOLReferralReportResource`

### OPERATION-662 · 报表-返佣报表-类型返佣

- 接口声明：`GET /type`
- 输入字段：`report_type`, `type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/refer.py:56` · `ReferTypeReport`

### OPERATION-663 · 报表-返佣报表-返佣占比

- 接口声明：`GET /proportion`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/refer.py:143` · `ReferProportionReport`

### OPERATION-664 · 报表-普通邀请报表

- 接口声明：`GET /normal_refer`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/refer.py:214` · `NormalReferReport`

### OPERATION-665 · 用户-邀请返佣-普通返佣记录 

- 接口声明：`GET /normal-user-refer-report`
- 输入字段：`report_type`, `start_date`, `end_date`, `user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/refer.py:297` · `UserReferralDetailReportResource`

### OPERATION-666 · 查询行情页活动Tab可展示活动ID列表  Returns:     reward_center (object): 奖励中心信息         claimable_count (int): 待领取奖励数量         available_task_count (int): 可参与任务数量         total_count (int): 待领取奖励

- 接口声明：`GET /app-tab/available-ids`
- 输入字段：`device_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:517` · `ActivityTabAvailableIdsResource`

### OPERATION-667 · BannersResource.get（用途待确认）

- 接口声明：`GET /banners`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:552` · `BannersResource`

### OPERATION-668 · 日历-活动日历

- 接口声明：`GET /calendar`
- 输入字段：`limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:597` · `CalendarResource`

### OPERATION-669 · PopupWindowsResource.get（用途待确认）

- 接口声明：`GET /popup-windows`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:623` · `PopupWindowsResource`

### OPERATION-670 · ActivitiesResource.get（用途待确认）

- 接口声明：`GET /list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:641` · `ActivitiesResource`

### OPERATION-671 · ExposureActivitiesResource.get（用途待确认）

- 接口声明：`GET /exposure/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:670` · `ExposureActivitiesResource`

### OPERATION-672 · 交易排名活动列表

- 接口声明：`GET /trade-rank/list`
- 输入字段：`ids`, `category`, `market`, `page`, `limit`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:726` · `TradeRankActivityListResource`

### OPERATION-673 · 交易排名活动详情

- 接口声明：`GET /trade-rank/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:964` · `TradeRankActivityResource`

### OPERATION-674 · 交易排名活动报名

- 接口声明：`POST /trade-rank/<int:id_>/user`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:1065` · `TradeRankActivityUserResource`

### OPERATION-675 · 交易排名活动 参与记录

- 接口声明：`GET /trade-rank/history`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1104` · `TradeRankActivityJoinHistoryResource`

### OPERATION-676 · 充值排名

- 接口声明：`GET /deposit/rank`
- 输入字段：`status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:1189` · `DepositActivityRankListResource`

### OPERATION-677 · 用户充值排名

- 接口声明：`GET /deposit/rank/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:1269` · `DepositActivityRankResource`

### OPERATION-678 · 挖矿-活动列表

- 接口声明：`GET /mining`
- 输入字段：`mining_mode`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:1303` · `MiningActivityListResource`

### OPERATION-679 · 挖矿活动详情 

- 接口声明：`GET /mining/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:1328` · `MiningActivityDetailResource`

### OPERATION-680 · 挖矿活动-用户报名 

- 接口声明：`POST /mining/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1339` · `MiningActivityDetailResource`

### OPERATION-681 · 用户某个挖矿活动的信息 

- 接口声明：`GET /mining/user-info`
- 输入字段：`activity_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1364` · `MiningActivityUserInfoResource`

### OPERATION-682 · 挖矿收益记录 

- 接口声明：`GET /mining/reward`
- 输入字段：`activity_id`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1443` · `MiningActivityRewardResource`

### OPERATION-683 · 提取（质押、做市）挖矿的收益 

- 接口声明：`POST /mining/reward`
- 输入字段：`activity_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1527` · `MiningActivityRewardResource`

### OPERATION-684 · （质押、做市）挖矿的操作历史：质押、提取质押、提取收益 

- 接口声明：`GET /mining/history`
- 输入字段：`activity_id`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1554` · `MiningActivityHistoryResource`

### OPERATION-685 · 质押挖矿-质押操作 

- 接口声明：`POST /mining/pledge`
- 输入字段：`activity_id`, `amount`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1606` · `MiningActivityPledgeResource`

### OPERATION-686 · 质押挖矿-提取质押操作 

- 接口声明：`DELETE /mining/pledge`
- 输入字段：`activity_id`, `amount`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:1643` · `MiningActivityPledgeResource`

### OPERATION-687 · 空投-活动列表

- 接口声明：`GET /airdrop`
- 输入字段：`ids`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:2117` · `AirdropActivityListResource`

### OPERATION-688 · 空投活动详情 

- 接口声明：`GET /airdrop/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:2209` · `AirdropActivityDetailResource`

### OPERATION-689 · 空投活动-用户报名 

- 接口声明：`POST /airdrop/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:2235` · `AirdropActivityDetailResource`

### OPERATION-690 · AirdropActivityAnswerSingleResource.post（用途待确认）

- 接口声明：`POST /airdrop/answer/<int:activity_id>/single`
- 输入字段：`number`, `answer`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:2449` · `AirdropActivityAnswerSingleResource`

### OPERATION-691 · 空投活动答题信息 

- 接口声明：`GET /airdrop/answer/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:2504` · `AirdropActivityAnswerResource`

### OPERATION-692 · 空投活动回答 

- 接口声明：`POST /airdrop/answer/<int:activity_id>`
- 输入字段：`answers`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:2516` · `AirdropActivityAnswerResource`

### OPERATION-693 · 用户的空投活动的信息 

- 接口声明：`GET /airdrop/user-info`
- 输入字段：`activity_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:2567` · `AirdropActivityUserInfoResource`

### OPERATION-694 · 用户的空投参与记录 

- 接口声明：`GET /airdrop/reword`
- 输入字段：`airdrop_mode`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:2664` · `AirdropActivityRewordResource`

### OPERATION-695 · Dibs-活动列表

- 接口声明：`GET /dibs`
- 输入字段：`limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:2789` · `DibsActivityListResource`

### OPERATION-696 · Dibs活动详情 

- 接口声明：`GET /dibs/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:2837` · `DibsActivityDetailResource`

### OPERATION-697 · Dibs活动-用户报名 

- 接口声明：`POST /dibs/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:2852` · `DibsActivityDetailResource`

### OPERATION-698 · 用户的Dibs活动的信息 

- 接口声明：`GET /dibs/user-info`
- 输入字段：`activity_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:2905` · `DibsActivityUserInfoResource`

### OPERATION-699 · 用户的Dibs参与记录 

- 接口声明：`GET /dibs/record`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:2952` · `DibsActivityRewordResource`

### OPERATION-700 · 投资-活动列表

- 接口声明：`GET /ieo`
- 输入字段：`limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:3000` · `IeoActivityListResource`

### OPERATION-701 · 投资活动详情 

- 接口声明：`GET /ieo/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:3044` · `IeoActivityDetailResource`

### OPERATION-702 · 投资活动-用户申购 

- 接口声明：`POST /ieo/<int:activity_id>`
- 输入字段：`subscribe_count`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:3061` · `IeoActivityDetailResource`

### OPERATION-703 · 投资活动详情 

- 接口声明：`GET /ieo/orders/<int:activity_id>/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:3133` · `IeoActivityOrdersDetailResource`

### OPERATION-704 · 投资活动详情 

- 接口声明：`DELETE /ieo/orders/<int:activity_id>/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:3186` · `IeoActivityOrdersDetailResource`

### OPERATION-705 · 用户的投资活动的信息 

- 接口声明：`GET /ieo/user-info`
- 输入字段：`activity_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3230` · `IeoActivityUserInfoResource`

### OPERATION-706 · 投资活动订单列表 

- 接口声明：`GET /ieo/orders`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3290` · `IeoActivityOrdersResource`

### OPERATION-707 · 投资活动签署协议 

- 接口声明：`POST /ieo/sign/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:3353` · `IeoActivitySignContractResource`

### OPERATION-708 · 旧版卡券弹框接口, APP兼容保留

- 接口声明：`GET /user/coupon`
- 输入字段：`coupon_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3370` · `UserCouponsResource`

### OPERATION-709 · 用户领取卡劵

- 接口声明：`POST /coupons/<int:pool_id>`
- 输入字段：`device_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:3414` · `UserReceiveCouponResource`

### OPERATION-710 · 兑换卡券

- 接口声明：`POST /coupon`
- 输入字段：`code`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:3499` · `UserExchangeCouponResource`

### OPERATION-711 · UserExchangeCouponHistoryResource.get（用途待确认）

- 接口声明：`GET /coupons/exchange-history`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3580` · `UserExchangeCouponHistoryResource`

### OPERATION-712 · 卡劵中心-公共卡劵

- 接口声明：`GET /coupons/public`
- 输入字段：`coupon_type`, `coupon_status`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3600` · `PublicCouponResponse`

### OPERATION-713 · 卡劵中心-个人卡劵

- 接口声明：`GET /coupons/myself`
- 输入字段：`coupon_type`, `coupon_status`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3672` · `MyselfCouponResponse`

### OPERATION-714 · 卡券状态定义 

- 接口声明：`GET /coupons/statuses`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:3819` · `CouponStatuesResponse`

### OPERATION-715 · 用户手动使用卡券 

- 接口声明：`POST /coupons/myself/<int:user_coupon_id>`
- 输入字段：`asset`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3838` · `UseMyselfCouponResponse`

### OPERATION-716 · 未使用和使用中的理财加息券，用于理财账户页 

- 接口声明：`GET /coupons/investment`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3896` · `InvestmentCouponsResponse`

### OPERATION-717 · 一键领取弹框

- 接口声明：`GET /coupons/popup`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3967` · `CouponPopupResponse`

### OPERATION-718 · 卡劵弹框 一键领取

- 接口声明：`POST /coupons/receive/all`
- 输入字段：`pool_ids`, `device_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:3979` · `CouponReceiveAllResponse`

### OPERATION-719 · 直接发放的弹框查看上报 确保只弹出一次

- 接口声明：`POST /coupons/popup/report`
- 输入字段：`pool_ids`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:4043` · `CouponPopupReportResponse`

### OPERATION-720 · APP 个人中心 活跃卡劵个数

- 接口声明：`GET /coupons/usable/total`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:4066` · `CouponUsableTotalResponse`

### OPERATION-721 · 五周年活动账单

- 接口声明：`GET /fifth-anniversary/summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:4089` · `FifthAnniversarySummaryResource`

### OPERATION-722 · FifthAnniversaryHiveFiveResource.get（用途待确认）

- 接口声明：`GET /fifth-anniversary/high-five`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4149` · `FifthAnniversaryHiveFiveResource`

### OPERATION-723 · FifthAnniversaryHiveFiveResource.post（用途待确认）

- 接口声明：`POST /fifth-anniversary/high-five`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4155` · `FifthAnniversaryHiveFiveResource`

### OPERATION-724 · 5周年-挑战活动、盲盒活动时间 

- 接口声明：`GET /fifth-anniversary/time`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4170` · `FifthAnniversaryTimeResource`

### OPERATION-725 · FifthAnniversaryThankLetterResource.get（用途待确认）

- 接口声明：`GET /fifth-anniversary/thank-letter`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4202` · `FifthAnniversaryThankLetterResource`

### OPERATION-726 · FifthAnniversaryThankLetterResource.post（用途待确认）

- 接口声明：`POST /fifth-anniversary/thank-letter`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4210` · `FifthAnniversaryThankLetterResource`

### OPERATION-727 · 5周年-是否禁用 

- 接口声明：`GET /fifth-anniversary/forbidden`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4241` · `FifthAnniversaryForbiddenResource`

### OPERATION-728 · 5周年-大挑战门票 

- 接口声明：`GET /fifth-anniversary/ticket`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4265` · `FifthAnniversaryChallengeTicketResource`

### OPERATION-729 · 5周年-领取大挑战门票 

- 接口声明：`POST /fifth-anniversary/ticket`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4277` · `FifthAnniversaryChallengeTicketResource`

### OPERATION-730 · 5周年-盲盒开箱机会、盲盒中奖 轮播 

- 接口声明：`GET /fifth-anniversary/broadcast/<type_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4329` · `FifthAnniversaryBroadcastResource`

### OPERATION-731 · 5周年-大挑战任务状态 

- 接口声明：`GET /fifth-anniversary/challenge`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4353` · `FifthAnniversaryChallengeStatusResource`

### OPERATION-732 · 5周年-盲盒数目信息 

- 接口声明：`GET /fifth-anniversary/box`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4378` · `FifthAnniversaryBoxResource`

### OPERATION-733 · 5周年-开盲盒 

- 接口声明：`POST /fifth-anniversary/box`
- 输入字段：`box_type`, `device_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4430` · `FifthAnniversaryBoxResource`

### OPERATION-734 · 5周年-用户盲盒奖品信息 

- 接口声明：`GET /fifth-anniversary/box/reward`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4512` · `FifthAnniversaryBoxRewardResource`

### OPERATION-735 · 五周年-大挑战-卡券接口

- 接口声明：`GET /fifth-anniversary/coupons`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:4532` · `FiveActivityCoupons`

### OPERATION-736 · FiveActivityReceiveCoupon.post（用途待确认）

- 接口声明：`POST /fifth-anniversary/coupons/<int:pool_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:4543` · `FiveActivityReceiveCoupon`

### OPERATION-737 · 6周年-活动信息 

- 接口声明：`GET /sixth-anniversary/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4554` · `SixthAnniversaryInfoResource`

### OPERATION-738 · 6周年-1024游戏二维码生成 

- 接口声明：`GET /sixth-anniversary/game1024/qrcode`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4582` · `SixthAnniversaryGameQrcodeResource`

### OPERATION-739 · 6周年-活动海报二维码生成 

- 接口声明：`GET /sixth-anniversary/activity/qrcode`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4597` · `SixthAnniversaryActivityQrcodeResource`

### OPERATION-740 · SixthAnniversaryAnswerCompleteResource.get（用途待确认）

- 接口声明：`GET /sixth-anniversary/answer/complete`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4613` · `SixthAnniversaryAnswerCompleteResource`

### OPERATION-741 · SixthAnniversaryAnswerCompleteResource.post（用途待确认）

- 接口声明：`POST /sixth-anniversary/answer/complete`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4620` · `SixthAnniversaryAnswerCompleteResource`

### OPERATION-742 · SixthAnniversaryRewardReceiveResource.get（用途待确认）

- 接口声明：`GET /sixth-anniversary/reward/receive`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4643` · `SixthAnniversaryRewardReceiveResource`

### OPERATION-743 · SixthAnniversaryRewardReceiveResource.post（用途待确认）

- 接口声明：`POST /sixth-anniversary/reward/receive`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4653` · `SixthAnniversaryRewardReceiveResource`

### OPERATION-744 · SixthAnniversaryQuestionResource.get（用途待确认）

- 接口声明：`GET /sixth-anniversary/questions`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4685` · `SixthAnniversaryQuestionResource`

### OPERATION-745 · 七周年用户账单

- 接口声明：`GET /seventh-anniversary-user-bill`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4720` · `SeventhAnniversaryUserBillResource`

### OPERATION-746 · 7周年-活动信息 

- 接口声明：`GET /seventh-anniversary/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4843` · `SeventhAnniversaryInfoResource`

### OPERATION-747 · 7周年-活动海报二维码生成 

- 接口声明：`GET /seventh-anniversary/activity/qrcode`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4865` · `SeventhAnniversaryActivityQrcodeResource`

### OPERATION-748 · 7周年-币种Logo批量获取 

- 接口声明：`GET /seventh-anniversary/asset/logo`
- 输入字段：`assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:4880` · `SeventhAnniversaryAssetLogoResource`

### OPERATION-749 · SeventhAnniversaryRewardReceiveResource.get（用途待确认）

- 接口声明：`GET /seventh-anniversary/reward/receive`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4899` · `SeventhAnniversaryRewardReceiveResource`

### OPERATION-750 · SeventhAnniversaryRewardReceiveResource.post（用途待确认）

- 接口声明：`POST /seventh-anniversary/reward/receive`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4913` · `SeventhAnniversaryRewardReceiveResource`

### OPERATION-751 · 八周年用户账单

- 接口声明：`GET /eighth-anniversary/bill`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:4947` · `EighthAnniversaryUserBillResource`

### OPERATION-752 · PerpetualSpecialIndexResource.get（用途待确认）

- 接口声明：`GET /perpetual-special/index`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5046` · `PerpetualSpecialIndexResource`

### OPERATION-753 · PerpetualSpecialActivitiesResource.get（用途待确认）

- 接口声明：`GET /perpetual-special/activities`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5063` · `PerpetualSpecialActivitiesResource`

### OPERATION-754 · 活动访问次数

- 接口声明：`POST /perpetual-special/activities/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5077` · `PerpetualSpecialActivityReportResource`

### OPERATION-755 · PerpetualSpecialTasksResource.get（用途待确认）

- 接口声明：`GET /perpetual-special/tasks`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:5088` · `PerpetualSpecialTasksResource`

### OPERATION-756 · PerpetualSpecialTasksResource.post（用途待确认）

- 接口声明：`POST /perpetual-special/tasks`
- 输入字段：`task_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:5093` · `PerpetualSpecialTasksResource`

### OPERATION-757 · NovicePrefectureResource.get（用途待确认）

- 接口声明：`GET /newbie-zone/index`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:5106` · `NovicePrefectureResource`

### OPERATION-758 · NovicePrefectureActivityResource.get（用途待确认）

- 接口声明：`GET /newbie-zone/activity`
- 输入字段：`task_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5117` · `NovicePrefectureActivityResource`

### OPERATION-759 · 大使活动列表

- 接口声明：`GET /ambassador-activity/list`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5171` · `AmbassadorActivityListResource`

### OPERATION-760 · 大使活动详情

- 接口声明：`GET /ambassador-activity/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5272` · `AmbassadorActivityDetailResource`

### OPERATION-761 · 大使活动报名

- 接口声明：`POST /ambassador-activity/<int:id_>/apply`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:5421` · `AmbassadorActivityUserResource`

### OPERATION-762 · 大使活动参与记录

- 接口声明：`GET /ambassador-activity/history`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:5465` · `AmbassadorActivityJoinHistoryResource`

### OPERATION-763 · SatoshiBidResource.get（用途待确认）

- 接口声明：`GET /satoshi/bid`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5529` · `SatoshiBidResource`

### OPERATION-764 · SatoshiBidResource.post（用途待确认）

- 接口声明：`POST /satoshi/bid`
- 输入字段：`amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:5573` · `SatoshiBidResource`

### OPERATION-765 · SatoshiBidHistoryResource.get（用途待确认）

- 接口声明：`GET /satoshi/bid-history`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5640` · `SatoshiBidHistoryResource`

### OPERATION-766 · SatoshiMyBidHistoryResource.get（用途待确认）

- 接口声明：`GET /satoshi/my-bid-history`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:5683` · `SatoshiMyBidHistoryResource`

### OPERATION-767 · 生成活动用户，回调 Wallacy 地址

- 接口声明：`POST /wallacy`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:5741` · `WallacyActiveUserResource`

### OPERATION-768 · 活动用户详情

- 接口声明：`GET /wallacy`
- 输入字段：`code`, `start_date`, `end_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5759` · `WallacyActiveUserResource`

### OPERATION-769 · CoinexWalletTrafficResource.get（用途待确认）

- 接口声明：`GET /coinex-wallet/traffic`
- 输入字段：`platform`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5813` · `CoinexWalletTrafficResource`

### OPERATION-770 · 活动用户详情

- 接口声明：`GET /vertus`
- 输入字段：`code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5826` · `VertusActivityResource`

### OPERATION-771 · 充值福利-活动列表

- 接口声明：`GET /deposit-bonus`
- 输入字段：`ids`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5900` · `DepositBonusActivityListResource`

### OPERATION-772 · 充值福利-活动详情 

- 接口声明：`GET /deposit-bonus/<int:activity_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:5965` · `DepositBonusDetailResource`

### OPERATION-773 · 充值福利-用户报名 

- 接口声明：`POST /deposit-bonus/<int:activity_id>`
- 输入字段：`config_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:5976` · `DepositBonusDetailResource`

### OPERATION-774 · 用户参与充值福利活动的信息 

- 接口声明：`GET /deposit-bonus/user-info`
- 输入字段：`activity_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:6037` · `DepositBonusActivityUserInfoResource`

### OPERATION-775 · 用户的充值福利参与记录 

- 接口声明：`GET /deposit-bonus/history`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/activity.py:6122` · `DepositBonusActivityRewordResource`

### OPERATION-776 · 充值福利-活动 banners

- 接口声明：`GET /deposit-bonus/banners`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:6248` · `DepositBonusActivityBannersResource`

### OPERATION-777 · DepositBonusOpeningAgreementResource.get（用途待确认）

- 接口声明：`GET /deposit-bonus/opening-agreement`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:6267` · `DepositBonusOpeningAgreementResource`

### OPERATION-778 · DepositBonusOpeningAgreementResource.post（用途待确认）

- 接口声明：`POST /deposit-bonus/opening-agreement`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:6276` · `DepositBonusOpeningAgreementResource`

### OPERATION-779 · PerpetualProfitRealRankResource.get（用途待确认）

- 接口声明：`GET /perpetual-profit-real/rank`
- 输入字段：`cycle_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:6290` · `PerpetualProfitRealRankResource`

### OPERATION-780 · PerpetualProfitRealAnonymousResource.get（用途待确认）

- 接口声明：`GET /perpetual-profit-real/anonymous`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=True)
- 代码依据：`app/api/frontend/activity.py:6318` · `PerpetualProfitRealAnonymousResource`

### OPERATION-781 · PerpetualProfitRealAnonymousResource.post（用途待确认）

- 接口声明：`POST /perpetual-profit-real/anonymous`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=True)
- 代码依据：`app/api/frontend/activity.py:6325` · `PerpetualProfitRealAnonymousResource`

### OPERATION-782 · EighthAnniversaryRewardResource.get（用途待确认）

- 接口声明：`GET /eighth-anniversary/rewards`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:6367` · `EighthAnniversaryRewardResource`

### OPERATION-783 · EighthAnniversaryLotteryResource.get（用途待确认）

- 接口声明：`GET /eighth-anniversary/lottery`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/activity.py:6381` · `EighthAnniversaryLotteryResource`

### OPERATION-784 · EighthAnniversaryLotteryResource.post（用途待确认）

- 接口声明：`POST /eighth-anniversary/lottery`
- 输入字段：`device_id`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/activity.py:6426` · `EighthAnniversaryLotteryResource`

### OPERATION-785 · EmailPushCountResource.get（用途待确认）

- 接口声明：`GET /count/<int:id_>`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/email_push.py:17` · `EmailPushCountResource`

### OPERATION-786 · EmailCodeResource.get（用途待确认）

- 接口声明：`GET /email/code`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/message.py:41` · `EmailCodeResource`

### OPERATION-787 · EmailCodeValidationResource.post（用途待确认）

- 接口声明：`POST /validate/email/code`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/message.py:49` · `EmailCodeValidationResource`

### OPERATION-788 · MobileCodeResource.get（用途待确认）

- 接口声明：`GET /sms`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/message.py:58` · `MobileCodeResource`

### OPERATION-789 · MobileCodeValidationResource.post（用途待确认）

- 接口声明：`POST /validate/sms`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/message.py:66` · `MobileCodeValidationResource`

### OPERATION-790 · 站内信-标签类型列表 

- 接口声明：`GET /channels`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/message.py:74` · `MessageChannelsResource`

### OPERATION-791 · ?display_type=POPUP_WINDOW&status=not_view : 弹窗列表 ?status=not_view : 未读列表 & 未读总数

- 接口声明：`GET /`
- 输入字段：`status`, `channel`, `display_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:86` · `MessagesResource`

### OPERATION-792 · 标为已读 

- 接口声明：`POST /`
- 输入字段：`display_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:202` · `MessagesResource`

### OPERATION-793 · 清空所有已读 

- 接口声明：`DELETE /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:221` · `MessagesResource`

### OPERATION-794 · MessageResource.get（用途待确认）

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:310` · `MessageResource`

### OPERATION-795 · MessageResource.post（用途待确认）

- 接口声明：`POST /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:319` · `MessageResource`

### OPERATION-796 · 获取站内信详情 

- 接口声明：`GET /detail`
- 输入字段：`id`, `push_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:341` · `MessageDetailResource`

### OPERATION-797 · 站内信点击跳转链接的上报 

- 接口声明：`POST /report/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:369` · `MessageReportResource`

### OPERATION-798 · 获取未读数和需要弹窗的列表，兼容APP保留 

- 接口声明：`GET /count`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:389` · `MessageCountResource`

### OPERATION-799 · 标为已读，兼容APP保留 

- 接口声明：`POST /count`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:422` · `MessageCountResource`

### OPERATION-800 · 清空所有已读，兼容APP保留 

- 接口声明：`DELETE /count`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/message.py:433` · `MessageCountResource`

### OPERATION-801 · MissionTasksResource.get（用途待确认）

- 接口声明：`GET /tasks`
- 输入字段：`channel`, `refer_code`, `device_id`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/mission.py:111` · `MissionTasksResource`

### OPERATION-802 · 任务详情 :param id_: 用户登录时, preview为true 是 user_mission_id, false 是 mission_id; 未登录是 mission_id :param preview: 是否预览 preview=true 时，不传 user 信息，获取预览数据(同未登录时获取的数据) :return:

- 接口声明：`GET /tasks/<int:id_>`
- 输入字段：`preview`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/mission.py:292` · `MissionInfoResource`

### OPERATION-803 · MissionBannerResource.get（用途待确认）

- 接口声明：`GET /banner`
- 输入字段：`channel`, `refer_code`, `device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/mission.py:317` · `MissionBannerResource`

### OPERATION-804 · MissionNewbieHubTasksResource.get（用途待确认）

- 接口声明：`GET /newbie-hub/tasks`
- 输入字段：`channel`, `device_id`, `refer_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/mission.py:348` · `MissionNewbieHubTasksResource`

### OPERATION-805 · 邀请任务统计

- 接口声明：`GET /mission-plan/referral/statistics`
- 输入字段：`page`, `limit`, `status`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/mission.py:436` · `ReferralMissionPlanStatisticsResource`

### OPERATION-806 · 登录页市场

- 接口声明：`GET /login-page-market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:65` · `LoginPageMarketResource`

### OPERATION-807 · 首页-新手指引

- 接口声明：`GET /newer-guide`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:76` · `NewerGuideResource`

### OPERATION-808 · 首页博客

- 接口声明：`GET /blog-display`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:98` · `BlogDisplayResource`

### OPERATION-809 · ThemeResource.get（用途待确认）

- 接口声明：`GET /theme`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:122` · `ThemeResource`

### OPERATION-810 · NotificationBarsResource.get（用途待确认）

- 接口声明：`GET /notification-bars`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:151` · `NotificationBarsResource`

### OPERATION-811 · TipBarResource.get（用途待确认）

- 接口声明：`GET /tip-bars`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:166` · `TipBarResource`

### OPERATION-812 · AssetMaintainResource.get（用途待确认）

- 接口声明：`GET /asset-maintain`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:186` · `AssetMaintainResource`

### OPERATION-813 · NewbieHubBannersResource.get（用途待确认）

- 接口声明：`GET /newbie-hub/banners`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:222` · `NewbieHubBannersResource`

### OPERATION-814 · CharityBannerResource.get（用途待确认）

- 接口声明：`GET /charity/banner`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:239` · `CharityBannerResource`

### OPERATION-815 · CharityDonationResource.get（用途待确认）

- 接口声明：`GET /charity/donation`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:252` · `CharityDonationResource`

### OPERATION-816 · CharityActivityResource.get（用途待确认）

- 接口声明：`GET /charity/activity`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:275` · `CharityActivityResource`

### OPERATION-817 · CharityVideoResource.get（用途待确认）

- 接口声明：`GET /charity/video`
- 输入字段：`category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:288` · `CharityVideoResource`

### OPERATION-818 · CharityCategoryResource.get（用途待确认）

- 接口声明：`GET /charity/category`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:315` · `CharityCategoryResource`

### OPERATION-819 · CharityFootprintResource.get（用途待确认）

- 接口声明：`GET /charity/footprint`
- 输入字段：`category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:376` · `CharityFootprintResource`

### OPERATION-820 · CharityFootprintDetailResource.get（用途待确认）

- 接口声明：`GET /charity/footprint/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:403` · `CharityFootprintDetailResource`

### OPERATION-821 · MarketBannerResource.get（用途待确认）

- 接口声明：`GET /market-banner`
- 输入字段：`code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:438` · `MarketBannerResource`

### OPERATION-822 · 数据已经整合到任务中心页面 /auth/page-config

- 接口声明：`GET /page-inset`
- 输入字段：`page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:468` · `PageImageResource`

### OPERATION-823 · AssetCirculationHistoryResource.get（用途待确认）

- 接口声明：`GET /assets/circulation-history`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:487` · `AssetCirculationHistoryResource`

### OPERATION-824 · Footer Learn 板块配置列表，供 WEB/H5 展示

- 接口声明：`GET /learn-configs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:501` · `LearnConfigsResource`

### OPERATION-825 · 获取 SNS 配置信息

- 接口声明：`GET /sns-conf`
- 输入字段：`business`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:543` · `SNSConfResource`

### OPERATION-826 · InsetsResource.get（用途待确认）

- 接口声明：`GET /insets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:567` · `InsetsResource`

### OPERATION-827 · 合约交易页活动列表

- 接口声明：`GET /perpetual-activity`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:612` · `PerpetualActivity`

### OPERATION-828 · DynamicFallingResource.get（用途待确认）

- 接口声明：`GET /dynamic-falling`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:625` · `DynamicFallingResource`

### OPERATION-829 · P2pActivityResource.get（用途待确认）

- 接口声明：`GET /p2p/activity`
- 输入字段：`show_type`, `fiat`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:697` · `P2pActivityResource`

### OPERATION-830 · 获取登录注册页面展示数据

- 接口声明：`GET /auth/page-config`
- 输入字段：`channel`, `refer_code`, `device_id`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:729` · `AuthPageConfigResource`

### OPERATION-831 · 获取用户相关的新手任务

- 接口声明：`GET /user-mission`
- 输入字段：`channel`, `refer_code`, `device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/operation.py:776` · `MissionResource`

### OPERATION-832 · 推荐比例的配置信息 

- 接口声明：`GET /config`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:101` · `ReferralConfigResource`

### OPERATION-833 · UserReferralRewardsResource.get（用途待确认）

- 接口声明：`GET /user-rewards`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:117` · `UserReferralRewardsResource`

### OPERATION-834 · 获取用户邀请返佣的基础信息 其他接口太重，获取的信息过多

- 接口声明：`GET /basic`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:138` · `ReferralBasicResource`

### OPERATION-835 · 推荐信息

- 接口声明：`GET /info`
- 输入字段：`type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:155` · `ReferralInfoResource`

### OPERATION-836 · ReferralCodeInfoResource.get（用途待确认）

- 接口声明：`GET /code`
- 输入字段：`referral_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:294` · `ReferralCodeInfoResource`

### OPERATION-837 · 推荐链接列表 / 推荐邀请码列表 

- 接口声明：`GET /codes`
- 输入字段：`type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:312` · `ReferralCodesResource`

### OPERATION-838 · 生成推荐链接 

- 接口声明：`POST /codes`
- 输入字段：`remark`, `rate`, `code`, `is_default`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:377` · `ReferralCodesResource`

### OPERATION-839 · 编辑推荐链接｜将推荐链接设为默认 

- 接口声明：`PUT /codes`
- 输入字段：`code`, `remark`, `rate`, `is_default`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:424` · `ReferralCodesResource`

### OPERATION-840 · 推荐文案列表 

- 接口声明：`GET /copywritings`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:466` · `ReferralCopyWritingsResource`

### OPERATION-841 · 推广数据分析-返佣曲线(用户每日返佣数据表格) 

- 接口声明：`GET /series`
- 输入字段：`code`, `points`, `type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:496` · `ReferralSeriesResource`

### OPERATION-842 · 推荐历史 / 推荐记录 

- 接口声明：`GET /history`
- 输入字段：`page`, `limit`, `code`, `search_keyword`, `type`, `start_date`, `end_date`, `has_trade`, `is_valid`, `is_coupon_gift`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:535` · `ReferralHistoryResource`

### OPERATION-843 · 绑定邀请人 

- 接口声明：`POST /history`
- 输入字段：`code`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:981` · `ReferralHistoryResource`

### OPERATION-844 · 推荐返佣历史 / 返佣记录 

- 接口声明：`GET /asset/history`
- 输入字段：`page`, `limit`, `code`, `start_date`, `end_date`, `report_type`, `type`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1026` · `ReferralAssetHistoryResource`

### OPERATION-845 · 推荐排行，不再使用

- 接口声明：`GET /rank`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:1195` · `ReferralRankResource`

### OPERATION-846 · 推荐图片

- 接口声明：`GET /pictures`
- 输入字段：`version`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:1206` · `ReferralPicturesResource`

### OPERATION-847 · 推荐图片（含好友邀请海报和活动海报）

- 接口声明：`GET /new-pictures`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1228` · `NewReferralPicturesResource`

### OPERATION-848 · 商务大使申请

- 接口声明：`POST /ambassador/application`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1302` · `AmbassadorApplicationResource`

### OPERATION-849 · 大使申请的校验信息，给前端用

- 接口声明：`GET /ambassador/application`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1354` · `AmbassadorApplicationResource`

### OPERATION-850 · 大使信息

- 接口声明：`GET /ambassador/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1392` · `AmbassadorInfoResource`

### OPERATION-851 · 大使点亮大洲

- 接口声明：`PATCH /ambassador/info`
- 输入字段：`continent`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1460` · `AmbassadorInfoResource`

### OPERATION-852 · 大使月度返佣历史，不再使用

- 接口声明：`GET /ambassador/asset/history`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1483` · `AmbassadorAssetHistoryResource`

### OPERATION-853 · 大使攻略列表，不再使用

- 接口声明：`GET /ambassador/guides`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:1500` · `AmbassadorGuidesResource`

### OPERATION-854 · 大使代理信息

- 接口声明：`GET /ambassador/agent/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1517` · `AmbassadorAgentInfoResource`

### OPERATION-855 · 大使代理邀请历史，不再使用

- 接口声明：`GET /ambassador/agent/history`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1538` · `AmbassadorAgentHistoryResource`

### OPERATION-856 · 大使代理返佣历史，不再使用

- 接口声明：`GET /ambassador/agent/asset/history`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1556` · `AmbassadorAgentAssetHistoryResource`

### OPERATION-857 · 大使排名，不再使用

- 接口声明：`GET /ambassador/rank`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:1574` · `StarRankResource`

### OPERATION-858 · 优秀大使

- 接口声明：`GET /ambassador/star`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:1601` · `StarResource`

### OPERATION-859 · 大使最新活动

- 接口声明：`GET /ambassador/activity`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:1617` · `ActivityResource`

### OPERATION-860 · ReferralActivityBannersResource.get（用途待确认）

- 接口声明：`GET /activity/banners`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/referral.py:1663` · `ReferralActivityBannersResource`

### OPERATION-861 · 大使主页-邀请礼入口

- 接口声明：`GET /ambassador/coupon-gift-entrance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1690` · `AmbassadorCouponGiftResource`

### OPERATION-862 · 返佣-我的邀请礼入口

- 接口声明：`GET /coupon-gift/myself-entrance`
- 输入字段：`type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1726` · `MyselfEntranceCouponGiftResource`

### OPERATION-863 · 返佣-我的邀请礼

- 接口声明：`GET /coupon-gift/myself`
- 输入字段：`type`, `is_valid`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1759` · `MyselfCouponGiftResource`

### OPERATION-864 · 大使看板-数据总览

- 接口声明：`GET /ambassador/dashboard/summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1921` · `AmbDashboardSummaryResource`

### OPERATION-865 · 大使看板-周期内用户数据

- 接口声明：`GET /ambassador/dashboard/user-series`
- 输入字段：`time_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1950` · `AmbDashboardUserDataSeriesResource`

### OPERATION-866 · 大使看板-周期内用户数据

- 接口声明：`GET /ambassador/dashboard/trade-series`
- 输入字段：`time_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:1995` · `AmbDashboardTradeDataSeriesResource`

### OPERATION-867 · 大使看板-邀请记录

- 接口声明：`GET /ambassador/dashboard/refer-history`
- 输入字段：`page`, `limit`, `code`, `keyword`, `start_date`, `end_date`, `export`, `source_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2045` · `AmbDashboardReferralHistoryResource`

### OPERATION-868 · 大使看板-返佣记录

- 接口声明：`GET /ambassador/dashboard/asset-history`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2274` · `AmbDashboardAssetHistoryResource`

### OPERATION-869 · 大使看板-返佣明细

- 接口声明：`GET /ambassador/dashboard/asset-detail`
- 输入字段：`report_type`, `start_date`, `end_date`, `keyword`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2380` · `AmbDashboardAssetDetailResource`

### OPERATION-870 · 大使看板-市场交易数据

- 接口声明：`GET /ambassador/dashboard/market-data`
- 输入字段：`time_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2527` · `AmbDashboardMarketDataResource`

### OPERATION-871 · 大使看板-代理-数据总览

- 接口声明：`GET /ambassador/dashboard/indirect-summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2579` · `AmbDashboardIndirectSummaryResource`

### OPERATION-872 · 大使看板-代理-周期内用户数据

- 接口声明：`GET /ambassador/dashboard/indirect-user-series`
- 输入字段：`time_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2593` · `AmbDashboardIndirectUserSeriesResource`

### OPERATION-873 · 大使看板-代理-周期内用户数据

- 接口声明：`GET /ambassador/dashboard/indirect-trade-series`
- 输入字段：`time_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2615` · `AmbDashboardIndirectTradeSeriesResource`

### OPERATION-874 · 大使看板-代理-返佣记录

- 接口声明：`GET /ambassador/dashboard/indirect-asset-history`
- 输入字段：`report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2637` · `AmbDashboardIndirectAssetHistoryResource`

### OPERATION-875 · 大使看板-代理-返佣明细

- 接口声明：`GET /ambassador/dashboard/indirect-asset-detail`
- 输入字段：`report_type`, `start_date`, `end_date`, `keyword`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2661` · `AmbDashboardIndirectAssetDetailResource`

### OPERATION-876 · 大使看板-代理列表（我的下级Tree大使列表）

- 接口声明：`GET /ambassador/dashboard/subordinates`
- 输入字段：`keyword`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2686` · `AmbDashboardChildTreeAmbListResource`

### OPERATION-877 · 大使看板-新增下级Tree大使

- 接口声明：`POST /ambassador/dashboard/subordinates`
- 输入字段：`account_name`, `referral_rate`, `remark`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/referral.py:2852` · `AmbDashboardChildTreeAmbListResource`

### OPERATION-878 · 大使看板-编辑下级Tree大使

- 接口声明：`PUT /ambassador/dashboard/subordinates/<account_name>`
- 输入字段：`referral_rate`, `remark`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2902` · `AmbDashboardChildTreeAmbDetailResource`

### OPERATION-879 · 大使激励包-列表

- 接口声明：`GET /ambassador/packages`
- 输入字段：`page`, `limit`, `status`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:2941` · `AmbassadorPackageResource`

### OPERATION-880 · 大使激励包-领取

- 接口声明：`POST /ambassador/package/<int:package_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:3048` · `AmbassadorPackageDetailResource`

### OPERATION-881 · 大使激励包-名称列表

- 接口声明：`GET /ambassador/package/settle-names`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:3094` · `AmbassadorPackageNamesResource`

### OPERATION-882 · 大使激励包-结算记录

- 接口声明：`GET /ambassador/package/settlement/records`
- 输入字段：`page`, `limit`, `name`, `start_time`, `end_time`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/referral.py:3141` · `AmbassadorPackageSettlementResource`

### OPERATION-883 · PushResource.post（用途待确认）

- 接口声明：`POST `
- 输入字段：`user_id`, `business`, `type`, `web_push_params`, `message_params`, `email_params`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/push.py:17` · `PushResource`

### OPERATION-884 · 学院-Wiki文章批量上传

- 接口声明：`POST /article/wiki-upload`
- 输入字段：`articles`
- 显式控制：require_api_auth
- 代码依据：`app/api/v1/operation.py:37` · `ArticleWikiAutoPublishResource`

### OPERATION-885 · BanterResource.get（用途待确认）

- 接口声明：`GET /banter/users`
- 输入字段：`email`, `page`, `limit`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/cooperation.py:36` · `BanterResource`

### OPERATION-886 · RefereeListResource.get（用途待确认）

- 接口声明：`GET /referee`
- 输入字段：`search`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/refer.py:104` · `RefereeListResource`

### OPERATION-887 · RefereeRebateRecordResource.get（用途待确认）

- 接口声明：`GET /referee-rebate/record`
- 输入字段：`start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/refer.py:369` · `RefereeRebateRecordResource`

### OPERATION-888 · RefereeRebateDetailResource.get（用途待确认）

- 接口声明：`GET /referee-rebate/detail`
- 输入字段：`search`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/refer.py:446` · `RefereeRebateDetailResource`

### OPERATION-889 · AgentRefereeListResource.get（用途待确认）

- 接口声明：`GET /agent-referee`
- 输入字段：`search`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/refer.py:544` · `AgentRefereeListResource`

### OPERATION-890 · AgentRebateRecordResource.get（用途待确认）

- 接口声明：`GET /agent-rebate/record`
- 输入字段：`start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/refer.py:738` · `AgentRebateRecordResource`

### OPERATION-891 · AgentRebateDetailResource.get（用途待确认）

- 接口声明：`GET /agent-rebate/detail`
- 输入字段：`search`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/refer.py:790` · `AgentRebateDetailResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/admin/operation/__init__.py`
- `tests/api/admin/operation/test_academy.py`
- `tests/api/admin/operation/test_app_push_test_resource.py`
- `tests/api/admin/operation/test_insight.py`
- `tests/api/admin/operation/test_name_block.py`
- `tests/api/admin/operation/test_push_inner_message_jump.py`
- `tests/api/admin/operation/test_reset_2fa.py`
- `tests/api/admin/operation/test_tip_bar.py`
- `tests/api/admin/test_notice.py`
- `tests/api/common/test_operation_token.py`
- `tests/api/frontend/test_activity.py`
- `tests/api/frontend/test_activity_party.py`
- `tests/api/frontend/test_message.py`
- `tests/api/frontend/test_operation.py`
- `tests/api/v2/test_permissions.py`
- `tests/business/activity/test_airdrop.py`
- `tests/business/activity/test_traffic.py`
- `tests/business/big_customer/test_message_translate.py`
- `tests/business/equity_center/test_inc_message.py`
- `tests/business/equity_center/test_notice_functions.py`
- `tests/business/mission_center/__init__.py`
- `tests/business/mission_center/test_group.py`
- `tests/business/mission_center/test_message_refactor.py`
- `tests/business/mission_center/test_mission.py`
- `tests/business/mission_center/test_utils.py`
- `tests/business/push/test_push.py`
- `tests/business/push/test_push_limit.py`
- `tests/business/test_app_push_delivery_statistics.py`
- `tests/business/test_push_statistic.py`
- `tests/business/test_push_statistic_batch_count.py`
- `tests/business/test_websocket_price_notice.py`
- `tests/caches/test_activity_popup_windows.py`
- `tests/caches/test_operation_message_push_content.py`
- `tests/schedules/test_app_push_content.py`
- `tests/schedules/test_app_push_inner_message_dependency.py`
- `tests/schedules/test_auto_push_notice.py`
- `tests/schedules/test_price_notice.py`
- `tests/test_app/test_coupon/test_coupon_message.py`
- `tests/test_app/test_templates/test_email/test_notice.py`
- `tests/test_app/test_templates/test_sms/test_notice.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
