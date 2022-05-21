# Github Page for YC Note Blog

**You must clone `ycnote_raw_source`**

## Docker

```
# docker build -t ycnote:0.0.1 .
docker load --input ycnote.tar

docker run -i -t -v $PWD:/YCNote ycnote:0.0.1 /bin/bash
```

```
cd YCNote

cd ycnote_raw_source/raw_markdown
python convert_raw.py --name Generative
```





## how to publish github page

- `make html`
- `make serve`
- `make github`
