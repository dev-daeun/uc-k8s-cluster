# udacity-capstone


### Infrastructure
* A load balancer
* VPC
* EC2 machines in VPC (EC2 machines are used as masters and nodes in k8s clusters.)

### Web application server
* nginx
* wsgi
* Flask

---


### CI & CD 
* Use Jenkins 

##### Steps of Continuous Integration
1. Lint Python Code & Dockerfile.
2. Setup Python environment.
3. Install dependencies of Flask application server.
4. Scans security vulnerabilities with [Snyk](https://support.snyk.io/hc/en-us/articles/360004032217-Jenkins-integration-overview).
4. Execute unit tests.

##### Steps of Continuous Deployment
Use blue/green deployment strategies

1. Update docker image with new version.
2. Deploy the image to blue cluster.
3. Execute health checks for the deployed version.
4. Update service to look up the updated blue cluster. (Now it's green one.)
5. If health checks fail, rollback 4th step and alert.

### Reference
* [Install a Kubernetes cluster on AWS using kops](https://kubernetes.io/docs/setup/production-environment/tools/kops/)
* [The simplest guide to using Blue/Green deployment in k8s](https://codefresh.io/kubernetes-tutorial/blue-green-deploy/)
* [Fully automated blue/green deployments in k8s with Codefresh](https://codefresh.io/kubernetes-tutorial/fully-automated-blue-green-deployments-kubernetes-codefresh/)
* [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
* [Nginx Upstream 성능최적화](https://brunch.co.kr/@alden/11)
* [Nginx config 정리](http://bong8nim.com/post/programming/etc/nginx-config-manual/)
* [Nginx full example](https://www.nginx.com/resources/wiki/start/topics/examples/full/)
