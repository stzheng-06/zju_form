# zju_form

中英双语匿名问卷。`index.html` 将答卷写入 Supabase；`export.html` 为管理员登录后导出 CSV 的页面。

## Supabase 设置

数据库建表和权限 SQL 在 `supabase_setup.sql`。请将文件中的 `REPLACE_WITH_YOUR_SUPABASE_LOGIN_EMAIL` 替换为管理员 Supabase Auth 邮箱，然后在 SQL Editor 重新运行。该策略只允许此邮箱读取答卷。

在 Supabase Dashboard → Authentication → Users 中创建或确认管理员登录用户。之后在 `export.html` 使用该邮箱和密码登录并下载 CSV。登录凭据不会保存到浏览器存储。

Project URL 和 publishable key 位于 HTML 中。publishable key 供公开网页使用；不要提交 secret key、service_role key 或数据库密码。匿名用户只能新增答卷，不能读取。

GitHub Pages：Settings → Pages → Deploy from a branch → `main` → `/(root)`。
