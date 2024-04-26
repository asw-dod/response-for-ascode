# Dependency

this program is requred to use many of the dependency. so, you can previosuly resolve dependency list below.

```
1. Docker
2. ubuntu os is prefered, if you are available.
```

# How to run this program?

```sh
# First. pull for downloading container
$ ./scripts/pull.sh 

# Seconds. Execute in shell file with your account information in ascode database.
# It's all.
$ ./exec.sh {YOUR_ASCODE_ID} {YOUR_ASCODE_PW}
```

# Parameter from Environment for Container

Name|Type|Description
:---:|:---:|:---:
`ASCODE_USERID`|`str`|user id in ascode
`ASCODE_USERPW`|`str`|user password in ascode
`DURATION_PER_CHECK`|`float`|duration of time for repeat(unit: sec) 


