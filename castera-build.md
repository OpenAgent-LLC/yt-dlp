
# Run local test of the modified Python entrypoint
```bash
python yt_dlp_start.py
```


# Build Docker
```bash
docker build --platform linux/amd64 -t docker-image:test .
```

# Run Docker image locally
```bash
docker run --platform linux/amd64 -p 9000:8080 docker-image:test
```

# Send a Curl request to the local Docker image
```bash
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"url":"https://vimeo.com/126035665"}'
```

