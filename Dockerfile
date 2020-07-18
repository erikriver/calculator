FROM node:12-alpine as frontend-builder

WORKDIR /frontend
COPY frontend /frontend
RUN npm run build


FROM python:3.8-alpine
WORKDIR /app
COPY backend /app
RUN apk add --no-cache --update --upgrade --virtual .build-deps gcc python3-dev libffi-dev openssl-dev libc-dev
RUN pip install -r requirements.txt
RUN apk del .build-deps gcc python3-dev libffi-dev openssl-dev libc-dev

COPY --from=frontend-builder /frontend/build /app/client

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]