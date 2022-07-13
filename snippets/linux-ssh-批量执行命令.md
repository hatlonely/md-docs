# linux ssh 批量执行命令

```shell
for i in $(cat machine.txt); do
ssh -o StrictHostKeyChecking=no -i weboffice-dingding-cn-shanghai.pem $i /bin/bash << EOF
  if [[ \$(rpm -qa systemd) < "systemd-219-67" ]]; then
  yum update -y systemd && systemctl daemon-reexec;
  fi
EOF
echo upgrade $i done
sleep 1
done
```