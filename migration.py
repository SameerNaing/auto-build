from sqlalchemy import create_engine
from datetime import datetime
from typing import List

from db.core import get_session
from db.models import Base, BuildQueueModel, DriveStoreModel
from common.constants import BUILDING, QUEUE_CURRENT, QUEUE_PENDING, DONE, FAILED
# from db.helpers import delete_done_queue


def create_db():
    engine = create_engine("sqlite:///db/autobuild.db")
    Base.metadata.create_all(engine)


def add():
    with get_session() as session:
        session.add_all([
            BuildQueueModel(
                commit_hash="2930cdc516db3226bf13df4eb3a8805fd3e6db75",
                committer_email="naing.ye.oo@flymya.co",
                commit_date=datetime.fromisoformat(
                    "2022-10-03 15:51:48.000000"),
                branch_name="test/coffee",
                build_android=True,
                android_version_code=2000800200,
                android_version_number="2.8.2",
                build_ios=True,
                ios_version_number="2.8.2",
                ios_build_number=2,
                ios_building_status=BUILDING,
                queue_status=QUEUE_CURRENT,
                build_started_at=datetime.now()

            ),
            BuildQueueModel(
                commit_hash="2930cdc516db3226bf13df4eb3a8805fd3e6db75",
                committer_email="naing.ye.oo@flymya.co",
                commit_date=datetime.fromisoformat(
                    "2022-12-03 15:51:48.000000"),
                branch_name="test/tea",
                build_android=False,
                android_version_code=2000800200,
                android_version_number="2.8.2",
                build_ios=True,
                ios_version_number="2.8.2",
                ios_build_number=2,
                queue_status=QUEUE_PENDING
            ),
            BuildQueueModel(
                commit_hash="2930cdc516db3226bf13df4eb3a8805fd3e6db75",
                committer_email="naing.ye.oo@flymya.co",
                commit_date=datetime.fromisoformat(
                    "2022-12-03 15:51:48.000000"),
                branch_name="test/chocolate",
                build_android=False,
                android_version_code=2000800200,
                android_version_number="2.8.2",
                build_ios=True,
                ios_version_number="2.8.2",
                ios_build_number=2,
                queue_status=QUEUE_PENDING
            ),
            BuildQueueModel(
                commit_hash="2930cdc516db3226bf13df4eb3a8805fd3e6db75",
                committer_email="naing.ye.oo@flymya.co",
                commit_date=datetime.fromisoformat(
                    "2022-12-03 15:51:48.000000"),
                branch_name="test/juice",
                build_android=False,
                android_version_code=2000800200,
                android_version_number="2.8.2",
                build_ios=True,
                ios_version_number="2.8.2",
                ios_build_number=2,
                queue_status=QUEUE_PENDING
            ),
            BuildQueueModel(
                commit_hash="2930cdc516db3226bf13df4eb3a8805fd3e6db75",
                committer_email="naing.ye.oo@flymya.co",
                commit_date=datetime.fromisoformat(
                    "2022-09-05 15:51:48.000000"),
                branch_name="test/coffee",
                build_android=True,
                android_version_code=2000800200,
                android_version_number="2.8.2",
                build_ios=True,
                ios_version_number="2.8.2",
                ios_build_number=2,
                queue_status=QUEUE_PENDING
            ),

        ])
        # session.add(BuildQueueModel(
        #     commit_hash="2930cdc516db3226bf13df4eb3a8805fd3e6db75",
        #     committer_email="naing.ye.oo@flymya.co",
        #     commit_date=datetime.fromisoformat("2022-09-03 15:51:48.000000"),
        #     branch_name="release",
        #     build_android=True,
        #     android_version_code=2000800200,
        #     android_version_number="2.8.2",
        #     android_building_status=DONE,
        #     build_ios=True,
        #     ios_building_status=FAILED,
        #     ios_version_number="2.8.2",
        #     ios_build_number=2,
        #     queue_status=QUEUE_CURRENT,
        #     build_started_at=datetime.fromisoformat(
        #         "2022-09-03 23:51:48.000000")
        # ))
        session.commit()


def delete_all():
    # session, Sesssion = get_session()
    with get_session() as session:
        queues = session.query(BuildQueueModel).all()
        drive = session.query(DriveStoreModel).all()

        for data in drive:
            session.delete(data)
            session.commit()

        for data in queues:
            session.delete(data)
            session.commit()


def add_drive_db():
    with get_session() as session:
        session.add_all([
            DriveStoreModel(
                file_id="AAbDypDjPa3posHww2_1-IKimC3fCmqI3gVwwIInJKhGr-0fsGaQEQgfVLm0o6Djq7gw4mmLRxNNpWybt7HNAWcnPUHSxeHqQJoNxS0Rn0cWuj21Jq_px9ptUJDUA2SgxWUupijfovp_yAMQNBZeVqJEhYruAxde2fxg-mQ5AO5e9wpkwEDD1dyTi3n6_9MkoZo2K9P4ApWvEnWNRlt_UV0OrA-JhUTtwvG9WQ9TXMYYobT4nkAys3JwcIIdLnlrRFpvDkSdzZNsTBRuUC3qfzE13BQVJXH7bCWgl1JXysZzw62GH_rIS4niPwb2QNQwgVOukWi8S8Dfd8VlcdbiaavdWn3GTPPYEnAl3JkKJok2rMXX3tNDChU8YG5WI-HOJuqnKBQSP_kfnmT5cUqmtRcvDkKoVvgvlUtToS-9Y6c0joTxcFcg5a6p5jnN-EHd_1kgjtm5_gu3iN6FALZT5Mt1KW083V94g-jnSrYjExRSPMr3g_JrZvaNI1RV4N98UqRnQgdbL_Ah0GDEpWO_gSTcKAtdOGbsoDyc7sp2JMNyF1uA34zW0kxu59go4CMOoJ3SagaaeM_yyV-FofdhoL7w5se6t5XyxlFxK0XwR07nT1khKY_BP3SYGzgA8sqX0rkxVZ-GjmqCz2Yji61Z7xjVA7PYyt8ehT4TDv0QNRNcZ9CYL5eKcLQFYS2qHdpeDP5aneZKT0rnrvWo1ZDfarQJ2jAPXtHr-Oe0EulVkpwQfqAhu6VRo6GxQaI6bW1DOyqH0UPJcVsP4NzEWlcMQl_JBd-CSafhaB-1CJdKpylb9bEgnCYoSWQHtUPNHofh-7inyqaL_DoV56Srtj8_iv-Sa6w_dJJ9lk32VnweTrGcWyixahuVLh2yonjDOA-pW4VsCL17NA3MbS_FIkZ6MqMFLFhuB83Ide-xSwhoNJ0SqaP8paDKY2ooeFDZaCFdIEW5mP84MYKYm1c3C60Yv3L-qPMPnXx9Ml0tnIz64fmB8_alBFYBodjtUYKofiNa4GpGr1syw-Zp2CRtpjKFPieqSwXG9klJG0xqE2Wu7jaBNwRoddyhTFFv9XVNgc3u4X34xCBcicrkwf-vWZO_iUOiA56wAQhU5r-dt-RZzFb7zB_18hKimsHk4h433gB-uM34ZNLDuWO2sui_J04xrJYCPjTmL1QKsVeLmJPUmM2oZpcPGI6QwhhFFo9BK5Mld8ijGymJHO7S0inKCXHV6GnM-HimEp8pjFFahrgJrgO_IXKAQlK3eaRN6nKiDgEU1vPvwTe-7q8KEsIeobpEvfIGIvoEtkPz6fI5w8wNJJdCVAUGhw9TmpJ3zPBV04oxP9IFQ9EUmjP58DWEhcroTJWTJtCo3lfAY6VTBYdQiHv6AXs=w200-h190-p-k-nu",
            ),
            DriveStoreModel(
                file_id="AAbDypCDjMwCF74LLqs2gC8nGcqNyGyS3VVDd9Qzulhi5e7GWBCnk3XSsayfTqe8CwYX3_YLIn58SnIx3vaTMbTQf9VWFLl8H9TsRHI3RMyGIJ-Ew_GeZVFMFqFMUOoveqom1d5JngNaX-lIbOLlY3XRKeatPS-56g-dcPLGnAZBguXIZ8uqxPl_A8I_Dxi_278e7Mux3TuDp8m9gr6URuQhb74SH2Cle7VRZ9x8QzsRUCr1-gqRGX_5cfixu7HCMzRn5r53KavX3McWz-OMstRi16mNBF23B8OVrOffnuIxblPZQNJr_86vYaqluNqa_8OgaoRZzMyIkMIPq3h5ltlW4dUqs1VZ08TVc1V5JJjBVSY7vryil-YYYa1aPLCAEO41wItGcE0gHANO6ER18D1q7EzmuX1KHZ32MPpHJHL0z7TWZfsqg2J_x45ul4KOuex_7jgk62ZGpgC3l_c7e-WDbQGlaWYZfJYXpQxpKYLN0hLIbEPRrDcu8FkBlNR7SDw3w0L1CUeUIf0ycebkaMNtH_CdqRMoZv0c_Ud37c1bJRCnF2bag15nBlRLGLk-VHN_pvfNiIUcvyAASyLDm1qGhAesB06AMj6E-83bIDHWjpO02agYRcNLl1Krrb4U27UwHGLjDJuhsd80efdnbc0QJMPdkCgwkp8yE0roM9IuiGZYs8kUN-0EUoGohhQHOGYApZyE_x24NuOSr4QotHJRD8JZ9HbivM0z7ARV1HIWB0J-f4ae76gQ9noruhl_SNYXalkbSwGhVjJfL6-VhBcFXu5H61ihxyIF5pHQXB07uGKXe8TzA4vOROO4NpPgyHkK8JyKz6zpoRanoFvcf-Fi0ayfRnYcQjfoqgMWxwHDcAy3ugFC_23YEKH6YtxZhZ_EJztwqx1Lhn2TpM6atgEFmdhUFGhFPstiw8wForiuyU9wjfDb-7CgERficpJmB9bTCOB9xs1WH--yHZKzPlXP3kVDc8mJmBldy9C7-56kLHh9BjydMcZZ741r6OpBb8_C5iJMejCgjHPzmtxoPTW1zDAeeUCzjyS0HJBvk4ywBFymnUanCA6fw7o6oyEVGO4OE_Vm4lgMAPhBEBUuI60vKA1COYf4LQp2n8l7jXpY4442_3-QTsGrM8Y8_xRzRAuVc_6vbzDhdo9kauDUXKt4MtTgNvde7TH5J463Y-RzXqUiWRYF9IZxMDqCK2vLi-9wHNIq5-rE8E-hqT-BGTsZAddctnzSvt64nVwmT61rXXUL0FOLwjiLbIUSZhGC_dayVhxeS1mJia9EbO9cJ0IZDJnMITG1ZUmRuFSUywK--UrcH55WzIRU4EdNhFygVdB4Mzp9CEH_Pkvp-epp-Gyd5lUzpThVH1T98WflQnrqcYg5Co_H9WVHS659YFfHHmkY1covy-S36hA8NnGR2TEIdf_eqwrB2kiOyzebShLr7895NHhqzmB72irkf7t3E5xCY81tF4GSdOj-0g6yPZVS7njo2rtiFPmGGjVI3nxs6d5yZKp8u9cVKZXf4YehTRZNOq20S0ENLVN79937IefAIA=w200-h190-p-k-nu"),
        ])
        session.commit()


def reset():
    with get_session() as session:
        data: List[BuildQueueModel] = session.query(
            BuildQueueModel).all()

        for d in data:
            d.android_building_status = None
            d.ios_building_status = None
            d.multiprocess_pid = None
            d.queue_status = QUEUE_PENDING if d.id != 2 else QUEUE_CURRENT
            d.process_pid = None
            d.metro_pid = None

            session.commit()


# reset()
# add_drive_db()
# get()
delete_all()
# add()
# create_db()
# add_status()
