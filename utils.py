import re
from .analysis import analyze

def prettify_search_result_html(html: str, query: str, highlight: bool, retry: bool) -> str:

    if html is None:
        return ""

    if not retry and highlight:
        html = re.sub(r"%s" % re.escape(query), f"<mark>{query}</mark>", html, flags=re.I)

    if retry and highlight:
        query_tokens    = set(analyze(query, lowercase=False))
        for qt in query_tokens:
            html = re.sub(r"\b%s\b" % re.escape(qt), f"<mark>{qt}</mark>", html, flags=re.I)

        html = re.sub("\x1f(?:\x1f)*", "<hr/>", html)
        html = re.sub(r"(?:<[hb]r/?>\w*)*$", "", html)

    return html
