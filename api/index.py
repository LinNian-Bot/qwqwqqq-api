from fastapi import FastAPI

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Jump API",docs_url="/",openapi_url='/api/openapi.json',redoc_url=None)

@app.get("/{url:path}")
async def read_file(url: str):
    html = """
    <html>
    <h1>哎嘿，稍等片刻嗷</h1>
    <script type="text/javascript">
        (function(c,l,a,r,i,t,y){
            c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", "8izj4eyf6k");
    </script>
     <meta http-equiv="refresh" content="1;url={url}">
</html>
    """.replace("url={url}",f"url=https://cdn.jsdelivr.net/npm/qwqqwqqwqqwqqwqqwq/files/{url}")
    return HTMLResponse(content=html,status_code=200)
