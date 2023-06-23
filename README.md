# atop

## How to Start

1. activate venv

```bash
python -m venv venv
source venv/Scripts/activate
```

2. dependency install

```bash
pip install -r requirements.txt
```

## How to Work

1. **할일을 issue로 등록한다.**
    이슈에 프로젝트, assignee, 마일스톤 선택    
    이슈 내용으로는 해당 할일에서 세부적으로 필요한 구현내용 등을 적는다
    
2. **할일 시작**
  이슈넘버로 브랜치 만들고 작업, 프로젝트에서 이슈 status ⇒ In Progress
  예시 : feat/#[이슈넘버]-[단어]
  ```bash
  git checkout -b feat/#1-signin
  ```

4. **할일 끝, pull request**
  할일이 끝낫으면 push하고, develop브랜치로 pull request를 작성한다.
  merge한다면 꼭 팀원들에게 알리고 다른사람들은 pull해야한다.
