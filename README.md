# Github Page for YC Note Blog

**You must clone `ycnote_raw_source`**

## Docker

```
docker build -t ycnote:0.0.1 .
docker run -i -t -v $PWD:/YCNote ycnote:0.0.1 /bin/bash
```

## how to publish github page

- `make html`
- `make serve`
- `make github`
