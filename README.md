# uipath-webhook-receiver-on-aws

## Path to deploy

* install serverless framework
```console
$ npm install -g serverless
```

* cron this repository and install serverless-python-requirements
```console
$ git clone <this repository>
$ cd <this clone directory>
$ npm install --save serverless-python-requirements
```

* modify config.json
```console
$ vim congig.json
```

* deploy it
```console
$ serverless deploy [--stage production]
```

## Use case

### Ticket Service Integration
![Use Case #1](https://user-images.githubusercontent.com/129797/51825579-6a43c100-2328-11e9-821f-18784398d09b.png)

### Slack (Slask Command) Integration
![Use Case #2](https://user-images.githubusercontent.com/129797/51825724-b858c480-2328-11e9-93bc-bd87aeaad2a9.png)

### IoT Enterprise Button Integration
![Use Case #3](https://user-images.githubusercontent.com/129797/51825742-c1e22c80-2328-11e9-8b3b-4d9a214a0ee9.png)

### HTML Form Integration
![Use Case #4](https://user-images.githubusercontent.com/129797/51825755-cc9cc180-2328-11e9-812f-f4f5df68cd7a.png)


* ticket service
* html form
* aws iot button
* slack command

## To Do

* ServiceNow integration
* Wrike integration
* Slack integration