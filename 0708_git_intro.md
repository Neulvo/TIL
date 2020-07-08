# git intro

## local git

1. git 다운로드 및 설치
2. 초기화 $ git init
   1. 실제로는 .git/폴더가 생성됨
   2. 버전관리가 시작됨
   3. 리포(repository)라고 부름

2. 서명 설정
   1. `$ git config --global user.name `
      `"name"`
   2. `$ git config --global user.email `
      `"email@mail"`

3. 리포의 상태 보기 `$ git status`
4. stage에 올리기 `$ git add`
   1. 특정 파일만 올리기 `$ git add <filename>`
   2. 내 위치(폴더) 다 올리기 `$ git add .`
5. snapshot(사진) 찍기 `$ git commit`
6. 로그(사진첩) 보기 `$ git log`

# 집 커퓨터 세팅

1. git 다운로드 및 설정
2.  `$ git config -- global ....`

3. `$ git clone <URL>`

# github

1. 원격저장소(remote repository) 생성

2. local repo => remote repo 연결하기 `$ git
   remote add origin <URL>`

3. 로컬 커밋들을 리모트로 보내기 `$
   git push origin master`

4. `$ git push == git push origin
   master`로 단축 명령하기 `$ git push
   -u origin master`

5. 다른 컴퓨터에서 remote repo **최초로** 받아오기

   `$ git clone <URL>`

6. 이후 remote repo 변경사항을 local repo에서
   반영하기 `$ git pull`

# TIL 관리 시나리오

1. 멀캠에 온다.
2. `$ git pull`
3. 열-공
4. 중간 중간 `$git add.` & `$ git commit`
5. 집 가기 전에 `$ git push`
6. 집 도착
7. `$ git pull`
8. 복습 및 자습 (`$ git commit`)
9. 마지막으로 `$ git push`
10. 수면
11. 1번으로