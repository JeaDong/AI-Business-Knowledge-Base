# 账户与身份 · 接口需求清单

> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。
> 基线提交：`0ec2f7bd32aae6408fe11c867ab77106fc76a00b`

## 范围与验收方法

以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。
验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。

## 已声明能力

### ACCOUNT-001 · 特殊提现白名单列表

- 接口声明：`GET `
- 输入字段：`user`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_privileged_users.py:20` · `UsersResource`

### ACCOUNT-002 · 特殊提现白名单添加

- 接口声明：`POST `
- 输入字段：`user`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_privileged_users.py:55` · `UsersResource`

### ACCOUNT-003 · 特殊提现白名单编辑

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_privileged_users.py:106` · `UserResource`

### ACCOUNT-004 · 特殊提现白名单删除

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/asset/withdrawal_privileged_users.py:142` · `UserResource`

### ACCOUNT-005 · 系统-权限-管理员列表

- 接口声明：`GET /admin-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:48` · `AdminUserList`

### ACCOUNT-006 · 系统-权限-添加管理员

- 接口声明：`POST /admin-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:161` · `AdminUserList`

### ACCOUNT-007 · 系统-权限-编辑管理员

- 接口声明：`PUT /admin-users/<int:admin_record_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:214` · `EditAdminUser`

### ACCOUNT-008 · 系统-权限-删除通行密钥

- 接口声明：`PATCH /admin-users/<int:admin_record_id>`
- 输入字段：`webauthn_id`
- 显式控制：ns.use_kwargs(dict(webauthn_id=wa_fields.Integer(required=True)))
- 代码依据：`app/api/admin/auth.py:241` · `EditAdminUser`

### ACCOUNT-009 · 系统-权限-管理员角色列表

- 接口声明：`GET /admin-users/<int:admin_user_id>/roles`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:277` · `EditAdminUserRole`

### ACCOUNT-010 · 系统-权限-添加管理员角色

- 接口声明：`PUT /admin-users/<int:admin_user_id>/roles`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:291` · `EditAdminUserRole`

### ACCOUNT-011 · 系统-权限-角色列表

- 接口声明：`GET /roles`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:339` · `AdminRoleList`

### ACCOUNT-012 · 系统-权限-添加角色

- 接口声明：`POST /roles`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:388` · `AdminRoleList`

### ACCOUNT-013 · 系统-权限-克隆角色

- 接口声明：`PATCH /roles`
- 输入字段：`role_ids`, `name`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:413` · `AdminRoleList`

### ACCOUNT-014 · 系统-权限-修改角色

- 接口声明：`PUT /roles/<int:role_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:494` · `EditAdminRole`

### ACCOUNT-015 · 系统-权限-角色权限列表

- 接口声明：`GET /roles/<int:role_id>/permissions`
- 输入字段：`export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:536` · `EditAdminRolePermission`

### ACCOUNT-016 · 系统-权限-编辑角色

- 接口声明：`PUT /roles/<int:role_id>/permissions`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:586` · `EditAdminRolePermission`

### ACCOUNT-017 · 系统-权限-角色用户列表

- 接口声明：`GET /roles/<int:role_id>/users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:652` · `GetRoleUser`

### ACCOUNT-018 · 系统-权限-权限列表

- 接口声明：`GET /permissions`
- 输入字段：`keyword`, `status`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:695` · `AdminPermissionList`

### ACCOUNT-019 · 系统-权限-编辑权限

- 接口声明：`PUT /permissions/<int:permission_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:766` · `EditAdminPermission`

### ACCOUNT-020 · 系统-权限-权限所属角色

- 接口声明：`GET /permissions/<int:permission_id>/roles`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:795` · `AdminPermissionRoles`

### ACCOUNT-021 · EmailCodeResource.get（用途待确认）

- 接口声明：`GET /email/code`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:813` · `EmailCodeResource`

### ACCOUNT-022 · EmailCodeResource.post（用途待确认）

- 接口声明：`POST /email/code`
- 输入字段：`validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/auth.py:826` · `EmailCodeResource`

### ACCOUNT-023 · 登录

- 接口声明：`POST `
- 输入字段：`email`, `login_password`
- 显式控制：ns.use_kwargs(dict(email=EmailField(required=True), login_password=wa_fields.String(required=True)))
- 代码依据：`app/api/admin/login.py:38` · `UserLoginResource`

### ACCOUNT-024 · 登录-2FA

- 接口声明：`POST /2fa`
- 输入字段：`webauthn_token`
- 显式控制：ns.use_kwargs(dict(webauthn_token=wa_fields.String(required=True)))
- 代码依据：`app/api/admin/login.py:108` · `Login2FAResource`

### ACCOUNT-025 · 登出

- 接口声明：`POST /logout`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/login.py:144` · `LogoutResource`

### ACCOUNT-026 · WebAuthnRegistration.get（用途待确认）

- 接口声明：`GET /webauthn/registration`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/login.py:154` · `WebAuthnRegistration`

### ACCOUNT-027 · WebAuthnRegistration.post（用途待确认）

- 接口声明：`POST /webauthn/registration`
- 输入字段：`credential`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/login.py:174` · `WebAuthnRegistration`

### ACCOUNT-028 · 通行密钥鉴权

- 接口声明：`GET /webauthn/authentication`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/login.py:195` · `WebAuthnAuthentication`

### ACCOUNT-029 · WebAuthnAuthentication.post（用途待确认）

- 接口声明：`POST /webauthn/authentication`
- 输入字段：`credential`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/login.py:209` · `WebAuthnAuthentication`

### ACCOUNT-030 · 运营-用户标签-列表

- 接口声明：`GET /list`
- 输入字段：`tag`, `category_id`, `begin_at`, `end_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:44` · `UserTagListResource`

### ACCOUNT-031 · 运营-用户标签-详情

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:99` · `UserTagDetailResource`

### ACCOUNT-032 · 运营-用户标签-编辑

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`category_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:105` · `UserTagDetailResource`

### ACCOUNT-033 · 运营-用户标签-删除

- 接口声明：`DELETE /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:152` · `UserTagDetailResource`

### ACCOUNT-034 · 运营-用户标签-类别管理

- 接口声明：`GET /categories`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:180` · `UserTagCategoriesResource`

### ACCOUNT-035 · 运营-用户标签-类别管理-详情

- 接口声明：`GET /category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:235` · `UserTagCategoryDetailResource`

### ACCOUNT-036 · 运营-用户标签-类别管理-编辑/创建

- 接口声明：`PATCH /category/<int:id_>`
- 输入字段：`name`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:241` · `UserTagCategoryDetailResource`

### ACCOUNT-037 · 运营-用户标签-类别管理-删除

- 接口声明：`DELETE /category/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:292` · `UserTagCategoryDetailResource`

### ACCOUNT-038 · 运营-用户标签-分群列表

- 接口声明：`GET /group-list`
- 输入字段：`name`, `group_type`, `keyword`, `begin_at`, `end_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:330` · `UserTagGroupListResource`

### ACCOUNT-039 · 运营-用户标签-分群用户下载

- 接口声明：`GET /group/<int:id_>/user-download`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:402` · `UserTagGroupUserResource`

### ACCOUNT-040 · 运营-用户标签-分群详情

- 接口声明：`GET /group/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:453` · `UserTagGroupDetailResource`

### ACCOUNT-041 · 运营-用户标签-用户分群复制

- 接口声明：`POST /group/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:462` · `UserTagGroupDetailResource`

### ACCOUNT-042 · 运营-用户标签-分群编辑/创建

- 接口声明：`PATCH /group/<int:id_>`
- 输入字段：`name`, `group_type`, `rules`, `import_users`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:495` · `UserTagGroupDetailResource`

### ACCOUNT-043 · 运营-用户标签-分群删除

- 接口声明：`DELETE /group/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:645` · `UserTagGroupDetailResource`

### ACCOUNT-044 · 运营-用户标签-分群用户更新

- 接口声明：`PATCH /group/<int:id_>/refreshed`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:676` · `UserTagGroupRefreshResource`

### ACCOUNT-045 · 运营-用户标签-用户分群-多分群导入模板下载

- 接口声明：`GET /group/batch-template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:702` · `UserTagGroupBatchTemplateResource`

### ACCOUNT-046 · 运营-用户标签-用户分群-创建多条分群

- 接口声明：`POST /group/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:722` · `UserTagGroupBatchUploadResource`

### ACCOUNT-047 · 运营-用户标签-群体画像列表

- 接口声明：`GET /group-portraits`
- 输入字段：`name`, `keyword`, `begin_at`, `end_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:813` · `GroupPortraitsResource`

### ACCOUNT-048 · 运营-用户标签-群体画像详情

- 接口声明：`GET /group-portraits/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:873` · `GroupPortraitDetailResource`

### ACCOUNT-049 · 运营-用户标签-群体画像复制

- 接口声明：`POST /group-portraits/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:882` · `GroupPortraitDetailResource`

### ACCOUNT-050 · 运营-用户标签-群体画像编辑/创建

- 接口声明：`PATCH /group-portraits/<int:id_>`
- 输入字段：`name`, `tag_ids`, `tag_group_ids`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:906` · `GroupPortraitDetailResource`

### ACCOUNT-051 · 运营-用户标签-群体画像删除

- 接口声明：`DELETE /group-portraits/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:1054` · `GroupPortraitDetailResource`

### ACCOUNT-052 · 运营-用户标签-群体画像数据预览

- 接口声明：`GET /group-portraits/<int:id_>/preview`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:1085` · `GroupPortraitDataPreviewResource`

### ACCOUNT-053 · 运营-用户标签-群体画像数据下载-普通下载（包含邮箱）

- 接口声明：`GET /group-portraits/<int:id_>/downloads/sync-include-email`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:1106` · `GroupPortraitDataDownloadResource`

### ACCOUNT-054 · 运营-用户标签-群体画像数据下载-普通下载（无邮箱）

- 接口声明：`GET /group-portraits/<int:id_>/downloads/sync-exclude-email`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:1150` · `GroupPortraitDataDownloadExcludeEmailResource`

### ACCOUNT-055 · 运营-用户标签-群体画像数据下载-异步下载（包含邮箱）

- 接口声明：`GET /group-portraits/<int:id_>/downloads/async-include-email`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:1161` · `GroupPortraitDataAsyncDownloadResource`

### ACCOUNT-056 · 运营-用户标签-群体画像数据下载-异步下载（无邮箱）

- 接口声明：`GET /group-portraits/<int:id_>/downloads/async-exclude-email`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/operation/user_tag.py:1171` · `GroupPortraitDataAsyncDownloadExcludeEmailResource`

### ACCOUNT-057 · 报表-用户报表-KYC报表-总KYC报表

- 接口声明：`GET /summary`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kyc.py:191` · `KycSummaryReportResource`

### ACCOUNT-058 · 报表-用户报表-KYC报表-初级KYC报表

- 接口声明：`GET /basic`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kyc.py:203` · `KycBasicReportResource`

### ACCOUNT-059 · 报表-用户报表-KYC报表-高级KYC报表

- 接口声明：`GET /pro`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kyc.py:215` · `KycProReportResource`

### ACCOUNT-060 · 报表-用户报表-KYC报表-机构KYC报表

- 接口声明：`GET /institution`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/kyc.py:227` · `KycInstitutionReportResource`

### ACCOUNT-061 · 报表-用户报表

- 接口声明：`GET `
- 输入字段：`start_date`, `end_date`, `report_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:96` · `DailySpotDealsResource`

### ACCOUNT-062 · 报表-用户报表-用户分层报表

- 接口声明：`GET /hierarchical`
- 输入字段：`start_date`, `end_date`, `report_type`, `vip_level`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:203` · `UserHierarchicalReportResource`

### ACCOUNT-063 · 报表-用户报表-用户分层报表-异步下载

- 接口声明：`GET /hierarchical-async-download`
- 输入字段：`start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:250` · `UserHierarchicalReportAsyncDownloadResource`

### ACCOUNT-064 · 报表-用户报表-用户分层报表详情

- 接口声明：`GET /hierarchical/detail`
- 输入字段：`report_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:274` · `UserHierarchicalReportDetailResource`

### ACCOUNT-065 · 报表-国际化报表-国家分布报表 

- 接口声明：`GET /country-statistics`
- 输入字段：`sort_type`, `sort_name`, `report_type`, `area`, `query_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:349` · `CountryStatisticsResource`

### ACCOUNT-066 · 报表-国际化报表-国家分布报表-详情 

- 接口声明：`GET /country-statistics-detail`
- 输入字段：`report_type`, `country`, `start_date`, `end_date`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:607` · `CountryStatisticsDetailResource`

### ACCOUNT-067 · 报表-国际化报表-国家分布报表-报表曲线 

- 接口声明：`GET /country-series`
- 输入字段：`country`, `start_date`, `end_date`, `series_type`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:692` · `CountrySeriesResource`

### ACCOUNT-068 · 报表-国际化报表-地区分布报表 

- 接口声明：`GET /area-statistics`
- 输入字段：`sort_type`, `sort_name`, `report_type`, `area`, `query_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:782` · `AreaStatisticsResource`

### ACCOUNT-069 · 报表-国际化报表-地区分布报表-详情 

- 接口声明：`GET /area-statistics-detail`
- 输入字段：`report_type`, `area`, `start_date`, `end_date`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:1036` · `AreaStatisticsDetailResource`

### ACCOUNT-070 · 报表-国际化报表-地区分布报表-报表曲线 

- 接口声明：`GET /area-series`
- 输入字段：`area`, `start_date`, `end_date`, `series_type`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:1106` · `AreaSeriesResource`

### ACCOUNT-071 · 报表-国际化报表-语言分布报表 

- 接口声明：`GET /language-statistics`
- 输入字段：`sort_type`, `sort_name`, `query_date`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:1175` · `LanguageStatisticsResource`

### ACCOUNT-072 · 报表-国际化报表-语言分布报表-详情 

- 接口声明：`GET /language-statistics-detail`
- 输入字段：`report_type`, `language`, `start_date`, `end_date`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:1365` · `LanguageStatisticsDetailResource`

### ACCOUNT-073 · 报表-国际化报表-语言分布报表-报表曲线 

- 接口声明：`GET /language-series`
- 输入字段：`language`, `start_date`, `end_date`, `series_type`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:1450` · `LanguageSeriesResource`

### ACCOUNT-074 · 报表-国际化报表-地区交易分布报表

- 接口声明：`GET /area-trade-statistics`
- 输入字段：`report_type`, `report_date`, `start_date`, `end_date`, `from_detail`, `area`, `sort_name`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2037` · `AreaTradeStatisticsResource`

### ACCOUNT-075 · 报表-国际化报表-国家合约渗透

- 接口声明：`GET /country-perpetual-penetration`
- 输入字段：`report_date`, `area`, `period_days`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2081` · `CountryPerpetualPenetrationResource`

### ACCOUNT-076 · 报表-国际化报表-国家合约渗透-详情

- 接口声明：`GET /country-perpetual-penetration-detail`
- 输入字段：`country`, `period_days`, `start_date`, `end_date`, `sort_name`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2111` · `CountryPerpetualPenetrationDetailResource`

### ACCOUNT-077 · 报表-国际化报表-国家合约渗透-报表曲线

- 接口声明：`GET /country-perpetual-penetration-series`
- 输入字段：`country`, `period_days`, `start_date`, `end_date`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2157` · `CountryPerpetualPenetrationSeriesResource`

### ACCOUNT-078 · 报表-国际化报表-地区合约渗透

- 接口声明：`GET /area-perpetual-penetration`
- 输入字段：`report_date`, `area`, `period_days`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2187` · `AreaPerpetualPenetrationResource`

### ACCOUNT-079 · 报表-国际化报表-地区合约渗透-详情

- 接口声明：`GET /area-perpetual-penetration-detail`
- 输入字段：`area`, `period_days`, `start_date`, `end_date`, `sort_name`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2217` · `AreaPerpetualPenetrationDetailResource`

### ACCOUNT-080 · 报表-国际化报表-地区合约渗透-报表曲线

- 接口声明：`GET /area-perpetual-penetration-series`
- 输入字段：`area`, `period_days`, `start_date`, `end_date`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2262` · `AreaPerpetualPenetrationSeriesResource`

### ACCOUNT-081 · 报表-国际化报表-语言合约渗透

- 接口声明：`GET /language-perpetual-penetration`
- 输入字段：`report_date`, `period_days`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2285` · `LanguagePerpetualPenetrationResource`

### ACCOUNT-082 · 报表-国际化报表-语言合约渗透-详情

- 接口声明：`GET /language-perpetual-penetration-detail`
- 输入字段：`language`, `period_days`, `start_date`, `end_date`, `sort_name`, `sort_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2317` · `LanguagePerpetualPenetrationDetailResource`

### ACCOUNT-083 · 报表-国际化报表-语言合约渗透-报表曲线

- 接口声明：`GET /language-perpetual-penetration-series`
- 输入字段：`language`, `period_days`, `start_date`, `end_date`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2364` · `LanguagePerpetualPenetrationSeriesResource`

### ACCOUNT-084 · 报表-国际化报表-国家交易分布报表

- 接口声明：`GET /country-trade-statistics`
- 输入字段：`report_type`, `report_date`, `area`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2402` · `CountryTradeStatisticsResource`

### ACCOUNT-085 · 报表-国际化报表-国家交易分布报表-详情

- 接口声明：`GET /country-trade-statistics-detail`
- 输入字段：`report_type`, `country`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2456` · `CountryTradeStatisticsDetailResource`

### ACCOUNT-086 · 报表-国际化报表-国家交易分布报表-报表曲线

- 接口声明：`GET /country-trade-series`
- 输入字段：`country`, `start_date`, `end_date`, `series_type`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2513` · `CountryTradeSeriesResource`

### ACCOUNT-087 · 报表-国际化报表-语言交易分布报表

- 接口声明：`GET /language-trade-statistics`
- 输入字段：`report_type`, `report_date`, `sort_name`, `sort_type`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2594` · `LanguageTradeStatisticsResource`

### ACCOUNT-088 · 报表-国际化报表-语言交易分布报表-详情

- 接口声明：`GET /language-trade-statistics-detail`
- 输入字段：`report_type`, `language`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2658` · `LanguageTradeStatisticsDetailResource`

### ACCOUNT-089 · 报表-国际化报表-语言交易分布报表-报表曲线

- 接口声明：`GET /language-trade-series`
- 输入字段：`language`, `start_date`, `end_date`, `series_type`, `report_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2716` · `LanguageTradeSeriesResource`

### ACCOUNT-090 · 报表-用户报表-渠道漏斗报表 

- 接口声明：`GET /increase-channel`
- 输入字段：`start_date`, `end_date`, `channel_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2924` · `IncreaseChannelResource`

### ACCOUNT-091 · 报表-用户报表-渠道漏斗报表-异步下载 

- 接口声明：`GET /increase-channel-async-download`
- 输入字段：`start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:2979` · `IncreaseChannelAsyncDownloadResource`

### ACCOUNT-092 · 报表-用户报表-国家漏斗报表 

- 接口声明：`GET /increase-country`
- 输入字段：`start_date`, `end_date`, `country`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3029` · `IncreaseCountryResource`

### ACCOUNT-093 · 报表-用户报表-渠道漏斗报表详情 

- 接口声明：`GET /increase-channel-detail`
- 输入字段：`page`, `limit`, `export`, `report_date`, `order`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3108` · `IncreaseChannelDetailResource`

### ACCOUNT-094 · 报表-用户报表-国家漏斗报表详情 

- 接口声明：`GET /increase-country-detail`
- 输入字段：`page`, `limit`, `export`, `report_date`, `order`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3173` · `IncreaseCountryResourceDetail`

### ACCOUNT-095 · 报表-用户报表-宣发渠道漏斗报表 

- 接口声明：`GET /publicity-channel`
- 输入字段：`platform`, `start_date`, `end_date`, `publicity_channel`, `language_area`, `country`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3246` · `PublicityChannelUserResource`

### ACCOUNT-096 · 报表-用户报表-宣发渠道漏斗报表详情 

- 接口声明：`GET /publicity-channel-detail`
- 输入字段：`platform`, `publicity_channel`, `language_area`, `country`, `page`, `limit`, `export`, `start_date`, `end_date`, `order`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3372` · `PublicityChannelUserDetailResource`

### ACCOUNT-097 · 用户报表-留存报表-活跃留存

- 接口声明：`GET /active-retained`
- 输入字段：`report_type`, `start_date`, `end_date`, `origin_type`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3439` · `UserActiveRetainedReportResource`

### ACCOUNT-098 · 用户报表-留存报表-活跃留存-异步下载

- 接口声明：`GET /active-retained-async-download`
- 输入字段：`report_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3566` · `UserActiveRetainedReportAsyncDownloadResource`

### ACCOUNT-099 · 用户报表-留存报表-交易留存

- 接口声明：`GET /trade-retained`
- 输入字段：`report_type`, `start_date`, `end_date`, `trade_type`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:3593` · `UserTradeRetainedReportResource`

### ACCOUNT-100 · 报表-用户报表-宣发渠道统计报表

- 接口声明：`GET /publicity-channel-statistics`
- 输入字段：`start_date`, `end_date`, `report_type`, `language_area`, `period`, `country`, `publicity_channel_id`, `publicity_channel`, `short_link_id`, `export`, `business_segment`, `category_id`, `cursor`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4068` · `PublicityChannelStatisticResource`

### ACCOUNT-101 · 报表-用户报表-宣发渠道统计报表-报表曲线

- 接口声明：`GET /publicity-channel-series`
- 输入字段：`start_date`, `end_date`, `report_type`, `series_type`, `language_area`, `period`, `country`, `publicity_channel_id`, `publicity_channel`, `short_link_id`, `business_segment`, `category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4190` · `PublicityChannelSeriesResource`

### ACCOUNT-102 · 报表-用户报表-宣发渠道统计详情

- 接口声明：`GET /publicity-channel-statistics-detail`
- 输入字段：`report_date`, `report_type`, `period`, `sort_type`, `language_area`, `country`, `publicity_channel_id`, `publicity_channel`, `export`, `page`, `limit`, `business_segment`, `category_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4285` · `PublicityChannelDetailResource`

### ACCOUNT-103 · 报表-用户报表-App宣发渠道统计报表

- 接口声明：`GET /app-publicity-channel-statistics`
- 输入字段：`start_date`, `end_date`, `report_type`, `language_area`, `period`, `country`, `channel`, `platform`, `export`, `cursor`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4499` · `AppPublicityChannelStatisticResource`

### ACCOUNT-104 · 报表-用户报表-App宣发渠道统计报表-报表曲线

- 接口声明：`GET /app-publicity-channel-series`
- 输入字段：`start_date`, `end_date`, `report_type`, `series_type`, `language_area`, `period`, `platform`, `country`, `channel`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4594` · `AppPublicityChannelSeriesResource`

### ACCOUNT-105 · 报表-用户报表-App宣发渠道统计详情

- 接口声明：`GET /app-publicity-channel-statistics-detail`
- 输入字段：`report_date`, `report_type`, `period`, `sort_type`, `language_area`, `country`, `channel`, `platform`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4657` · `AppPublicityChannelDetailResource`

### ACCOUNT-106 · 报表-国家报表-语区留存报表

- 接口声明：`GET /language-area-user-active-retain`
- 输入字段：`sort_name`, `query_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4823` · `LanguageAreaUserActiveRetainResource`

### ACCOUNT-107 · 报表-国家报表-语区留存报表详情

- 接口声明：`GET /language-area-user-active-retain-detail`
- 输入字段：`language_area`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4869` · `LanguageAreaUserActiveRetainDetailResource`

### ACCOUNT-108 · 报表-国家报表-语区留存报表-报表曲线

- 接口声明：`GET /language-area-user-active-retain-series`
- 输入字段：`language_area`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4925` · `LanguageAreaUserActiveRetainSeriesResource`

### ACCOUNT-109 · 报表-国家报表-国家留存报表

- 接口声明：`GET /country-user-active-retain`
- 输入字段：`sort_name`, `query_date`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:4989` · `CountryUserActiveRetainResource`

### ACCOUNT-110 · 报表-国家报表-国家留存报表详情

- 接口声明：`GET /country-user-active-retain-detail`
- 输入字段：`country`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:5028` · `CountryUserActiveRetainDetailResource`

### ACCOUNT-111 · 报表-国家报表-国家留存报表-报表曲线

- 接口声明：`GET /country-user-active-retain-series`
- 输入字段：`country`, `series_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:5074` · `CountryUserActiveRetainSeriesResource`

### ACCOUNT-112 · 报表-流失报表

- 接口声明：`GET /loss-user`
- 输入字段：`type`, `report_type`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:5146` · `LossUserReportResource`

### ACCOUNT-113 · 报表-用户报表-VIP报表

- 接口声明：`GET /vip-report`
- 输入字段：`start_date`, `end_date`, `report_type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/report/user.py:5211` · `VipReportResource`

### ACCOUNT-114 · 用户-子账户列表

- 接口声明：`GET `
- 输入字段：`main_user_id`, `manage_user_id`, `status`, `manage_status`, `type`, `is_visible`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/sub_accounts.py:41` · `SubAccountsResource`

### ACCOUNT-115 · 用户-子账户-编辑

- 接口声明：`PUT `
- 输入字段：`sub_account_id`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/sub_accounts.py:187` · `SubAccountsResource`

### ACCOUNT-116 · 用户-特殊配置-子账号上限配置列表 

- 接口声明：`GET /limit-config`
- 输入字段：`user_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/sub_accounts.py:215` · `SubAccountLimitResource`

### ACCOUNT-117 · 用户-特殊配置-子账号上限配置-新增 

- 接口声明：`POST /limit-config`
- 输入字段：`user_id`, `limit_num`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/sub_accounts.py:247` · `SubAccountLimitResource`

### ACCOUNT-118 · 用户-特殊配置-子账号上限配置-编辑 

- 接口声明：`PUT /limit-config`
- 输入字段：`user_id`, `limit_num`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/sub_accounts.py:292` · `SubAccountLimitResource`

### ACCOUNT-119 · 用户-特殊配置-子账号上限配置-删除 

- 接口声明：`DELETE /limit-config`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/sub_accounts.py:346` · `SubAccountLimitResource`

### ACCOUNT-120 · 用户-子账户列表-更新是否禁用 

- 接口声明：`POST /update-visible`
- 输入字段：`sub_user_id`, `is_visible`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/sub_accounts.py:385` · `SubAccountUpdateVisibleResource`

### ACCOUNT-121 · 用户设置

- 接口声明：`GET /<field>`
- 输入字段：`user`, `order_by`, `show_expired`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user-settings.py:29` · `FieldResource`

### ACCOUNT-122 · 运营-内容模块-用户教育-用户教育列表

- 接口声明：`GET /list`
- 输入字段：`platform`, `path`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:86` · `UserEducationListResource`

### ACCOUNT-123 · 运营-内容模块-用户教育-用户教育配置详情

- 接口声明：`GET /`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:145` · `UserEducationResource`

### ACCOUNT-124 · 运营-内容模块-用户教育-创建/修改用户教育配置

- 接口声明：`POST /`
- 输入字段：`id`, `platform`, `path`, `desc`, `contents`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:192` · `UserEducationResource`

### ACCOUNT-125 · 运营-内容模块-用户教育-启用用户教育

- 接口声明：`PUT /`
- 输入字段：`id`, `active`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:336` · `UserEducationResource`

### ACCOUNT-126 · 运营-内容模块-用户教育-删除用户教育

- 接口声明：`DELETE /`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:416` · `UserEducationResource`

### ACCOUNT-127 · 运营-内容模块-用户教育-获取启用的用户教育配置ID

- 接口声明：`GET /active`
- 输入字段：`platform`, `path`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:442` · `UserEducationActiveResource`

### ACCOUNT-128 · 运营-内容模块-用户教育-用户教育模版

- 接口声明：`GET /batch-upload/template`
- 输入字段：`content_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:515` · `BatchUploadTemplateResource`

### ACCOUNT-129 · 运营-内容模块-用户教育-校验视频链接

- 接口声明：`POST /video/check`
- 输入字段：`urls`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:552` · `VideoCheckResource`

### ACCOUNT-130 · 运营-内容模块-用户教育-校验文章链接

- 接口声明：`POST /articles/check`
- 输入字段：`urls`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/user_education.py:588` · `ArticleCheckResource`

### ACCOUNT-131 · UserMyInfoResource.get（用途待确认）

- 接口声明：`GET /my-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:221` · `UserMyInfoResource`

### ACCOUNT-132 · UserCommonResource.get（用途待确认）

- 接口声明：`GET /common`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:234` · `UserCommonResource`

### ACCOUNT-133 · 用户列表

- 接口声明：`GET `
- 输入字段：`user_type`, `keyword`, `location_code`, `channel`, `start_time`, `end_time`, `vip_level`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:250` · `UsersResource`

### ACCOUNT-134 · 用户搜索（用户详情）

- 接口声明：`GET /permission-required-search`
- 输入字段：`user_type`, `keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:400` · `PermissionRequiredUserSearchResource`

### ACCOUNT-135 · 用户搜索

- 接口声明：`GET /search`
- 输入字段：`user_type`, `keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:414` · `UserSearchResource`

### ACCOUNT-136 · 用户-基本信息

- 接口声明：`GET /<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:474` · `UserBasicsResource`

### ACCOUNT-137 · 用户-基本信息修改

- 接口声明：`PATCH /<int:id_>`
- 输入字段：`kyc_status`, `kyc_pro_status`, `kyc_name`, `telegram`, `reset_withdraw_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:489` · `UserBasicsResource`

### ACCOUNT-138 · 用户详情-查看敏感信息

- 接口声明：`POST /<int:id_>/sensitive-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1094` · `UserSensitiveInfoResource`

### ACCOUNT-139 · 用户-手机号修改

- 接口声明：`PATCH /<int:id_>/mobile`
- 输入字段：`mobile`, `mobile_country_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1105` · `UserMobileResource`

### ACCOUNT-140 · 用户-邮箱修改

- 接口声明：`PATCH /<int:id_>/email`
- 输入字段：`email`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1164` · `UserEmailResource`

### ACCOUNT-141 · 用户-邮箱修改审核

- 接口声明：`PUT /<int:id_>/email`
- 输入字段：`email`, `status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1198` · `UserEmailResource`

### ACCOUNT-142 · 用户-解绑TOTP

- 接口声明：`DELETE /<int:id_>/totp`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1273` · `UserTotpResource`

### ACCOUNT-143 · 用户-解绑通行密钥

- 接口声明：`DELETE /<int:id_>/webauthn`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1300` · `UserWebauthnResource`

### ACCOUNT-144 · 用户-备注修改

- 接口声明：`PATCH /<int:id_>/remark`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1325` · `UserRemarkResource`

### ACCOUNT-145 · 用户-删除提现审核人

- 接口声明：`DELETE /<int:id_>/withdrawal-approvers`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1350` · `UserWithdrawalApproversResource`

### ACCOUNT-146 · 用户详情-提现多人审核-删除提现地址

- 接口声明：`PUT /<int:id_>/withdrawal-approvals-delete`
- 输入字段：`accounts`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1390` · `WithdrawalApprovalsDeleteResource`

### ACCOUNT-147 · 用户详情-审核删除多人提现地址-审核通过

- 接口声明：`PUT /<int:id_>/withdrawal-approval-audit/pass`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1426` · `WithdrawalApprovalAuditPassResource`

### ACCOUNT-148 · 用户详情-审核删除多人提现地址-审核拒绝

- 接口声明：`PUT /<int:id_>/withdrawal-approval-audit/reject`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1481` · `WithdrawalApprovalAuditRejectResource`

### ACCOUNT-149 · 用户-重置用户头像

- 接口声明：`PATCH /<int:id_>/avatar`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1512` · `UserResetAvatarResource`

### ACCOUNT-150 · 用户-头像信息列表

- 接口声明：`GET /avatars`
- 输入字段：`user_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1536` · `UserAvatarListResource`

### ACCOUNT-151 · 用户详情-设置列表

- 接口声明：`GET /<int:id_>/settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1568` · `UserSettingFieldResource`

### ACCOUNT-152 · 用户详情-设置修改

- 接口声明：`PUT /<int:id_>/settings/<field>`
- 输入字段：`value`, `valid_from`, `valid_till`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1588` · `UserSettingFieldResource`

### ACCOUNT-153 · 用户详情-设置删除

- 接口声明：`DELETE /<int:id_>/settings/<field>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1642` · `UserSettingFieldResource`

### ACCOUNT-154 · 用户-特殊配置-提现额度配置

- 接口声明：`PUT /<int:id_>/withdrawal-limit`
- 输入字段：`daily_withdrawal_limit`, `withdrawal_limit_30_days`, `valid_till`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1724` · `UserWithdrawalLimitResource`

### ACCOUNT-155 · 用户-特殊配置-删除提现额度配置

- 接口声明：`DELETE /<int:id_>/withdrawal-limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1788` · `UserWithdrawalLimitResource`

### ACCOUNT-156 · 用户-特殊配置-提现额度配置列表

- 接口声明：`GET /sp-config/withdrawal-limit`
- 输入字段：`user`, `page`, `limit`, `active_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1822` · `UserWithdrawalLimitSpecialConfigResource`

### ACCOUNT-157 · 用户详情-获取实际国家列表

- 接口声明：`GET /<int:id_>/real_country_code`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1930` · `UserRealCountryCodeResource`

### ACCOUNT-158 · 用户详情-修改实际国家

- 接口声明：`PUT /<int:id_>/real_country_code`
- 输入字段：`value`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1936` · `UserRealCountryCodeResource`

### ACCOUNT-159 · 用户详情-偏好修改

- 接口声明：`PUT /<int:id_>/preferences/<field>`
- 输入字段：`value`, `valid_from`, `valid_till`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:1979` · `UserPreferenceFieldResource`

### ACCOUNT-160 · 用户详情-现货账户-现货资产

- 接口声明：`GET /<int:id_>/spot-assets`
- 输入字段：`filter_small_assets`, `hide_deposit_withdrawal`, `hide_offline_assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2036` · `UserSpotInfoResource`

### ACCOUNT-161 · 用户详情-资产总览-资产总览

- 接口声明：`GET /<int:id_>/spot-assets-preview`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2115` · `UserSpotAssetPreviewResource`

### ACCOUNT-162 · 用户详情-现货账户-充值记录

- 接口声明：`GET /<int:id_>/spot-deposits`
- 输入字段：`asset`, `chain`, `type`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2220` · `UserSpotDepositsResource`

### ACCOUNT-163 · 用户详情-现货账户-提现记录

- 接口声明：`GET /<int:id_>/spot-withdrawals`
- 输入字段：`asset`, `chain`, `type`, `start`, `end`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2308` · `UserSpotWithdrawalsResource`

### ACCOUNT-164 · 用户详情-现货账户-划转记录

- 接口声明：`GET /<int:id_>/spot-balance-history`
- 输入字段：`asset`, `account_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2388` · `UserSpotBalanceHistoryResource`

### ACCOUNT-165 · 用户详情-永续信息

- 接口声明：`GET /<int:id_>/perpetual-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2459` · `UserPerpetualInfoResource`

### ACCOUNT-166 · 用户详情-永续-当前持仓信息

- 接口声明：`GET /<int:id_>/current-position`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2621` · `UserPerpetualPositionResource`

### ACCOUNT-167 · 用户详情-永续-当前持仓-一键平仓(市价)

- 接口声明：`DELETE /<int:id_>/current-position`
- 输入字段：`market`, `position_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2664` · `UserPerpetualPositionResource`

### ACCOUNT-168 · 用户详情-永续-历史仓位

- 接口声明：`GET /<int:id_>/history-position`
- 输入字段：`market`, `page`, `limit`, `start_time`, `end_time`, `export`, `finish_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2786` · `UserHistoryPositionResource`

### ACCOUNT-169 · 用户详情-永续-仓位明细-导出

- 接口声明：`GET /<int:id_>/position-detail-export`
- 输入字段：`position_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:2894` · `PositionDetailExportResource`

### ACCOUNT-170 · 用户详情-永续-仓位明细-加减仓

- 接口声明：`GET /<int:id_>/position-deal-detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3151` · `PositionDealDetailResource`

### ACCOUNT-171 · 用户详情-永续-仓位明细-追加/减少保证金

- 接口声明：`GET /<int:id_>/position-margin-detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3204` · `PositionMarginResource`

### ACCOUNT-172 · 用户详情-永续-仓位明细-结算记录

- 接口声明：`GET /<int:id_>/position-settle-detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3238` · `SettleDetailResource`

### ACCOUNT-173 · 用户详情-永续-仓位明细-资金费用

- 接口声明：`GET /<int:id_>/position-funding-detail`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3271` · `FundingDetailResource`

### ACCOUNT-174 · 用户详情-永续-仓位明细-止盈止损

- 接口声明：`GET /<int:id_>/position-stop-loss-take-profit-history`
- 输入字段：`position_id`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3299` · `PositionStopLossTakeProfitHistoryResource`

### ACCOUNT-175 · 用户详情-永续-当前委托

- 接口声明：`GET /<int:id_>/perpetual-pending-orders`
- 输入字段：`type`, `market`, `side`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3370` · `UserPerpetualPendingOrderResource`

### ACCOUNT-176 · 用户详情-永续-撤销订单

- 接口声明：`DELETE /<int:id_>/perpetual-pending-orders`
- 输入字段：`type`, `market`, `order_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3410` · `UserPerpetualPendingOrderResource`

### ACCOUNT-177 · 用户详情-永续-批量撤销订单

- 接口声明：`DELETE /<int:id_>/perpetual-pending-orders/batch`
- 输入字段：`type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3444` · `UserPerpetualPendingOrderBatchDeleteResource`

### ACCOUNT-178 · 用户详情-永续-历史普通委托

- 接口声明：`GET /<int:id_>/perpetual-history-orders`
- 输入字段：`market`, `side`, `page`, `limit`, `start_time`, `end_time`, `stop_order_id`, `order_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3526` · `UserPerpetualFinishedOrderResource`

### ACCOUNT-179 · 用户详情-永续-盈亏统计

- 接口声明：`GET /<int:id_>/perpetual-position-profit`
- 输入字段：`start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3638` · `UserPerpetualPositionProfitResource`

### ACCOUNT-180 · 用户详情-永续-历史计划委托

- 接口声明：`GET /<int:id_>/perpetual-history-stop-orders`
- 输入字段：`market`, `page`, `limit`, `side`, `status`, `start_time`, `end_time`, `order_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3813` · `UserPerpetualHistoryStopOrderResource`

### ACCOUNT-181 · 用户详情-充值信息

- 接口声明：`GET /<int:id_>/deposit-info`
- 输入字段：`chain`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3939` · `UserDepositInfoResource`

### ACCOUNT-182 · 用户详情-提现信息

- 接口声明：`GET /<int:id_>/withdrawal-info`
- 输入字段：`chain`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:3998` · `UserWithdrawalInfoResource`

### ACCOUNT-183 · 用户详情-操作记录

- 接口声明：`GET /<int:id_>/operation-logs`
- 输入字段：`hide_login_extension`, `started_at`, `ended_at`, `operation_type`, `page`, `limit`
- 显式控制：ns.use_kwargs(dict(hide_login_extension=fields.Boolean(load_default=True), started_at=TimestampField, ended_at=TimestampField, operation_type=fields.String(), page=ex_fields.PageFi
- 代码依据：`app/api/admin/users.py:4059` · `UserOperationLogsResource`

### ACCOUNT-184 · 用户详情-休眠自动平仓操作记录：时间、操作

- 接口声明：`GET /<int:id_>/perpetual-dormancy-operation-logs`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4130` · `PerpetualDormancyOperationLogsResource`

### ACCOUNT-185 · 用户详情-客服记录

- 接口声明：`GET /<int:id_>/admin-operation-logs`
- 输入字段：`op_type`, `started_at`, `ended_at`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4157` · `AdminOperationLogsResource`

### ACCOUNT-186 · 用户详情-登录记录

- 接口声明：`GET /<int:id_>/login-history`
- 输入字段：`page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4238` · `UserLoginHistoryResource`

### ACCOUNT-187 · 用户详情-子账号

- 接口声明：`GET /<int:id_>/sub_accounts`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4330` · `UserSubAccountsResource`

### ACCOUNT-188 · 用户详情-杠杆资产

- 接口声明：`GET /<int:id_>/assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4349` · `UserAssetsResource`

### ACCOUNT-189 · 用户详情-借币权限配置

- 接口声明：`PATCH /<int:id_>/assets`
- 输入字段：`can_loan`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4402` · `UserAssetsResource`

### ACCOUNT-190 · 用户详情-币币订单

- 接口声明：`GET /<int:id_>/deals`
- 输入字段：`market`, `market_type`, `side`, `page`, `limit`, `start_time`, `end_time`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4456` · `UserDealsResource`

### ACCOUNT-191 · 用户详情-永续成交记录

- 接口声明：`GET /<int:id_>/contract-deals`
- 输入字段：`market`, `side`, `page`, `limit`, `start_time`, `end_time`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4555` · `ContractDealsResource`

### ACCOUNT-192 · 用户详情-永续资金费用

- 接口声明：`GET /<int:id_>/contract-funding`
- 输入字段：`market`, `page`, `limit`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4661` · `ContractFundingResource`

### ACCOUNT-193 · 用户详情-币币成交统计

- 接口声明：`GET /<int:id_>/statistic`
- 输入字段：`coin_type`, `market_type`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4739` · `StatisticResource`

### ACCOUNT-194 · 用户详情-永续成交统计

- 接口声明：`GET /<int:id_>/perpetual-statistic`
- 输入字段：`asset`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4866` · `PerpetualStatisticResource`

### ACCOUNT-195 · 用户详情-资金流水

- 接口声明：`GET /<int:id_>/balance-history`
- 输入字段：`market`, `market_type`, `pledge_account_id`, `asset`, `business`, `sub_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:4939` · `BalanceHistoryResource`

### ACCOUNT-196 · 用户详情-报税数据导出

- 接口声明：`GET /<int:id_>/tax-history-export`
- 输入字段：`start_time`, `end_time`, `asset`, `hide_transfer`, `account`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5147` · `TaxHistoryExportResource`

### ACCOUNT-197 · 用户详情-报税数据导出历史

- 接口声明：`GET /<int:id_>/tax/export/history`
- 输入字段：`page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5197` · `TaxExportHistoryResource`

### ACCOUNT-198 · 用户详情-理财资产

- 接口声明：`GET /<int:id_>/invest-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5248` · `InvestHistoryResource`

### ACCOUNT-199 · 用户详情-定期理财资产

- 接口声明：`GET /<int:id_>/fixed-invest-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5293` · `UserFixedInvestAssetResource`

### ACCOUNT-200 · 用户详情-双币理财资产

- 接口声明：`GET /<int:id_>/dual-invest-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5355` · `UserDualInvestAssetResource`

### ACCOUNT-201 · 用户详情-链上质押资产

- 接口声明：`GET /<int:id_>/staking-assets`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5402` · `StakingAssetResource`

### ACCOUNT-202 · 用户详情-币币-计划委托

- 接口声明：`GET /<int:id_>/stop-orders`
- 输入字段：`market`, `side`, `page`, `limit`, `account_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5469` · `UserStopOrderResource`

### ACCOUNT-203 · 用户详情-币币-当前委托

- 接口声明：`GET /<int:id_>/pending-orders`
- 输入字段：`market`, `side`, `page`, `limit`, `account_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5541` · `UserPendingOrderResource`

### ACCOUNT-204 · 用户详情-币币-撤销普通委托

- 接口声明：`DELETE /<int:id_>/pending-orders/<int:order_id>`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5584` · `UserPendingOrderDeleteResource`

### ACCOUNT-205 · 用户详情-币币-撤销计划委托

- 接口声明：`DELETE /<int:id_>/stop-orders/<int:order_id>`
- 输入字段：`market`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5608` · `UserStopOrderDeleteResource`

### ACCOUNT-206 · 用户详情-币币-批量撤销计划委托单

- 接口声明：`DELETE /<int:id_>/stop-orders/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5630` · `UserStopOrderBatchDeleteResource`

### ACCOUNT-207 · 用户详情-币币-批量撤销普通委托单

- 接口声明：`DELETE /<int:id_>/pending-orders/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5645` · `UserPendingOrderBatchDeleteResource`

### ACCOUNT-208 · 用户详情-币币-历史委托

- 接口声明：`GET /<int:id_>/pending-history-orders`
- 输入字段：`market`, `page`, `side`, `limit`, `start_time`, `end_time`, `account_id`, `order_id`, `stop_order_id`, `margin_liquidation_history_id`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5783` · `UserPendingHistoryOrderResource`

### ACCOUNT-209 · 用户详情-币币-订单明细

- 接口声明：`GET /<int:id_>/order-detail/<int:order_id>`
- 输入字段：`market`, `market_type`, `limit`, `page`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:5898` · `UserOrderDetailResource`

### ACCOUNT-210 · 用户详情-币币-历史计划委托

- 接口声明：`GET /<int:id_>/stop-history-orders`
- 输入字段：`market`, `page`, `limit`, `start_time`, `end_time`, `account_id`, `side`, `order_id`, `status`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6058` · `UserStopHistoryOrderResource`

### ACCOUNT-211 · 用户详情-用户等级

- 接口声明：`GET /user-level/`
- 输入字段：`id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6151` · `UserLevelResource`

### ACCOUNT-212 · 用户详情-修改账号类型

- 接口声明：`POST /user-type`
- 输入字段：`user_id`, `user_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6349` · `UserTypeResource`

### ACCOUNT-213 · 用户详情-杠杆日息

- 接口声明：`POST /margin-day-rate`
- 输入字段：`user_id`, `day_rate`, `expired_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6482` · `UserMarginDayRateResource`

### ACCOUNT-214 · 邀请列表

- 接口声明：`GET /referral`
- 输入字段：`user_id`, `export`, `referral_code`, `page`, `status`, `limit`, `start_date`, `end_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6556` · `ReferralResource`

### ACCOUNT-215 · 邀请码列表

- 接口声明：`GET /referral-codes`
- 输入字段：`user_id`, `referral_code`, `type`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6727` · `ReferralCodesResource`

### ACCOUNT-216 · 用户详情-资产锁定-列表

- 接口声明：`GET /<int:id_>/asset-lock`
- 输入字段：`asset`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6819` · `UserAssetLockResource`

### ACCOUNT-217 · 用户详情-资产锁定

- 接口声明：`POST /<int:id_>/asset-lock`
- 输入字段：`asset`, `amount`, `remark`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/users.py:6845` · `UserAssetLockResource`

### ACCOUNT-218 · 用户详情-资产解锁

- 接口声明：`PUT /<int:id_>/asset-lock`
- 输入字段：`business_ids`, `remark`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/users.py:6877` · `UserAssetLockResource`

### ACCOUNT-219 · 用户详情-资产变更

- 接口声明：`POST /<int:id_>/asset-update`
- 输入字段：`asset`, `amount`, `remark`, `type`
- 显式控制：require_admin_webauth_token
- 代码依据：`app/api/admin/users.py:6912` · `UserAssetUpdateResource`

### ACCOUNT-220 · 用户详情-资产持仓历史

- 接口声明：`GET /<int:user_id>/asset-series`
- 输入字段：`account_type`, `asset`, `market`, `start_date`, `end_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:6981` · `AssetSeriesResource`

### ACCOUNT-221 · 用户详情-总资产持仓历史

- 接口声明：`GET /<int:user_id>/asset-sum-series`
- 输入字段：`account_type`, `start_date`, `end_date`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7026` · `AssetSumSeriesResource`

### ACCOUNT-222 · 用户详情-做市账户

- 接口声明：`GET /<int:user_id>/amm-market`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7102` · `AmmMarketResource`

### ACCOUNT-223 · 用户详情-AMM收益记录

- 接口声明：`GET /<int:user_id>/amm-incomes`
- 输入字段：`market`, `start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7125` · `AmmIncomeHistoryResource`

### ACCOUNT-224 · 用户详情-AMM全部收益记录

- 接口声明：`GET /<int:user_id>/all-amm-incomes`
- 输入字段：`start_date`, `end_date`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7219` · `AllAmmIncomeHistoryResource`

### ACCOUNT-225 · 用户->API用户列表 

- 接口声明：`GET /auth-api`
- 输入字段：`user_id`, `withdrawals_enabled`, `trading_enabled`, `expire_status`, `disabled_status`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7248` · `UserAuthAPIResource`

### ACCOUNT-226 · 用户->API用户列表->恢复/禁用 

- 接口声明：`PATCH /auth-api/<int:id_>`
- 输入字段：`disabled_status`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7373` · `UserAuthAPIDetailResource`

### ACCOUNT-227 · 用户->API用户列表->删除 

- 接口声明：`DELETE /auth-api/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7401` · `UserAuthAPIDetailResource`

### ACCOUNT-228 · 用户-API-提现白名单列表

- 接口声明：`GET /withdrawal-whitelist`
- 输入字段：`user_id`, `chain`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7433` · `APIUsersResource`

### ACCOUNT-229 · 用户-API-现货交易用户白名单列表

- 接口声明：`GET /spot-trading-whitelist`
- 输入字段：`user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7495` · `APISpotTradingWhiteListResource`

### ACCOUNT-230 · 用户-API-新建现货交易用户白名单

- 接口声明：`POST /spot-trading-whitelist`
- 输入字段：`user_id`, `markets`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7548` · `APISpotTradingWhiteListResource`

### ACCOUNT-231 · 用户-API-修改现货交易用户白名单

- 接口声明：`PUT /spot-trading-whitelist/<int:id_>`
- 输入字段：`markets`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7605` · `APISpotTradingWhiteListDetailResource`

### ACCOUNT-232 · 用户-API-删除现货交易用户白名单

- 接口声明：`DELETE /spot-trading-whitelist/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7648` · `APISpotTradingWhiteListDetailResource`

### ACCOUNT-233 · 用户-API-合约交易用户白名单列表

- 接口声明：`GET /perpetual-trading-whitelist`
- 输入字段：`user_id`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7681` · `APIPerpetualTradingWhiteListResource`

### ACCOUNT-234 · 用户-API-新建合约交易用户白名单

- 接口声明：`POST /perpetual-trading-whitelist`
- 输入字段：`user_id`, `markets`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7734` · `APIPerpetualTradingWhiteListResource`

### ACCOUNT-235 · 用户-API-修改合约交易用户白名单

- 接口声明：`PUT /perpetual-trading-whitelist/<int:id_>`
- 输入字段：`markets`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7791` · `APIPerpetualTradingWhiteListDetailResource`

### ACCOUNT-236 · 用户-API-删除合约交易用户白名单

- 接口声明：`DELETE /perpetual-trading-whitelist/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7834` · `APIPerpetualTradingWhiteListDetailResource`

### ACCOUNT-237 · 用户-用户组配置

- 接口声明：`GET /user-groups`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7859` · `CouponUserGroupConfigResource`

### ACCOUNT-238 · 用户-清退用户列表

- 接口声明：`GET /cleared-users`
- 输入字段：`user_id`, `operator`, `status`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7869` · `ClearedUsersResource`

### ACCOUNT-239 · 用户-新增清退用户

- 接口声明：`POST /cleared-users`
- 输入字段：`user_id`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:7964` · `ClearedUsersResource`

### ACCOUNT-240 · 用户-修改清退用户

- 接口声明：`PATCH /cleared-users`
- 输入字段：`user_ids`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8021` · `ClearedUsersResource`

### ACCOUNT-241 · 用户-删除清退用户

- 接口声明：`DELETE /cleared-users`
- 输入字段：`user_ids`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8100` · `ClearedUsersResource`

### ACCOUNT-242 · 用户-清退用户批量上传

- 接口声明：`POST /cleared-users/batch-upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8167` · `ClearedUsersBatchUploadResource`

### ACCOUNT-243 · 用户-注销用户列表

- 接口声明：`GET /sign-off-users`
- 输入字段：`user`, `start_time`, `end_time`, `page`, `limit`, `with_assets`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8300` · `UserSignOffHistoryResource`

### ACCOUNT-244 · 用户-IP/设备ID/提现地址查询

- 接口声明：`GET /relations`
- 输入字段：`user_id`, `start_time`, `end_time`, `withdrawal_address`, `device_id`, `ip`, `location_code`, `language`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8595` · `UserRelationListResource`

### ACCOUNT-245 · 用户-IP/设备ID/提现地址-批量查询

- 接口声明：`POST /relations`
- 输入字段：`batch_user_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8682` · `UserRelationListResource`

### ACCOUNT-246 · 用户-IP/设备ID/提现地址查询（当天）

- 接口声明：`GET /relations-1day`
- 输入字段：`user_id`, `start_time`, `end_time`, `location_code`, `withdrawal_address`, `device_id`, `ip`, `language`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8710` · `UserRelation1dayListResource`

### ACCOUNT-247 · 用户-IP/设备ID/提现地址-异步导出模板下载

- 接口声明：`GET /relations/async-export/template`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8752` · `UserRelationAsyncExportTemplateResource`

### ACCOUNT-248 · 用户-IP/设备ID/提现地址-异步导出

- 接口声明：`POST /relations/async-export`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:8828` · `UserRelationAsyncExportResource`

### ACCOUNT-249 · 用户-关联用户详情

- 接口声明：`GET /relation/detail`
- 输入字段：`user_id`, `batch_user_ids`, `search_user_id`, `relation_type`, `sort_type`, `start_time`, `end_time`, `has_remark`, `export`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9078` · `UserRelationDetailResource`

### ACCOUNT-250 · 用户-IP/设备ID/提现地址-关联用户详情-异步导出

- 接口声明：`POST /relation/detail/async-export`
- 输入字段：`batch_user_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9375` · `UserRelationDetailAsyncExportResource`

### ACCOUNT-251 · 解绑第三方账号

- 接口声明：`DELETE /third-party`
- 输入字段：`user_id`, `source`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9424` · `ThirdPartyAccountResource`

### ACCOUNT-252 · 用户-KOL列表-列表详情

- 接口声明：`GET /kol-user`
- 输入字段：`user_id`, `account_platform`, `status`, `location`, `page`, `limit`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9487` · `KolUserListResource`

### ACCOUNT-253 · 用户-KOL列表-添加KOL用户

- 接口声明：`POST /kol-user`
- 输入字段：`user_id`, `account_platforms`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9542` · `KolUserListResource`

### ACCOUNT-254 · 用户-KOL列表-修改KOL用户

- 接口声明：`PUT /kol-user/<int:id_>`
- 输入字段：`user_id`, `account_platforms`, `status`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9579` · `KolUserDetailResource`

### ACCOUNT-255 · 用户-KOL列表-删除KOL用户

- 接口声明：`DELETE /kol-user/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9608` · `KolUserDetailResource`

### ACCOUNT-256 · 用户-KOL申请-列表详情

- 接口声明：`GET /kol-apply`
- 输入字段：`user_id`, `account_platform`, `location`, `page`, `limit`, `start`, `end`, `export`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9667` · `KolApplyListResource`

### ACCOUNT-257 · 用户-KOL申请-修改详情

- 接口声明：`PUT /kol-apply/<int:apply_id>`
- 输入字段：`remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9749` · `KolApplyDetailResource`

### ACCOUNT-258 · 查询用户价格提醒设置

- 接口声明：`GET /<int:id_>/price-notice`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9894` · `UserPriceNoticeResource`

### ACCOUNT-259 · 用户详情-权益记录

- 接口声明：`GET /<int:id_>/equity-records`
- 输入字段：`equity_id`, `equity_type`, `status`, `business_type`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:9933` · `UserEquityRecordsResource`

### ACCOUNT-260 · 用户详情-权益记录-合约体验权益仓位使用

- 接口声明：`GET /<int:id_>/equity-records/<int:record_id>/perpetual-positions`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:10145` · `UserEquityRecordPerpetualPositionsResource`

### ACCOUNT-261 · 查询ip信誉信息

- 接口声明：`GET /ip-reputation`
- 输入字段：`ip`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:10331` · `IPReputationResource`

### ACCOUNT-262 · 手动更新ip信誉信息

- 接口声明：`POST /ip-reputation`
- 输入字段：`ip`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:10341` · `IPReputationResource`

### ACCOUNT-263 · 用户详情-币币-历史委托

- 接口声明：`GET /<int:id_>/onchain-stop-orders`
- 输入字段：`status`, `side`, `asset`, `page`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:10365` · `UserOnchainStopOrderResource`

### ACCOUNT-264 · 用户详情-币币-链上交易-撤销计划委托

- 接口声明：`DELETE /<int:id_>/onchain-stop-orders/<int:order_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:10470` · `UserOnchainStopOrderDeleteResource`

### ACCOUNT-265 · 用户详情-币币-链上交易-批量撤销计划委托单

- 接口声明：`DELETE /<int:id_>/onchain-stop-orders/batch`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/admin/users.py:10486` · `UserOnchainStopOrderBatchDeleteResource`

### ACCOUNT-266 · BusinessTypesResource.get（用途待确认）

- 接口声明：`GET /balance/business-types`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:217` · `BusinessTypesResource`

### ACCOUNT-267 · AssetConversionResource.get（用途待确认）

- 接口声明：`GET /asset/conversion`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:240` · `AssetConversionResource`

### ACCOUNT-268 · AssetConversionResource.post（用途待确认）

- 接口声明：`POST /asset/conversion`
- 输入字段：`assets`
- 显式控制：require_login(allow_sub_account=False); trade_permission_validate(is_spot=True, account_id=0)
- 代码依据：`app/api/frontend/account.py:260` · `AssetConversionResource`

### ACCOUNT-269 · AssetConvertibleResource.get（用途待确认）

- 接口声明：`GET /asset/conversion_list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/account.py:446` · `AssetConvertibleResource`

### ACCOUNT-270 · AssetConversionHistoryResource.get（用途待确认）

- 接口声明：`GET /asset/conversion_history`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/account.py:474` · `AssetConversionHistoryResource`

### ACCOUNT-271 · AssetSettingsResource.get（用途待确认）

- 接口声明：`GET /asset/setting`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:502` · `AssetSettingsResource`

### ACCOUNT-272 · DepositsResource.get（用途待确认）

- 接口声明：`GET /coin/deposit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:511` · `DepositsResource`

### ACCOUNT-273 · DepositResource.get（用途待确认）

- 接口声明：`GET /coin/deposit/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:521` · `DepositResource`

### ACCOUNT-274 · ProcessingDepositsResource.get（用途待确认）

- 接口声明：`GET /coin/deposit/processing`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:530` · `ProcessingDepositsResource`

### ACCOUNT-275 · WithdrawalsResource.get（用途待确认）

- 接口声明：`GET /coin/withdraw`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:539` · `WithdrawalsResource`

### ACCOUNT-276 · WithdrawalsResource.post（用途待确认）

- 接口声明：`POST /coin/withdraw`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:543` · `WithdrawalsResource`

### ACCOUNT-277 · WithdrawalResource.get（用途待确认）

- 接口声明：`GET /coin/withdraw/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:553` · `WithdrawalResource`

### ACCOUNT-278 · WithdrawalResource.patch（用途待确认）

- 接口声明：`PATCH /coin/withdraw/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:557` · `WithdrawalResource`

### ACCOUNT-279 · WithdrawalResource.delete（用途待确认）

- 接口声明：`DELETE /coin/withdraw/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:561` · `WithdrawalResource`

### ACCOUNT-280 · WithdrawalAmountResource.get（用途待确认）

- 接口声明：`GET /coin/withdraw/amount`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:570` · `WithdrawalAmountResource`

### ACCOUNT-281 · WithdrawalLimitResource.get（用途待确认）

- 接口声明：`GET /withdraw/limit`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:579` · `WithdrawalLimitResource`

### ACCOUNT-282 · DepositWithdrawalBroadcastResource.get（用途待确认）

- 接口声明：`GET /deposit/withdrawal/broadcast`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:588` · `DepositWithdrawalBroadcastResource`

### ACCOUNT-283 · FeeResource.get（用途待确认）

- 接口声明：`GET /fee`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:597` · `FeeResource`

### ACCOUNT-284 · SpecialFeeResource.get（用途待确认）

- 接口声明：`GET /special/fee`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:610` · `SpecialFeeResource`

### ACCOUNT-285 · UserFeeResource.get（用途待确认）

- 接口声明：`GET /user/fee`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:648` · `UserFeeResource`

### ACCOUNT-286 · UserFeeResource.put（用途待确认）

- 接口声明：`PUT /user/fee`
- 输入字段：`fee_switch`
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:659` · `UserFeeResource`

### ACCOUNT-287 · BalanceHistoryResource.get（用途待确认）

- 接口声明：`GET /balance/history`
- 输入字段：`asset`, `account_id`, `account_type`, `business`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:699` · `BalanceHistoryResource`

### ACCOUNT-288 · BalanceSeriesResource.get（用途待确认）

- 接口声明：`GET /balance/series`
- 输入字段：`account_type`, `asset`, `account_id`, `days`, `market`
- 显式控制：require_login(allow_sub_account=True)
- 代码依据：`app/api/frontend/account.py:862` · `BalanceSeriesResource`

### ACCOUNT-289 · BalanceSumSeriesResource.get（用途待确认）

- 接口声明：`GET /balance/sum/series`
- 输入字段：`account_type`, `days`
- 显式控制：require_login(allow_sub_account=True)
- 代码依据：`app/api/frontend/account.py:913` · `BalanceSumSeriesResource`

### ACCOUNT-290 · 账户间划转历史 

- 接口声明：`GET /transfer/history`
- 输入字段：`asset`, `account_type`, `start_time`, `end_time`, `page`, `limit`, `export`
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:950` · `AccountTransferHistoryResource`

### ACCOUNT-291 · 导航栏的资产字段。主帐号时，要包括子帐号的资产市值 

- 接口声明：`GET /realtime-balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:1059` · `RealtimeBalanceResource`

### ACCOUNT-292 · 各个帐户的资产市值（APP使用） 

- 接口声明：`GET /realtime-account-balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:1087` · `RealtimeAccountBalanceResource`

### ACCOUNT-293 · AssetLogoResource.get（用途待确认）

- 接口声明：`GET /asset/logo`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:1099` · `AssetLogoResource`

### ACCOUNT-294 · 导出报税数据

- 接口声明：`POST /tax/export`
- 输入字段：`start_time`, `end_time`, `account`, `asset`, `hide_transfer`
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:1134` · `TaxExportResource`

### ACCOUNT-295 · 报税数据导出历史

- 接口声明：`GET /tax/export/history`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:1186` · `TaxExportHistoryResource`

### ACCOUNT-296 · 下载已导出的报税数据

- 接口声明：`GET /tax/export/download/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:1236` · `TaxExportDownloadResource`

### ACCOUNT-297 · 获取用户分享弹窗详情

- 接口声明：`GET /share-pop-window`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/account.py:1265` · `SharePopResource`

### ACCOUNT-298 · 更新用户已弹窗的记录

- 接口声明：`PATCH /share-pop-window`
- 输入字段：`pop_type`, `pop_types`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/account.py:1289` · `SharePopResource`

### ACCOUNT-299 · BalanceMerkleReserve.get（用途待确认）

- 接口声明：`GET /balance/merkle/reserve`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/account.py:1320` · `BalanceMerkleReserve`

### ACCOUNT-300 · BalanceMerkleProof.get（用途待确认）

- 接口声明：`GET /balance/merkle/proof`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/account.py:1358` · `BalanceMerkleProof`

### ACCOUNT-301 · BalanceLockProof.get（用途待确认）

- 接口声明：`GET /balance/lock`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/account.py:1389` · `BalanceLockProof`

### ACCOUNT-302 · 导出账户结单数据

- 接口声明：`POST /statement/export`
- 输入字段：`export_month`, `include_deposit_withdrawal_detail`, `include_order_detail`
- 显式控制：require_login()
- 代码依据：`app/api/frontend/account.py:1421` · `AccountStatementExportResource`

### ACCOUNT-303 · 发送账户结单数据到主账户邮箱

- 接口声明：`POST /statement/export/send_email`
- 输入字段：`export_history_id`
- 显式控制：require_login()
- 代码依据：`app/api/frontend/account.py:1490` · `AccountStatementExportSendResource`

### ACCOUNT-304 · 获取账户结单导出任务列表

- 接口声明：`GET /statement/export/history`
- 输入字段：`page`, `limit`
- 显式控制：require_login()
- 代码依据：`app/api/frontend/account.py:1530` · `AccountStatementExportHistoryResource`

### ACCOUNT-305 · 现货币种持仓成本

- 接口声明：`GET /balance/cost`
- 输入字段：`page`, `limit`
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:1591` · `AccountBalanceCostResource`

### ACCOUNT-306 · AccountBalanceCostResource.post（用途待确认）

- 接口声明：`POST /balance/cost`
- 输入字段：`asset`, `price`
- 显式控制：require_login
- 代码依据：`app/api/frontend/account.py:1615` · `AccountBalanceCostResource`

### ACCOUNT-307 · EmailCodeResource.get（用途待确认）

- 接口声明：`GET /email/code`
- 输入字段：`email`, `code_type`, `device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:176` · `EmailCodeResource`

### ACCOUNT-308 · EmailCodeResource.post（用途待确认）

- 接口声明：`POST /email/code`
- 输入字段：`email`, `validate_code`, `code_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:220` · `EmailCodeResource`

### ACCOUNT-309 · MobileTokenResource.get（用途待确认）

- 接口声明：`GET /mobile/token`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:259` · `MobileTokenResource`

### ACCOUNT-310 · WebAuthnList.get（用途待确认）

- 接口声明：`GET /webauthn/list`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/auth.py:269` · `WebAuthnList`

### ACCOUNT-311 · WebAuthnRegistration.get（用途待确认）

- 接口声明：`GET /webauthn/registration`
- 输入字段：`authenticator_attachment`
- 显式控制：require_login; ns.use_kwargs(dict(authenticator_attachment=fields.String))
- 代码依据：`app/api/frontend/auth.py:288` · `WebAuthnRegistration`

### ACCOUNT-312 · WebAuthnRegistration.post（用途待确认）

- 接口声明：`POST /webauthn/registration`
- 输入字段：`credential`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:308` · `WebAuthnRegistration`

### ACCOUNT-313 · 通行密钥鉴权

- 接口声明：`GET /webauthn/authentication`
- 输入字段：`key`, `email_code_token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:385` · `WebAuthResource`

### ACCOUNT-314 · WebAuthResource.post（用途待确认）

- 接口声明：`POST /webauthn/authentication`
- 输入字段：`credential`
- 显式控制：require_login
- 代码依据：`app/api/frontend/auth.py:401` · `WebAuthResource`

### ACCOUNT-315 · WebAuthRenameResource.post（用途待确认）

- 接口声明：`POST /webauthn/rename`
- 输入字段：`name`, `credential_id`
- 显式控制：require_login()
- 代码依据：`app/api/frontend/auth.py:425` · `WebAuthRenameResource`

### ACCOUNT-316 · WebAuthUnbindResource.post（用途待确认）

- 接口声明：`POST /webauthn/unbind`
- 输入字段：`credential_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:443` · `WebAuthUnbindResource`

### ACCOUNT-317 · MobileCodeResource.get（用途待确认）

- 接口声明：`GET /mobile/code`
- 输入字段：`country_code`, `mobile`, `code_type`, `token`, `sig`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:598` · `MobileCodeResource`

### ACCOUNT-318 · MobileCodeResource.post（用途待确认）

- 接口声明：`POST /mobile/code`
- 输入字段：`validate_code`, `code_type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/auth.py:652` · `MobileCodeResource`

### ACCOUNT-319 · TotpCodeResource.post（用途待确认）

- 接口声明：`POST /totp/code`
- 输入字段：`validate_code`
- 显式控制：require_login
- 代码依据：`app/api/frontend/auth.py:677` · `TotpCodeResource`

### ACCOUNT-320 · QrCodeSignResource.get（用途待确认）

- 接口声明：`GET /qrcode/sign`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:698` · `QrCodeSignResource`

### ACCOUNT-321 · ThirdPartyAuthURLResource.get（用途待确认）

- 接口声明：`GET /<string:name>`
- 输入字段：`device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/auth.py:709` · `ThirdPartyAuthURLResource`

### ACCOUNT-322 · KYC: 查询各国家支持的证件类型 目前只有 APP 端在使用。WEB 端 KYC 个人认证与 KYC 机构认证已经切换到新的接口：SupportedIDTypesResource （TODO: 后续 APP 切换新接口后，考虑删除）

- 接口声明：`GET /accepted_id_types`
- 输入字段：`kyc_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/kyc.py:213` · `AcceptedIDTypesResource`

### ACCOUNT-323 · KYC: 查询各国家支持的证件类型（新版）

- 接口声明：`GET /supported`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/kyc.py:241` · `SupportedIDTypesResource`

### ACCOUNT-324 · KYC: 提交认证 (人工审核) 

- 接口声明：`POST /netverify`
- 输入字段：`frontside_image_file`, `backside_image_file`, `face_image_file`, `country`, `nationality`, `id_number`, `id_type`, `first_name`, `last_name`, `name`, `gender`, `date_of_birth`, `expire_date`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:270` · `VerificationResource`

### ACCOUNT-325 · KYC: 图片上传

- 接口声明：`POST /image/upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/kyc.py:356` · `KYCImageUploadResource`

### ACCOUNT-326 · KYC: 校验基本信息

- 接口声明：`POST /basic-info`
- 输入字段：`country`, `nationality`, `id_type`, `id_number`, `first_name`, `last_name`, `name`, `gender`, `date_of_birth`, `expire_date`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/kyc.py:443` · `KycRequestIdResource`

### ACCOUNT-327 · KycStatusResource.get（用途待确认）

- 接口声明：`GET /status`
- 输入字段：`raw`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/kyc.py:531` · `KycStatusResource`

### ACCOUNT-328 · KycOpportunityResource.get（用途待确认）

- 接口声明：`GET /opportunity`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/kyc.py:547` · `KycOpportunityResource`

### ACCOUNT-329 · KYC: 提交认证至第三方

- 接口声明：`POST /verification`
- 输入字段：`frontside_image_file`, `backside_image_file`, `face_image_file`, `country`, `nationality`, `id_type`, `id_number`, `first_name`, `last_name`, `name`, `gender`, `date_of_birth`, `expire_date`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:575` · `VerificationSubmitResource`

### ACCOUNT-330 · KYC: 初高级混合提交认证

- 接口声明：`POST /verification/mixin`
- 输入字段：`frontside_image_file`, `backside_image_file`, `face_image_file`, `country`, `nationality`, `id_type`, `id_number`, `name`, `gender`, `date_of_birth`, `address`, `address_file_ids`, `address_file_category`, `address_file_type`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:678` · `VerificationMixinSubmitResource`

### ACCOUNT-331 · KYC: 提交非文件认证至第三方

- 接口声明：`POST /verification/non-doc`
- 输入字段：`country`, `nationality`, `id_type`, `id_number`, `name`, `gender`, `date_of_birth`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:815` · `NonDocVerificationSubmitResource`

### ACCOUNT-332 · KYC: 非文件验证人脸识别后调用

- 接口声明：`PATCH /verification/non-doc`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:909` · `NonDocVerificationSubmitResource`

### ACCOUNT-333 · KYC: 扩展认证提交非文件认证至第三方

- 接口声明：`POST /verification/extend/non-doc`
- 输入字段：`nationality`, `id_type`, `id_number`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:971` · `NonDocVerificationExtendSubmitResource`

### ACCOUNT-334 · KYC: 扩展认证非文件验证人脸识别后调用

- 接口声明：`PATCH /verification/extend/non-doc`
- 输入字段：`nationality`, `id_type`, `id_number`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:1015` · `NonDocVerificationExtendSubmitResource`

### ACCOUNT-335 · KYC: 获取sumsub access token

- 接口声明：`GET /sumsub/token`
- 输入字段：`type`, `nationality`, `id_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/kyc.py:1070` · `SumsubAccessTokenResource`

### ACCOUNT-336 · 用户提交 KYC 机构认证

- 接口声明：`POST /institution`
- 输入字段：`company_info`, `manager_info`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/kyc.py:1150` · `KYCInstitutionResource`

### ACCOUNT-337 · 获取生物识别认证结果

- 接口声明：`GET /liveness`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/kyc.py:1261` · `LivenessCheckResource`

### ACCOUNT-338 · 用户发起生物识别认证

- 接口声明：`POST /liveness`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/kyc.py:1273` · `LivenessCheckResource`

### ACCOUNT-339 · 用户完成生物识别认证

- 接口声明：`PATCH /liveness`
- 输入字段：`token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/kyc.py:1303` · `LivenessCheckResource`

### ACCOUNT-340 · 获取CoinEx授权页面

- 接口声明：`GET /authorize`
- 输入字段：`client_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/oauth.py:23` · `AuthorizeResource`

### ACCOUNT-341 · 获取CoinEx授权token

- 接口声明：`POST /authorize`
- 输入字段：`client_id`, `code`, `client_secret`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/oauth.py:42` · `AuthorizeResource`

### ACCOUNT-342 · 获取client的基本信息

- 接口声明：`GET /client-info`
- 输入字段：`client_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/oauth.py:78` · `ClientInfoResource`

### ACCOUNT-343 · 获取授权码

- 接口声明：`POST /code`
- 输入字段：`client_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/oauth.py:105` · `AuthorizeCodeResource`

### ACCOUNT-344 · AuthorizeCreateAPIResource.post（用途待确认）

- 接口声明：`POST /create-api`
- 输入字段：`access_token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/oauth.py:136` · `AuthorizeCreateAPIResource`

### ACCOUNT-345 · 子账号列表(包括 用户创建的、系统策略子帐号，系统策略子帐号会汇总为一个) 

- 接口声明：`GET /`
- 输入字段：`user_name`, `status`, `sort_type`, `filter_balance`, `page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:91` · `SubAccountsResource`

### ACCOUNT-346 · 子账号总资产USD 

- 接口声明：`GET /total-balance`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:233` · `SubAccountTotalBalanceResource`

### ACCOUNT-347 · 子账号用户名列表 

- 接口声明：`GET /names`
- 输入字段：`status`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:246` · `SubAccountNamesResource`

### ACCOUNT-348 · 新增子账号 

- 接口声明：`POST /register`
- 输入字段：`user_name`, `permissions`, `remark`, `custody_platform`
- 显式控制：ns.use_kwargs(dict(user_name=fields.String(required=True), permissions=fields.List(EnumField(SubAccountPermission), required=True), remark=fields.String(load_default=''), custody_p
- 代码依据：`app/api/frontend/sub_accounts.py:288` · `SubAccountRegistrationResource`

### ACCOUNT-349 · 获取子账号可划转数量（现货、合约） 

- 接口声明：`GET /balance/transfer`
- 输入字段：`sub_user_id`, `asset`, `account_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:385` · `BalanceTransferResource`

### ACCOUNT-350 · 子账号用户维度 划转 

- 接口声明：`POST /balance/transfer`
- 输入字段：`source_user_id`, `target_user_id`, `source_account`, `target_account`, `coin_type`, `amount`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:413` · `BalanceTransferResource`

### ACCOUNT-351 · 子账号用户维度-划转历史 

- 接口声明：`GET /balance/transfer/history`
- 输入字段：`source_user_id`, `target_user_id`, `asset`, `start_date`, `end_date`, `page`, `limit`, `export`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:501` · `TransferHistoryResource`

### ACCOUNT-352 · 子账号-详情信息 

- 接口声明：`GET /<int:user_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:603` · `SubAccountResource`

### ACCOUNT-353 · 修改子账号信息 

- 接口声明：`PATCH /<int:user_id>`
- 输入字段：`user_name`, `remark`, `permissions`
- 显式控制：require_login(allow_sub_account=False); ns.use_kwargs(dict(user_name=fields.String, remark=fields.String, permissions=fields.List(EnumField(SubAccountPermission))))
- 代码依据：`app/api/frontend/sub_accounts.py:623` · `SubAccountResource`

### ACCOUNT-354 · 禁用子账号 

- 接口声明：`PUT /<int:user_id>/frozen`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:751` · `AccountFreezingResource`

### ACCOUNT-355 · 取消禁用子账号 

- 接口声明：`PUT /<int:user_id>/unfrozen`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:765` · `AccountUnfreezingResource`

### ACCOUNT-356 · ReferenceUser.get（用途待确认）

- 接口声明：`GET /reference_user`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/sub_accounts.py:779` · `ReferenceUser`

### ACCOUNT-357 · 子账号-新增授权 

- 接口声明：`POST /managers`
- 输入字段：`user_id`, `account`, `manage_type`, `remark`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/sub_accounts.py:794` · `SubAccountManagerListResource`

### ACCOUNT-358 · 子账号-授权列表 

- 接口声明：`GET /managers`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:903` · `SubAccountManagerListResource`

### ACCOUNT-359 · 子账号-解除授权 

- 接口声明：`DELETE /managers/<int:row_id>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:978` · `SubAccountManagerResource`

### ACCOUNT-360 · 子账号-授权列表 编辑备注 

- 接口声明：`PUT /managers/<int:row_id>`
- 输入字段：`remark`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:1036` · `SubAccountManagerResource`

### ACCOUNT-361 · 子账号-托管列表(他人授权) 

- 接口声明：`GET /managements`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:1066` · `SubAccountManagementListResource`

### ACCOUNT-362 · 子账号-托管列表(他人授权) 编辑备注 

- 接口声明：`PUT /managements/<int:row_id>`
- 输入字段：`remark`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/sub_accounts.py:1160` · `SubAccountManagementResource`

### ACCOUNT-363 · UserResource.get（用途待确认）

- 接口声明：`GET /`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:320` · `UserResource`

### ACCOUNT-364 · UserResource.put（用途待确认）

- 接口声明：`PUT /`
- 输入字段：`name`, `account_name`, `avatar`, `lang`, `display_asset`, `order_confirm`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:481` · `UserResource`

### ACCOUNT-365 · "同UserResource，但只返回尽量少的字段，提高响应性能，加速首屏渲染

- 接口声明：`GET /basic`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:522` · `UserBasicResource`

### ACCOUNT-366 · 获取IM用户信息，支持匿名和实名调用

- 接口声明：`GET /im-user-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:566` · `ImUserInfoResource`

### ACCOUNT-367 · SignUpResource.post（用途待确认）

- 接口声明：`POST /sign/up/email`
- 输入字段：`email`, `validate_code`, `email_code_token`, `login_password`, `refer_code`, `channel`, `device_id`, `activity_party`
- 显式控制：ns.use_kwargs(dict(email=NewEmailField(required=True), validate_code=fields.String, email_code_token=fields.String, login_password=fields.String(required=True), refer_code=fields.S
- 代码依据：`app/api/frontend/user.py:754` · `SignUpResource`

### ACCOUNT-368 · SignInResource.post（用途待确认）

- 接口声明：`POST /sign/in`
- 输入字段：`account`, `login_password`, `device_id`
- 显式控制：ns.use_kwargs(dict(account=fields.String(required=True), login_password=fields.String(required=True), device_id=DeviceIdField(required=True)))
- 代码依据：`app/api/frontend/user.py:941` · `SignInResource`

### ACCOUNT-369 · SignInWith2FAResource.post（用途待确认）

- 接口声明：`POST /sign/in/verify`
- 输入字段：`operate_token`, `validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1010` · `SignInWith2FAResource`

### ACCOUNT-370 · 轮询二维码

- 接口声明：`GET /sign/qrcode`
- 输入字段：`qrcode_key`, `device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1092` · `LoginQRCodeResource`

### ACCOUNT-371 · 生成登陆二维码

- 接口声明：`POST /sign/qrcode`
- 输入字段：`device_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1138` · `LoginQRCodeResource`

### ACCOUNT-372 · App扫码

- 接口声明：`PATCH /sign/qrcode`
- 输入字段：`qrcode_key`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1164` · `LoginQRCodeResource`

### ACCOUNT-373 · 确认登陆

- 接口声明：`PUT /sign/qrcode`
- 输入字段：`operation_token`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1208` · `LoginQRCodeResource`

### ACCOUNT-374 · SignOutResource.post（用途待确认）

- 接口声明：`POST /sign/out`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:1246` · `SignOutResource`

### ACCOUNT-375 · SignOffResource.get（用途待确认）

- 接口声明：`GET /sign/off`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1274` · `SignOffResource`

### ACCOUNT-376 · 用户注销

- 接口声明：`POST /sign/off`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1281` · `SignOffResource`

### ACCOUNT-377 · CountriesResource.get（用途待确认）

- 接口声明：`GET /sign/country`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1323` · `CountriesResource`

### ACCOUNT-378 · SignUPIpResource.get（用途待确认）

- 接口声明：`GET /sign/up/ip`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1357` · `SignUPIpResource`

### ACCOUNT-379 · Deprecated

- 接口声明：`GET /sign/captcha`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1386` · `CaptchaResource`

### ACCOUNT-380 · LoginHistoryResource.get（用途待确认）

- 接口声明：`GET /sign/log`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1409` · `LoginHistoryResource`

### ACCOUNT-381 · LoginStatesResource.get（用途待确认）

- 接口声明：`GET /login-states`
- 输入字段：`page`, `limit`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1461` · `LoginStatesResource`

### ACCOUNT-382 · LoginStateResource.delete（用途待确认）

- 接口声明：`DELETE /login-states/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1498` · `LoginStateResource`

### ACCOUNT-383 · EmailResource.post（用途待确认）

- 接口声明：`POST /email`
- 输入字段：`email`, `validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1525` · `EmailResource`

### ACCOUNT-384 · 账户设置-修改邮箱 

- 接口声明：`PUT /email`
- 输入字段：`email`, `validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1546` · `EmailResource`

### ACCOUNT-385 · MobileResource.post（用途待确认）

- 接口声明：`POST /mobile`
- 输入字段：`country_code`, `mobile`, `validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1597` · `MobileResource`

### ACCOUNT-386 · 账户设置-修改手机 

- 接口声明：`PUT /mobile`
- 输入字段：`country_code`, `mobile`, `validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1666` · `MobileResource`

### ACCOUNT-387 · 账户设置-解绑手机 

- 接口声明：`PATCH /mobile`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1715` · `MobileResource`

### ACCOUNT-388 · 账户设置-设置提现密码 

- 接口声明：`POST /withdraw-password`
- 输入字段：`withdraw_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1751` · `WithdrawPasswordResource`

### ACCOUNT-389 · 账户设置-修改提现密码 

- 接口声明：`PUT /withdraw-password`
- 输入字段：`old_withdraw_password`, `new_withdraw_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1786` · `WithdrawPasswordResource`

### ACCOUNT-390 · 验证提现密码 

- 接口声明：`POST /withdraw-password/validate`
- 输入字段：`withdraw_password`, `usage`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1830` · `WithdrawPasswordValidateResource`

### ACCOUNT-391 · 账户设置-交易密码详情 

- 接口声明：`GET /trade-password`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:1852` · `TradePasswordResource`

### ACCOUNT-392 · 账户设置-设置交易密码 

- 接口声明：`POST /trade-password`
- 输入字段：`trade_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1867` · `TradePasswordResource`

### ACCOUNT-393 · 账户设置-修改交易密码 

- 接口声明：`PUT /trade-password`
- 输入字段：`new_trade_password`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1889` · `TradePasswordResource`

### ACCOUNT-394 · 验证交易密码 

- 接口声明：`POST /trade-password/validate`
- 输入字段：`trade_password`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:1938` · `TradePasswordValidateResource`

### ACCOUNT-395 · TotpResource.get（用途待确认）

- 接口声明：`GET /totp`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:1954` · `TotpResource`

### ACCOUNT-396 · TotpResource.post（用途待确认）

- 接口声明：`POST /totp`
- 输入字段：`validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:1964` · `TotpResource`

### ACCOUNT-397 · 账户设置-修改TOTP 

- 接口声明：`PUT /totp`
- 输入字段：`validate_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2031` · `TotpResource`

### ACCOUNT-398 · 账户设置-解绑TOTP 

- 接口声明：`PATCH /totp`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2072` · `TotpResource`

### ACCOUNT-399 · TotpValidationResource.post（用途待确认）

- 接口声明：`POST /validate/totp`
- 输入字段：`validate_code`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:2106` · `TotpValidationResource`

### ACCOUNT-400 · AuthAPIsResource.get（用途待确认）

- 接口声明：`GET /auth/api`
- 输入字段：`page`, `limit`
- 显式控制：require_login; require_user_permission(sub_account_permissions=[SubAccountPermission.API])
- 代码依据：`app/api/frontend/user.py:2153` · `AuthAPIsResource`

### ACCOUNT-401 · AuthAPIsResource.post（用途待确认）

- 接口声明：`POST /auth/api`
- 输入字段：`remark`, `allow_ips`, `allow_withdraw`, `allow_trade`, `is_copy_trader`, `validity_period`
- 显式控制：require_user_permission(sub_account_permissions=[SubAccountPermission.API])
- 代码依据：`app/api/frontend/user.py:2182` · `AuthAPIsResource`

### ACCOUNT-402 · AuthAPIResource.get（用途待确认）

- 接口声明：`GET /auth/api/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_user_permission(sub_account_permissions=[SubAccountPermission.API])
- 代码依据：`app/api/frontend/user.py:2253` · `AuthAPIResource`

### ACCOUNT-403 · AuthAPIResource.put（用途待确认）

- 接口声明：`PUT /auth/api/<int:id_>`
- 输入字段：`remark`, `allow_ips`, `allow_withdraw`, `allow_trade`, `validity_period`
- 显式控制：require_user_permission(sub_account_permissions=[SubAccountPermission.API])
- 代码依据：`app/api/frontend/user.py:2260` · `AuthAPIResource`

### ACCOUNT-404 · AuthAPIResource.delete（用途待确认）

- 接口声明：`DELETE /auth/api/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2302` · `AuthAPIResource`

### ACCOUNT-405 · AuthAPIResource.patch（用途待确认）

- 接口声明：`PATCH /auth/api/<int:id_>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_user_permission(sub_account_permissions=[SubAccountPermission.API])
- 代码依据：`app/api/frontend/user.py:2312` · `AuthAPIResource`

### ACCOUNT-406 · APIKEY续期

- 接口声明：`PUT /auth/api/extend/<token>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2340` · `AuthAPIExtendResource`

### ACCOUNT-407 · 获取APIKEY续期相关信息

- 接口声明：`GET /auth/api/extend/<token>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2360` · `AuthAPIExtendResource`

### ACCOUNT-408 · 非登录态重置密码2fa验证

- 接口声明：`POST /sign/reset/2fa`
- 输入字段：`email_code_token`, `validate_code`, `type`, `credential`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2391` · `PasswordReset2FAResource`

### ACCOUNT-409 · (主账号登入态)账户设置-重置密码

- 接口声明：`PUT /sign/reset/by/email`
- 输入字段：`email_code_token`, `login_password`
- 显式控制：require_login(allow_sub_account=False); ns.use_kwargs(dict(email_code_token=fields.String(required=True), login_password=fields.String(required=True)))
- 代码依据：`app/api/frontend/user.py:2437` · `PasswordResetByEmailResource`

### ACCOUNT-410 · (主账号非登入态)忘记/重置密码

- 接口声明：`PUT /security/reset/password`
- 输入字段：`email`, `email_code_token`, `login_password`
- 显式控制：ns.use_kwargs(dict(email=EmailField(required=True), email_code_token=fields.String(required=True), login_password=fields.String(required=True)))
- 代码依据：`app/api/frontend/user.py:2496` · `NonLoginPasswordResetByEmailResource`

### ACCOUNT-411 · 非登入态获取用户信息 

- 接口声明：`GET /info`
- 输入字段：`email`, `email_code_token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2561` · `NonLoginUserInfoResource`

### ACCOUNT-412 · (子账号登入态)账户设置-重置密码 

- 接口声明：`PUT /sign/auth/reset/by/email`
- 输入字段：`email_code_token`, `login_password`
- 显式控制：require_login; ns.use_kwargs(dict(email_code_token=fields.String(required=True), login_password=fields.String(required=True)))
- 代码依据：`app/api/frontend/user.py:2603` · `AuthPasswordResetByEmailResource`

### ACCOUNT-413 · SafetyUserResource.get（用途待确认）

- 接口声明：`GET /safety/user`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:2659` · `SafetyUserResource`

### ACCOUNT-414 · SafetyUserResource.put（用途待确认）

- 接口声明：`PUT /safety/user`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2664` · `SafetyUserResource`

### ACCOUNT-415 · SafetyForbidResource.post（用途待确认）

- 接口声明：`POST /safety/forbid`
- 输入字段：`reason`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:2677` · `SafetyForbidResource`

### ACCOUNT-416 · App设置指纹/手势密码时校验登录密码

- 接口声明：`POST /safety/login`
- 输入字段：`login_password`
- 显式控制：require_login(allow_sub_account=False); ns.use_kwargs(dict(login_password=fields.String(required=True)))
- 代码依据：`app/api/frontend/user.py:2765` · `SafetyLoginResource`

### ACCOUNT-417 · 添加防钓鱼码

- 接口声明：`POST /anti-phishing-code`
- 输入字段：`anti_phishing_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2783` · `AntiPhishingCodeResource`

### ACCOUNT-418 · 编辑防钓鱼码

- 接口声明：`PUT /anti-phishing-code`
- 输入字段：`anti_phishing_code`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2803` · `AntiPhishingCodeResource`

### ACCOUNT-419 · BindingAccountsResource.get（用途待确认）

- 接口声明：`GET /binding/accounts`
- 输入字段：`account_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:2828` · `BindingAccountsResource`

### ACCOUNT-420 · TelegramBindingUrlResource.get（用途待确认）

- 接口声明：`GET /binding/telegram/url`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:2852` · `TelegramBindingUrlResource`

### ACCOUNT-421 · 自助重置安全工具，校验账号密码

- 接口声明：`POST /security/reset/account`
- 输入字段：`account`, `login_password`
- 显式控制：ns.use_kwargs(dict(account=EmailField(required=True), login_password=fields.String(required=True)))
- 代码依据：`app/api/frontend/user.py:2908` · `SecurityVerificationResource`

### ACCOUNT-422 · 异常流程-非登入态获取用户非敏感信息 

- 接口声明：`GET /security/reset/account-forget`
- 输入字段：`email`, `flow_case`, `reset_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:2957` · `NonSensitiveUserInfoResource`

### ACCOUNT-423 · SecurityQuestionResource.get（用途待确认）

- 接口声明：`GET /security/reset/answer`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3011` · `SecurityQuestionResource`

### ACCOUNT-424 · SecurityQuestionResource.post（用途待确认）

- 接口声明：`POST /security/reset/answer`
- 输入字段：`reset_type`, `answer`, `email_code_token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3027` · `SecurityQuestionResource`

### ACCOUNT-425 · Security2FAResource.post（用途待确认）

- 接口声明：`POST /security/reset/2fa`
- 输入字段：`validate_code`, `type`, `credential`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3167` · `Security2FAResource`

### ACCOUNT-426 · SecurityNewEmailResource.post（用途待确认）

- 接口声明：`POST /security/reset/email`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3207` · `SecurityNewEmailResource`

### ACCOUNT-427 · SecurityStatisticsResource.get（用途待确认）

- 接口声明：`GET /security/statistics`
- 输入字段：`user_id`, `type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3267` · `SecurityStatisticsResource`

### ACCOUNT-428 · UnfreezeAccountResource.post（用途待确认）

- 接口声明：`POST /unfreeze/account`
- 输入字段：`account`, `login_password`
- 显式控制：ns.use_kwargs(dict(account=EmailField(required=True), login_password=fields.String(required=True)))
- 代码依据：`app/api/frontend/user.py:3292` · `UnfreezeAccountResource`

### ACCOUNT-429 · UnfreezeEmailResource.post（用途待确认）

- 接口声明：`POST /unfreeze/email`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3328` · `UnfreezeEmailResource`

### ACCOUNT-430 · UnfreezeSubmitResource.post（用途待确认）

- 接口声明：`POST /unfreeze/submit`
- 输入字段：`email_code_token`, `face_with_id_card`, `history_notice_snapshot`, `third_party_deposit_snapshot`, `id_card_front`, `id_card_back`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3385` · `UnfreezeSubmitResource`

### ACCOUNT-431 · 自助解冻-发起活体识别

- 接口声明：`POST /unfreeze/liveness`
- 输入字段：`email_code_token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3473` · `UnfreezeLivenessResource`

### ACCOUNT-432 · 自助解冻-用户完成生物识别认证

- 接口声明：`PATCH /unfreeze/liveness`
- 输入字段：`email_code_token`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3538` · `UnfreezeLivenessResource`

### ACCOUNT-433 · SecurityEmailValidateResource.post（用途待确认）

- 接口声明：`POST /security/validate/email`
- 输入字段：`email`, `validate_code`, `flow_case`, `reset_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3613` · `SecurityEmailValidateResource`

### ACCOUNT-434 · SecurityFileResource.post（用途待确认）

- 接口声明：`POST /security/reset/identity`
- 输入字段：`email_code_token`, `reset_type`, `flow_case`, `face_with_id_card`, `history_notice_snapshot`, `third_party_deposit_snapshot`, `third_party_deposit_video`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3676` · `SecurityFileResource`

### ACCOUNT-435 · SecurityLivenessResource.post（用途待确认）

- 接口声明：`POST /security/reset/liveness`
- 输入字段：`email_code_token`, `reset_type`, `flow_case`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3776` · `SecurityLivenessResource`

### ACCOUNT-436 · 重置安全工具-用户完成生物识别认证

- 接口声明：`PATCH /security/reset/liveness`
- 输入字段：`email_code_token`, `reset_type`, `flow_case`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3849` · `SecurityLivenessResource`

### ACCOUNT-437 · WithdrawPasswordResetResource.get（用途待确认）

- 接口声明：`GET /withdraw-password/reset/token`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:3929` · `WithdrawPasswordResetResource`

### ACCOUNT-438 · SecurityResetWithdrawPasswordResource.post（用途待确认）

- 接口声明：`POST /security/reset/withdraw-password`
- 输入字段：`token`, `face_with_id_card`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:3981` · `SecurityResetWithdrawPasswordResource`

### ACCOUNT-439 · for image/mp4 only

- 接口声明：`POST /security/reset/upload`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:4040` · `SecurityUploadResource`

### ACCOUNT-440 · 查询用户新手指引的状态 

- 接口声明：`GET /guide`
- 输入字段：`page`, `type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4083` · `UserGuideResource`

### ACCOUNT-441 · 更新用户新手指引的状态 

- 接口声明：`POST /guide`
- 输入字段：`page`, `type`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4115` · `UserGuideResource`

### ACCOUNT-442 · 查询用户所有协议勾选的状态，仅 app 端使用 

- 接口声明：`GET /user-agreement`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4164` · `UserAgreementResource`

### ACCOUNT-443 · 用户属性信息

- 接口声明：`GET /profile`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4319` · `UserProfileResource`

### ACCOUNT-444 · 可切换的账号列表 

- 接口声明：`GET /switch-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4430` · `SwitchUserListResource`

### ACCOUNT-445 · 切换子账号上报 

- 接口声明：`POST /report-switch-user`
- 输入字段：`user_id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4513` · `ReportSwitchUserResource`

### ACCOUNT-446 · UserEducationRecorde.put（用途待确认）

- 接口声明：`PUT /user-education-record`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4531` · `UserEducationRecorde`

### ACCOUNT-447 · UserEducationRecorde.get（用途待确认）

- 接口声明：`GET /user-education-record`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:4540` · `UserEducationRecorde`

### ACCOUNT-448 · 第三方账号信息

- 接口声明：`GET /third-party/account`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:4553` · `ThirdPartyAccountResource`

### ACCOUNT-449 · 第三方账号绑定

- 接口声明：`POST /third-party/account`
- 输入字段：`code`, `source`, `device_id`, `state`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/user.py:4566` · `ThirdPartyAccountResource`

### ACCOUNT-450 · 第三方账号解绑

- 接口声明：`DELETE /third-party/account`
- 输入字段：`source`
- 显式控制：require_login(allow_sub_account=False); lock_request(with_user=True)
- 代码依据：`app/api/frontend/user.py:4625` · `ThirdPartyAccountResource`

### ACCOUNT-451 · 第三方账号注册

- 接口声明：`POST /third-party/sign/up`
- 输入字段：`code`, `source`, `refer_code`, `channel`, `device_id`, `activity_party`, `state`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:4655` · `ThirdPartyAccountSignUpResource`

### ACCOUNT-452 · 第三方账号登录

- 接口声明：`POST /third-party/sign/in`
- 输入字段：`code`, `source`, `device_id`, `state`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:4728` · `ThirdPartyAccountSignInResource`

### ACCOUNT-453 · 非登录态绑定第三方账号

- 接口声明：`POST /third-party/bind`
- 输入字段：`account`, `login_password`, `code`, `source`, `device_id`, `email_code_token`, `state`
- 显式控制：ns.use_kwargs(dict(account=EmailField(required=True), login_password=fields.String(required=True), code=fields.String(required=True), source=EnumField(ThirdPartyAccount.Source, req
- 代码依据：`app/api/frontend/user.py:4778` · `ThirdPartyAccountBindResource`

### ACCOUNT-454 · P2pUserKycProResource.post（用途待确认）

- 接口声明：`POST /kyc-pro`
- 输入字段：`address`, `name`, `address_file_ids`, `file_type`
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:4893` · `P2pUserKycProResource`

### ACCOUNT-455 · P2pUserKycProResource.get（用途待确认）

- 接口声明：`GET /kyc-pro`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:4932` · `P2pUserKycProResource`

### ACCOUNT-456 · KycProFileCategoryResource.get（用途待确认）

- 接口声明：`GET /kyc-pro/category`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:4966` · `KycProFileCategoryResource`

### ACCOUNT-457 · ActivityPartyUserResource.get（用途待确认）

- 接口声明：`GET /activity-party`
- 输入字段：`activity_party`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user.py:4984` · `ActivityPartyUserResource`

### ACCOUNT-458 · EditPopupUserResource.post（用途待确认）

- 接口声明：`POST /edit-account-name/callback`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:5011` · `EditPopupUserResource`

### ACCOUNT-459 · USerAccountInfoResource.get（用途待确认）

- 接口声明：`GET /account-info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_login(allow_sub_account=False)
- 代码依据：`app/api/frontend/user.py:5046` · `USerAccountInfoResource`

### ACCOUNT-460 · 站内转账-检查收款人状态

- 接口声明：`GET /status`
- 输入字段：`account`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5067` · `UserStatusCheckResource`

### ACCOUNT-461 · UserCustomLayoutResource.get（用途待确认）

- 接口声明：`GET /custom-layouts`
- 输入字段：`business`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5101` · `UserCustomLayoutResource`

### ACCOUNT-462 · UserCustomLayoutResource.post（用途待确认）

- 接口声明：`POST /custom-layouts`
- 输入字段：`name`, `details`, `business`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5125` · `UserCustomLayoutResource`

### ACCOUNT-463 · UserCustomLayoutResource.put（用途待确认）

- 接口声明：`PUT /custom-layouts`
- 输入字段：`id`, `name`, `details`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5159` · `UserCustomLayoutResource`

### ACCOUNT-464 · UserCustomLayoutResource.patch（用途待确认）

- 接口声明：`PATCH /custom-layouts`
- 输入字段：`id`, `name`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5183` · `UserCustomLayoutResource`

### ACCOUNT-465 · UserCustomLayoutResource.delete（用途待确认）

- 接口声明：`DELETE /custom-layouts`
- 输入字段：`id`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5205` · `UserCustomLayoutResource`

### ACCOUNT-466 · UserActiveLayoutResource.get（用途待确认）

- 接口声明：`GET /active-layout`
- 输入字段：`business`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5234` · `UserActiveLayoutResource`

### ACCOUNT-467 · UserActiveLayoutResource.post（用途待确认）

- 接口声明：`POST /active-layout`
- 输入字段：`layout_id`, `business`
- 显式控制：require_login
- 代码依据：`app/api/frontend/user.py:5253` · `UserActiveLayoutResource`

### ACCOUNT-468 · 获取用户教育配置

- 接口声明：`GET /<string:path>`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user_education.py:18` · `UserEducationResource`

### ACCOUNT-469 · 检查是否存在用户教育配置

- 接口声明：`GET /check`
- 输入字段：`paths`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/frontend/user_education.py:33` · `UserEducationCheckResource`

### ACCOUNT-470 · CoinTypesResource.get（用途待确认）

- 接口声明：`GET /coin/type`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/account.py:20` · `CoinTypesResource`

### ACCOUNT-471 · AssetsResource.get（用途待确认）

- 接口声明：`GET /asset`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/account.py:85` · `AssetsResource`

### ACCOUNT-472 · CoinInformationResource.get（用途待确认）

- 接口声明：`GET /coin/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/account.py:98` · `CoinInformationResource`

### ACCOUNT-473 · SubAccountAuthResource.post（用途待确认）

- 接口声明：`POST /auth`
- 输入字段：`user_id`, `sub_users`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/sub_account.py:19` · `SubAccountAuthResource`

### ACCOUNT-474 · AuthUserResource.get（用途待确认）

- 接口声明：`GET /auth`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:60` · `AuthUserResource`

### ACCOUNT-475 · ApiAuthUserResource.get（用途待确认）

- 接口声明：`GET /api/auth`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:108` · `ApiAuthUserResource`

### ACCOUNT-476 · ApiV2AuthUserResource.get（用途待确认）

- 接口声明：`GET /api/v2/auth`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:128` · `ApiV2AuthUserResource`

### ACCOUNT-477 · ApiV2AuthStatusResource.get（用途待确认）

- 接口声明：`GET /api/v2/auth/status`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:141` · `ApiV2AuthStatusResource`

### ACCOUNT-478 · ContractApiAuthResource.get（用途待确认）

- 接口声明：`GET /contract/api/auth`
- 输入字段：`update_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:190` · `ContractApiAuthResource`

### ACCOUNT-479 · UserInfoResource.get（用途待确认）

- 接口声明：`GET /info`
- 输入字段：`user_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:228` · `UserInfoResource`

### ACCOUNT-480 · UserInfoCommentResource.get（用途待确认）

- 接口声明：`GET /info/for_comment`
- 输入字段：`user_ids`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:252` · `UserInfoCommentResource`

### ACCOUNT-481 · UserSearchResource.get（用途待确认）

- 接口声明：`GET /search`
- 输入字段：`keyword`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:291` · `UserSearchResource`

### ACCOUNT-482 · AdminUserListResource.get（用途待确认）

- 接口声明：`GET /admin-users`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:305` · `AdminUserListResource`

### ACCOUNT-483 · UserLocationSmsProviderResource.get（用途待确认）

- 接口声明：`GET /info/location-sms-provider`
- 输入字段：`user_ids`, `start_time`, `end_time`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:399` · `UserLocationSmsProviderResource`

### ACCOUNT-484 · AntiFraudUserFactsQueryResource.post（用途待确认）

- 接口声明：`POST /anti-fraud/user-facts/query`
- 输入字段：`user_ids`, `as_of_by_user`, `start_time_by_user`, `scopes`, `sample_limit`, `include_relation_2y`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:455` · `AntiFraudUserFactsQueryResource`

### ACCOUNT-485 · AntiFraudIdentityUsersQueryResource.post（用途待确认）

- 接口声明：`POST /anti-fraud/identity-users/query`
- 输入字段：`identity`, `identity_type`, `fact_type`, `as_of`, `window_days`, `offset`, `limit`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:473` · `AntiFraudIdentityUsersQueryResource`

### ACCOUNT-486 · UserRiskResource.post（用途待确认）

- 接口声明：`POST /risk`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:491` · `UserRiskResource`

### ACCOUNT-487 · ImUserResource.get（用途待确认）

- 接口声明：`GET /im`
- 输入字段：`app`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:504` · `ImUserResource`

### ACCOUNT-488 · ImPushResource.post（用途待确认）

- 接口声明：`POST /im/push`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:529` · `ImPushResource`

### ACCOUNT-489 · MakersResource.get（用途待确认）

- 接口声明：`GET /makers`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:540` · `MakersResource`

### ACCOUNT-490 · 查询所有配置了ws加速白名单的用户ID 

- 接口声明：`GET /ws-speed-whitelist`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:553` · `WSSpeedWhitelistResource`

### ACCOUNT-491 · 查询指定TAG类型的白名单用户 

- 接口声明：`GET /whitelist`
- 输入字段：`tag_type`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:576` · `WhitelistResource`

### ACCOUNT-492 · UserFeeRateResource.get（用途待确认）

- 接口声明：`GET /vip/perpetual/fee-rate`
- 输入字段：`user_id`
- 显式控制：需结合公共鉴权和调用入口确认
- 代码依据：`app/api/internal/user.py:604` · `UserFeeRateResource`

### ACCOUNT-493 · 修改账户设置 

- 接口声明：`POST /settings`
- 输入字段：`cet_discount_enabled`
- 显式控制：require_api_v2_auth(require_trading_permission=True)
- 代码依据：`app/api/v2/account.py:100` · `AccountSettingsAPIResource`

### ACCOUNT-494 · UserTradeFeeResource.get（用途待确认）

- 接口声明：`GET /trade-fee-rate`
- 输入字段：`market_type`, `market`
- 显式控制：require_api_v2_auth
- 代码依据：`app/api/v2/account.py:127` · `UserTradeFeeResource`

### ACCOUNT-495 · 子账号列表 

- 接口声明：`GET /subs`
- 输入字段：`sub_user_name`, `is_frozen`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/account.py:159` · `SubAccountResource`

### ACCOUNT-496 · 新增子账户 

- 接口声明：`POST /subs`
- 输入字段：`sub_user_name`, `permissions`, `remark`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_trading_permission=True); ns.use_kwargs(dict(sub_user_name=fields.String(required=True), permissions=fields.List(EnumField(SubA
- 代码依据：`app/api/v2/account.py:228` · `SubAccountResource`

### ACCOUNT-497 · 禁用子账户 

- 接口声明：`POST /subs/frozen`
- 输入字段：`sub_user_name`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_trading_permission=True)
- 代码依据：`app/api/v2/account.py:311` · `SubAccountFrozenResource`

### ACCOUNT-498 · 取消禁用子账户 

- 接口声明：`POST /subs/unfrozen`
- 输入字段：`sub_user_name`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_trading_permission=True)
- 代码依据：`app/api/v2/account.py:341` · `SubAccountUnFrozenResource`

### ACCOUNT-499 · 为子账户新增APIKEY

- 接口声明：`POST /subs/api`
- 输入字段：`sub_user_name`, `remark`, `ip_whitelist`, `trade_enabled`, `validity_period`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_trading_permission=True)
- 代码依据：`app/api/v2/account.py:371` · `SubAccountAPIResource`

### ACCOUNT-500 · 查询子账户的APIKEY

- 接口声明：`GET /subs/api`
- 输入字段：`page`, `limit`, `sub_user_name`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/account.py:434` · `SubAccountAPIResource`

### ACCOUNT-501 · 查询APIKEY的详细信息

- 接口声明：`GET /subs/api-detail`
- 输入字段：`api_id`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/account.py:467` · `SubAccountAPIDetailResource`

### ACCOUNT-502 · 子账号信息查询

- 接口声明：`GET /subs/info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth(allow_sub_account=True)
- 代码依据：`app/api/v2/account.py:494` · `SubAccountInfoResource`

### ACCOUNT-503 · 编辑APIKEY

- 接口声明：`POST /subs/edit-api`
- 输入字段：`sub_user_name`, `api_id`, `trade_enabled`, `ip_whitelist`, `remark`, `validity_period`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_trading_permission=True)
- 代码依据：`app/api/v2/account.py:514` · `SubAccountAPIEditResource`

### ACCOUNT-504 · 删除APIKEY

- 接口声明：`POST /subs/delete-api`
- 输入字段：`api_id`
- 显式控制：require_api_v2_auth(allow_sub_account=False, require_trading_permission=True)
- 代码依据：`app/api/v2/account.py:584` · `SubAccountAPIDeleteResource`

### ACCOUNT-505 · 母账号访问：可以在主账号和子账号之间、子账号和子账号之间进行双向划转 子账号访问：只能从自己的账户转出到母账号或其他子账号，不能转入

- 接口声明：`POST /subs/transfer`
- 输入字段：`from_user_name`, `to_user_name`, `from_account_type`, `to_account_type`, `ccy`, `amount`
- 显式控制：require_api_v2_auth(allow_sub_account=True, require_trading_permission=True)
- 代码依据：`app/api/v2/account.py:650` · `SubAccountTransferResource`

### ACCOUNT-506 · 子账号划转记录（包括子子划转记录） 

- 接口声明：`GET /subs/transfer-history`
- 输入字段：`sub_user_name`, `ccy`, `start_time`, `end_time`, `page`, `limit`
- 显式控制：require_api_v2_auth(allow_sub_account=True)
- 代码依据：`app/api/v2/account.py:780` · `SubAccountTransferHistoryResource`

### ACCOUNT-507 · SubAccountSpotBalanceResource.get（用途待确认）

- 接口声明：`GET /subs/spot-balance`
- 输入字段：`sub_user_name`, `ccy`
- 显式控制：require_api_v2_auth(allow_sub_account=True)
- 代码依据：`app/api/v2/account.py:867` · `SubAccountSpotBalanceResource`

### ACCOUNT-508 · 获取子账号余额(现货/杠杆/合约)

- 接口声明：`GET /subs/balance`
- 输入字段：`market_type`, `sub_user_name`, `market`
- 显式控制：require_api_v2_auth(allow_sub_account=False)
- 代码依据：`app/api/v2/account.py:910` · `SubAccountBalanceResource`

### ACCOUNT-509 · 账号信息查询

- 接口声明：`GET /info`
- 输入字段：本方法未提取到字段，需查阅原代码
- 显式控制：require_api_v2_auth(allow_sub_account=True)
- 代码依据：`app/api/v2/account.py:1033` · `AccountInfoResource`

## 相关测试文件（路径归类，未执行）

- `tests/api/admin/report/test_language_area_user_active_retain.py`
- `tests/api/admin/report/test_unkyc_deposit_withdrawal.py`
- `tests/api/admin/test_active_user_statistic.py`
- `tests/api/admin/test_mandatory_kyc_users.py`
- `tests/api/admin/test_user_education.py`
- `tests/api/admin/test_user_relation_upload.py`
- `tests/api/admin/test_users.py`
- `tests/api/common/test_api_v2_auth.py`
- `tests/api/frontend/test_kyc_liveness.py`
- `tests/api/frontend/test_user.py`
- `tests/api/frontend/test_user_api_auth.py`
- `tests/api/internal/test_user.py`
- `tests/api/v2/test_account.py`
- `tests/business/account_pl/test_account_pl.py`
- `tests/business/test_auth_page_config.py`
- `tests/business/test_kyc_id_number_validation.py`
- `tests/business/test_kyc_pro.py`
- `tests/business/test_kyc_status_masking.py`
- `tests/business/test_mandatory_kyc_user.py`
- `tests/business/test_sub_account.py`
- `tests/business/test_unkyc_deposit_withdrawal_report.py`
- `tests/business/test_user_sign_off.py`
- `tests/business/user/test_user_config_key_cache.py`
- `tests/business/user/test_user_repository_last_active.py`
- `tests/business/user_tag/test_reader.py`
- `tests/models/test_user_email.py`
- `tests/models/test_user_tag.py`
- `tests/schedules/test_kyc.py`
- `tests/schedules/test_nation_register_user.py`
- `tests/schedules/test_t31_user_tag_max_position_migration.py`
- `tests/scripts/test_migrate_kyc_country_settings.py`
- `tests/utils/test_user_agents_parsers.py`

## 待确认事项

- 哪些接口当前对外开放，哪些仅内部或管理端使用？
- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？
- 外部服务、异步消费及运行时开关有哪些额外约束？
- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。
