# zju_form

中英双语匿名问卷。`index.html` 提交答卷至 Supabase；答卷保存在 `survey_responses` 表，匿名访问只开放新增权限，不开放读取。

## Supabase 初始化

在项目的 SQL Editor 中运行 `supabase_setup.sql`。Project URL 与 publishable key 已配置在 `index.html`。不要把 secret key 或 service_role key 放入网页或仓库。

提交表单后，在 Supabase Dashboard 的 Table Editor 查看或导出答卷。GitHub Pages 发布前，将仓库的 Pages source 设为 `main` 分支的根目录。
