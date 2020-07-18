# git 常用操作

## 清空所有远端 commit

```sh
git checkout --orphan latest_branch
git add -A
git commit -m "commit message"
git branch -D master
git branch -m master
git push -f origin master
```