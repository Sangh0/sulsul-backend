CLASSIFY_IMAGE_DESC = """
AI 모델로 이미지를 술+안주로 분류

- 먼저 파일업로드를 통해 AWS S3 이미지 url을 받아와서 인풋으로 넣어야합니다.
- 추론 결과는 안주, 술 모두 리스트로 내려갑니다. (모델이 여러개로 추론가능)
- 안주, 술 모두 빈 리스트일 수 있습니다. 이러면 잘못된 사진이거나 인식 실패한 경우입니다.
- 여기서 받아진 결과를 피드 작성에서 classfiy_tags로 넘겨주시면 됩니다.
"""

CREATE_FEED_DESC = """
피드 생성
*로그인 필수*

- represent_image : 피드 대표 이미지 url을 images 중 하나로 넣어주세요
- classify_tags : 모델이 추론한 음식 태그입니다. 순서상관없이 넣어주세요
- user_tags : 유저가 추가적으로 입력한 태그입니다. nullable
"""

GET_FEED_DESC = """
피드 상세 조회

- 로그인 되어있으면 좋아요를 표시해줍니다.
- 로그인 없이도 API Call 가능합니다. 이런 경우 is_liked는 무조건 False로 내려갑니다.
"""

GET_RELATED_FEEDS_DESC = """
관련 피드 조회

- CursorPageResponse에 내용물은 스키마가 없어서 따로 첨부합니다.
RelatedFeedResponse
    feed_id: Int (not-null)
    title: String (not-null)
    represent_image: String (not-null)
    score: Double (not-null)
    user_tags: List<String> (*nullable*)
    classify_tags: List<String> (not-null)
    is_liked: Boolean = False (not-null)
"""

GET_FEEDS_BY_ME_DESC = """
마이페이지 - 내가 쓴 피드 조회
*로그인 필수*

- 무한 스크롤
"""

GET_FEEDS_LIKED_BY_ME_DESC = """
마이페이지 - 좋아요 표시한 피드 조회
*로그인 필수*

- 무한 스크롤
"""

DELETE_FEED_DESC = """
피드를 삭제(소프트 딜리트)
*로그인 필수*

- 관련 좋아요는 영구 삭제됩니다.
- 포함되어있던 댓글은 소프트 딜리트 됩니다.
"""

GET_RANDOM_FEEDS_DESC = """
랜덤 피드 조회

- exclude_feed_ids는 랜덤 피드 중복 조회를 방지하기 위해서 이전 응답에 내려갔던 피드들 id를 콤마로 이어서 넣어줍니다. (공백 포함 되면 안 됨)
  조회 후 받은 ids_string을 고대로 넣어주시면 해당 피드들은 제외하고 랜덤 피드가 포함내려갑니다.
  ex) 최초 조회 빈 스트링 / 2번째 조회 2,3,4,5,6 / 3번째 조회 2,3,4,5,6,7,8,9,10 ...
- 로그인 되어있으면 좋아요도 표시됩니다. 없으면 항상 false
"""
