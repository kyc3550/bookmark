from django.db import models
from django.urls import reverse
# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 사용한다.
# 데이터를 객체화 해서 다루겠다.
# 모델 = 데이터베이스의 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값
class Bookmark(models.Model):
    site_name=models.CharField(max_length=100)
    url=models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류(숫자,문자..)
    # 2. 제약 사항을 결정 (몇 글자까지)
    # 3. Form의 종류
    # 4. Form에서 제약사항

    def __str__(self):  #bookmark필드의 이름을 바꿔준 메서드
        return "이름 : " +self.site_name+", 주소 : "+ self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
# 모델을 만들었다 => 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정
# makemigrations => 모델의 변경 사항을 추정해서 기록
# 마이그레이션(migrate) => 데이터 베이스에 모델의 내용을 반영(테이블 생성)