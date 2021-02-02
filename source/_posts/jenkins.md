---
title: 升级jenkins插件
date: 2021-02-02 16:25:49
tags:
- atom
- github
- hexo
- travis
categories:
- Diary
---

【Brew】openshift jenkins-2-container
https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=67183

不同版本的image有不同的tag
在build log中可以看到plugin版本
【cgit】
http://pkgs.devel.redhat.com/cgit/containers/openshift-jenkins-2/

【Brew】jenkins-2-plugins
https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=63638
不同的plugin build有不同的tag
【cgit】
http://pkgs.devel.redhat.com/cgit/rpms/jenkins-2-plugins/



# Web UI

https://console-openshift-console.apps.ocp4.prod.psi.redhat.com/k8s/ns/art-cd/tekton.dev~v1beta1~Pipeline

# Console

1. 登陆PSI
oc login --token=** --server=https://api.ocp4.prod.psi.redhat.com:6443

2. 切换到art-cd
oc project art-cd

3. 开始build
tkn pipeline start <pipeline>

【jenkins-plugin】
tkn pipeline start jenkins-plugins -p jenkins-version=2.235.5 -p ocp-branch=rhaos-4.6-rhel-8 -p build-url=<url>

【bump jenkins】
tkn pipeline start jenkins-bump-version -p jenkins-version=2.235.5 -p ocp-branch=rhaos-4.6-rhel-8

4. 跟踪build log
tkn pipelinerun logs -f <pipelinerun ID>


tkn task list
tkn pipeline list
tkn pipelinerun list
tkn pipelinerun logs -f <pipelinerun ID>
