

### Build docker image

```
docker build -t selenium-python .   
```

### Run this to execute the `test.py` file in `/` dir

```
docker run --rm -v $(pwd):/tmp selenium-python python test.py
```

### Run this to manually test by adding pwd inside docker

```
docker run --rm -it -w /usr/workspace -v $(pwd):/usr/workspace selenium-python bash
```