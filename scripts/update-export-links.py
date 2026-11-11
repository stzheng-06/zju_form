from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
page = root / "index.html"
html = page.read_text(encoding="utf-8")
html = re.sub(r"\.preview-note\{[^}]*\}", "", html)
html = re.sub(r'<div class="preview-note">.*?</div>', "", html, count=1)
html = html.replace("'完成预览':'下一步'", "'提交问卷 / Submit':'下一步 / Next'")
html = re.sub(r'<p class="foot">.*?</p>', '<p class="foot">请避免填写您或他人的姓名、联系方式等可识别信息。 / Avoid identifying details in open answers. <a href="./export.html">管理员导出 CSV / Admin CSV export</a></p>', html, count=1)
html = html.replace("预览完成，答卷未保存。", "匿名答卷已提交 / Your anonymous response has been submitted.")
page.write_text(html, encoding="utf-8")

readme = """# zju_form

中英双语匿名问卷。`index.html` 将答卷写入 Supabase；`export.html` 为管理员登录后导出 CSV 的页面。

## Supabase 设置

数据库建表和权限 SQL 在 `supabase_setup.sql`。请将文件中的 `REPLACE_WITH_YOUR_SUPABASE_LOGIN_EMAIL` 替换为管理员 Supabase Auth 邮箱，然后在 SQL Editor 重新运行。该策略只允许此邮箱读取答卷。

在 Supabase Dashboard → Authentication → Users 中创建或确认管理员登录用户。之后在 `export.html` 使用该邮箱和密码登录并下载 CSV。登录凭据不会保存到浏览器存储。

Project URL 和 publishable key 位于 HTML 中。publishable key 供公开网页使用；不要提交 secret key、service_role key 或数据库密码。匿名用户只能新增答卷，不能读取。

GitHub Pages：Settings → Pages → Deploy from a branch → `main` → `/(root)`。
"""
(root / "README.md").write_text(readme, encoding="utf-8")
