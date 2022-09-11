# aws-services-template
Amazon Web Service knowledge repository for projects and template for future work. Initial projects are meant to be used for simple designs discussions. Forthcoming projects will increase the complexity of the below via three measures: reliability, maintainability and scalability.

_Reliability_ - what would a solution with a million requests need to look like on an AWS service?</br>
_Maintainability_ - what would a coder-friendly solution with a team of 5, 10, 15 look like on AWS?</br>
_Scalability_ - how would a service/system cope with extended functionality in both its code design and its use of compute and storage resources?</br>

[AWS's Architecture Center](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all) is the go-to source for much of the above.</br>
[Designing Data-Intensive Applications by Martin Kleppmann](https://martin.kleppmann.com/) is used as a reference and inspiration for much of what is contained in this repo and many others.

## Table of Contents

1. Getting Around
2. Projects
  </br>a. Metropolitan Museum of Art API [Lambda, S3]

## Getting Around

  _.config_: directory containing configuration for local setup</br>
  _.build_: scripts for build process (Docker images, powershell executables)</br>
  _doc_: documentation for aws-services-template repository</br>
  _samples_: 'Hello World'-esque work</br>
  _src_: source code for repo</br>
  _test_: unit-tests, integration-tests</br>
  _tools_: scripts used to automate tasts .sh and .cmd files should go here.</br>

## Metropolitan Museum of Art API - [Lambda, S3] 

[API documentation here](https://metmuseum.github.io/)</br>
This simple service is used to demonstrate a Lambda job sending a request to MoMA's API, getting a JSON. The service retrieves the resultant image at the URL returned from the API and stores it into the S3. 
The second function of the service retrieves the image within S3 runs a Quad-Tree compression and stores the branch-leaf data into an RDS
