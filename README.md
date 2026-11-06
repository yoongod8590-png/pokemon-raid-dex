# Pokémon GO 레이드 도감 — 자동 뉴스 갱신 PWA

## GitHub Pages 배포
1. GitHub에서 새 **Public** 저장소를 만듭니다. 이 폴더의 **내용물** 전체(`index.html`, `data/`, `.github/` 등)를 저장소 루트에 업로드합니다. GitHub Pages는 무료 계정에서 일반적으로 공개 저장소가 필요합니다.
2. Settings → Pages → Build and deployment → Source → GitHub Actions.
3. Actions → Daily Pokemon GO news refresh → Run workflow에서 기본 브랜치를 선택해 첫 수집과 배포를 실행합니다. 몇 분 뒤 `https://사용자명.github.io/저장소명/` 주소로 접속합니다. URL은 계정과 저장소명에 따라 결정되며 여기서 미리 발급할 수 없습니다.
4. Android Chrome에서 주소를 열고 메뉴 → 홈 화면에 추가 / 앱 설치를 선택합니다. HTTPS에서 서비스 워커가 동작합니다.
5. 이후 매일 06:00 KST에 자동 실행을 시도합니다. GitHub Actions 예약 실행은 지연되거나 비활성화될 수 있습니다.

## 중요한 데이터 구분
- 자동 업데이트는 **Google News RSS에서 포켓몬 GO 레이드 관련 기사 제목과 링크를 가져오는 기능**입니다. 공식 발표 여부, 정확성, 중복 여부는 자동 검증하지 않습니다.
- **레이드 순위·기술·전체 포켓몬 데이터는 자동 갱신되지 않습니다.** 기존 45종의 편집된 참고 점수이며 실제 DPS 순위가 아닙니다.
- RSS 실패 시 이전 뉴스 목록을 유지하고 실패 상태를 표시합니다.
- 개인 도감은 기기 브라우저의 localStorage에만 저장됩니다. 다른 기기와 동기화되지 않습니다. 브라우저 데이터 삭제 시 사라질 수 있으므로 JSON 백업을 이용하세요.
- `data/updates.json`은 Actions가 갱신하며 같은 작업이 최신 JSON을 포함한 사이트를 GitHub Pages에 배포합니다. 무료 호스팅 및 외부 서비스 정책은 변경될 수 있습니다.

