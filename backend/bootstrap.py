"""Generate auditable as-built inventories without loading the business application."""
import ast
import collections
import subprocess

from . import indexer, settings, store


def clean(value):
    return str(value).replace('|', ' / ').replace('\n', ' ')[:180]


def generate():
    settings.DOCS.mkdir(parents=True, exist_ok=True)
    version = subprocess.check_output(['git', '-C', str(settings.REPO), 'rev-parse', 'HEAD'], text=True).strip()
    groups = collections.defaultdict(list)
    counts = collections.Counter()
    tests = collections.defaultdict(list)
    for path, actual in indexer.safe_files():
        if not path.endswith('.py'):
            continue
        module = indexer.module_for(path)
        counts[module] += 1
        if path.startswith('tests/'):
            tests[module].append(path)
        if not path.startswith('app/api/'):
            continue
        try:
            tree = ast.parse(actual.read_text())
        except (SyntaxError, UnicodeError):
            continue
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            routes = []
            for d in node.decorator_list:
                if isinstance(d, ast.Call) and isinstance(d.func, ast.Attribute) and d.func.attr == 'route' and d.args and isinstance(d.args[0], ast.Constant):
                    routes.append(str(d.args[0].value))
            if not routes:
                continue
            for method in node.body:
                if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) or method.name not in ('get', 'post', 'put', 'delete', 'patch'):
                    continue
                decorators = [ast.unparse(x) for x in method.decorator_list]
                auth = [x for x in decorators if any(word in x for word in ('auth', 'permission', 'lock_request', 'login'))]
                keys = []
                for d in method.decorator_list:
                    if isinstance(d, ast.Call) and isinstance(d.func, ast.Attribute) and d.func.attr == 'use_kwargs':
                        for sub in ast.walk(d):
                            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) and sub.func.id == 'dict':
                                keys += [kw.arg for kw in sub.keywords if kw.arg]
                description = ast.get_docstring(method) or node.name + '.' + method.name + '（用途待确认）'
                line = min([method.lineno] + [d.lineno for d in method.decorator_list])
                groups[module].append((path, line, node.name, method.name.upper(), ', '.join(routes), description, keys, auth))
    domains = indexer.DOMAINS + [('platform', '平台与其他能力', ())]
    overview = [
        '# CoinEx 后端 · 现状需求总览', '',
        '> 文档性质：根据当前代码反推的需求草稿，非原始 PRD。产品目标、线上启用范围、合规规则均需负责人确认。',
        f'> 基线提交：`{version}`；索引同时保存工作区文件内容哈希。生成时间：{store.now()}', '',
        '## 使用对象与业务边界', '',
        '仓库提供网站、开放 API、管理后台及内部服务接口。业务代码包含账户、资产、交易、安全、运营等模块。',
        '本清单依据接口声明及方法说明生成；接口存在不等于线上已启用。外部交易撮合、钱包执行和生产配置不在本次验证范围内。', '',
        '## 模块范围', '', '| 业务模块 | Python 文件 | 接口方法 | 测试文件 |', '|---|---:|---:|---:|',
    ]
    for key, title, _ in domains:
        entries = groups[key]
        overview.append(f'| {title} | {counts[key]} | {len(entries)} | {len(tests[key])} |')
        doc = [f'# {title} · 接口需求清单', '',
               '> 静态提取草稿。业务分组按路径关键词推断；接口用途来自代码注释，尚未逐条人工评审。',
               f'> 基线提交：`{version}`', '',
               '## 范围与验收方法', '',
               '以下列出该模块的接口声明、输入字段和显式控制装饰器。路由为局部声明，完整 URL 还需结合命名空间注册与网关配置。',
               '验收建议：逐条确认访问主体、输入边界、权限失败、成功响应、异常分支及重复请求行为。缺少装饰器记录不代表无鉴权。', '',
               '## 已声明能力', '']
        for i, (path, line, symbol, verb, route, description, keys, auth) in enumerate(entries, 1):
            doc += [f'### {key.upper()}-{i:03d} · {clean(description)}', '',
                    f'- 接口声明：`{verb} {clean(route)}`',
                    f'- 输入字段：{", ".join("`"+x+"`" for x in keys) if keys else "本方法未提取到字段，需查阅原代码"}',
                    f'- 显式控制：{clean("; ".join(auth)) if auth else "需结合公共鉴权和调用入口确认"}',
                    f'- 代码依据：`{path}:{line}` · `{symbol}`', '']
        doc += ['## 相关测试文件（路径归类，未执行）', ''] + [f'- `{p}`' for p in tests[key]]
        doc += ['', '## 待确认事项', '',
                '- 哪些接口当前对外开放，哪些仅内部或管理端使用？',
                '- 代码现状与产品期望是否一致？历史兼容行为是否继续保留？',
                '- 外部服务、异步消费及运行时开关有哪些额外约束？',
                '- 现有测试实际覆盖哪些验收条件？必须阅读断言或运行后才能确认。', '']
        (settings.DOCS / f'inventory-{key}.md').write_text('\n'.join(doc))
    overview += ['', '## 跨模块需求建议（待确认）', '',
                 '- 产品规则应明确访问主体、前置条件、成功状态、失败状态和审计要求。',
                 '- 资金和订单写操作需单独确认并发、重试、部分成功及外部服务超时的预期。',
                 '- 每条正式需求关联代码版本、负责人、验收用例；本版所有文档默认未确认。', '',
                 '## 已深入整理的流程', '',
                 '- 兑换与闪兑：询价、订单提交、状态展示、查询过滤、并发测试。',
                 '- 安全资料重置：不同重置类型的行为、操作记录与登录态清理边界。', '',
                 '## 证据范围', '',
                 '从 Git 已跟踪的应用、测试、迁移和架构说明中提取；不读取运行环境配置，不运行业务应用，不连接生产数据库。',
                 '测试文件存在不代表测试通过；代码行为不自动构成已确认的产品承诺。', '']
    (settings.DOCS / '00-overview.md').write_text('\n'.join(overview))
    return {'modules': len(domains), 'endpoints': sum(map(len, groups.values())), 'files': sum(counts.values())}


if __name__ == '__main__':
    store.init()
    print(generate())
    print(indexer.sync())
