from pathlib import Path, PosixPath
import pickle
import ast
import gzip


class ScrapyHttpCacheParser(object):
    def __init__(self, page_dir: PosixPath | Path | str):
        if isinstance(page_dir, str):
            self.page_dir = Path(page_dir)
        else:
            self.page_dir = page_dir
        self.data = {}

    def parse_cache(self) -> dict:
        # meta
        self.data["meta"] = self._parse_meta()
        self.data["pickled_meta"] = self._parse_pickled_meta()
        # request
        self.data["request_body"] = self._parse_request_body()
        self.data["request_headers"] = self._parse_request_headers()
        # response
        self.data["response_body"] = self._parse_response_body()
        self.data["response_headers"] = self._parse_response_headers()
        return self.data

    def list(self):
        return list(self.page_dir.iterdir())

    def _parse_pickled_meta(self):
        path = self.page_dir / "pickled_meta"
        with open(path, "rb") as f:
            pickled_meta = pickle.loads(f.read())
        return pickled_meta

    def _parse_meta(self):
        path = self.page_dir / "meta"
        with open(path, "r") as f:
            # Note:
            # The line {'url': 'https://example.com'} has single quotes,
            # that cannot be handled by json.loads.
            # This is why ast.literal_eval can be used.
            meta = ast.literal_eval(f.read())
        return meta

    def _parse_request_body(self):
        path = self.page_dir / "request_body"
        with open(path, "r") as f:
            request_body = f.read()
        return request_body

    def _parse_request_headers(self):
        path = self.page_dir / "request_body"
        with open(path, "r") as f:
            request_headers = f.read()
        return request_headers

    def _parse_response_headers(self):
        path = self.page_dir / "response_headers"
        with open(path, "r") as f:
            response_headers = f.read()
        return response_headers

    def _parse_response_body(self):
        path = self.page_dir / "response_body"
        try:
            with open(path, "r") as f:
                response_body = f.read()
        except:
            with gzip.open(path, "rt", encoding="utf-8") as f:
                response_body = f.read()
        return response_body
