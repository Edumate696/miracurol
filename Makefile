SHELL = /bin/sh

WEB_ROOT = ./app/http/web-app

clean:
ifeq ($(OS), Windows_NT)
	@if exist "${WEB_ROOT}/dist" rmdir /s /q "${WEB_ROOT}/dist"
else
	@rm -rf "${WEB_ROOT}/dist"
endif

configure:
	@pip install -r "./requirements.txt"
	@cd "${WEB_ROOT}" && npm install

serve:
	@python -m app

build-web:
	@cd "${WEB_ROOT}" && npm run build

build: clean build-web