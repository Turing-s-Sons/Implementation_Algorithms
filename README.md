# Implementation_Algorithms
Implementation_Algorithms

- [x] Линейная регрессия 
- [x] Градиентный спуск 
- [x] K-ближайших соседей (K-Nearest Neighbors) 
- [x] Метод опорных векторов (Support Vector Machines) 
- [x] Decision Tree
      
- [ ] Нейронные сети
  - [x] Основы
  - [ ] Forward Propagation и Back Propagation 


```mermaid
gitGraph
    commit id: "Initial Commit"
    branch develop
    checkout develop
    commit id: "Setup Project Structure"
    branch feature/auth
    checkout feature/auth
    commit id: "Implement Login"
    commit id: "Implement Logout"
    checkout develop
    merge feature/auth tag: "v1.1"

    branch feature/ui
    checkout feature/ui
    commit id: "Create UI Mockups"
    commit id: "Develop UI Components"
    checkout develop
    merge feature/ui tag: "v1.2"

    branch hotfix/critical-bug
    checkout hotfix/critical-bug
    commit id: "Fix Critical Bug"
    checkout develop
    merge hotfix/critical-bug tag: "v1.2.1"
    checkout main
    merge develop tag: "v1.2.1"

    branch feature/api
    checkout feature/api
    commit id: "Setup API Framework"
    commit id: "Add Authentication API"
    checkout develop
    merge feature/api tag: "v1.3"

    branch feature/notifications
    checkout feature/notifications
    commit id: "Add Notification System"
    commit id: "Integrate Notifications with UI"
    checkout develop
    merge feature/notifications tag: "v1.4"

    checkout main
    merge develop tag: "v1.4"
    commit id: "Prepare Release v1.4"

    branch feature/testing
    checkout feature/testing
    commit id: "Setup Unit Tests"
    commit id: "Add Integration Tests"
    checkout develop
    merge feature/testing tag: "v1.5"

    checkout main
    merge develop tag: "v1.5"
    commit id: "Final Release v1.5"
```
