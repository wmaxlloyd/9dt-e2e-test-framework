IMAGE_TAG=9dt-e2e-tests
CONTAINER_NAME=${IMAGE_TAG}_container

build: e2e_tests.py src/
	docker rmi ${IMAGE_TAG} || true
	docker build -t $(IMAGE_TAG) .

run:
	docker rm ${CONTAINER_NAME} || true
	docker run -d --name="${CONTAINER_NAME}" "${IMAGE_TAG}" python e2e_tests.py
	docker logs -f ${CONTAINER_NAME}

clean:
	docker stop ${CONTAINER_NAME} || true
	docker rmi ${IMAGE_TAG} || true
	docker rm ${CONTAINER_NAME} || true
	rm -rf ./artifacts || true

archive:
	docker cp ${CONTAINER_NAME}:/home/artifacts ./artifacts

enter:
	docker run -it $(IMAGE_TAG) /bin/sh

test:
	echo "Testing"