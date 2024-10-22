from django.db import models


class PersonalMember(models.Model):
    member_number = models.CharField(
        primary_key=True, max_length=8, db_column="会員番号"
    )
    membership_type = models.CharField(
        max_length=1, blank=True, null=True, db_column="入会区分"
    )
    withdrawal_type = models.CharField(
        max_length=1, blank=True, null=True, db_column="退会区分"
    )
    affiliation = models.CharField(
        max_length=1, blank=True, null=True, db_column="所属"
    )
    membership_category_1 = models.CharField(
        max_length=2, blank=True, null=True, db_column="会員種別１"
    )
    membership_category_2 = models.CharField(
        max_length=2, blank=True, null=True, db_column="会員種別２"
    )
    appraiser_number = models.CharField(
        max_length=8, blank=True, null=True, db_column="鑑定士番号"
    )
    appraiser_registration_date = models.DateTimeField(
        blank=True, null=True, db_column="鑑定士登録年月日"
    )
    assistant_appraiser_number = models.CharField(
        max_length=8, blank=True, null=True, db_column="鑑定士補番号"
    )
    assistant_appraiser_registration_date = models.DateTimeField(
        blank=True, null=True, db_column="鑑定士補登録年月日"
    )
    application_date = models.DateTimeField(blank=True, null=True, db_column="申込日付")
    name_kana = models.CharField(
        max_length=20, blank=True, null=True, db_column="氏名カナ"
    )
    name_kanji = models.CharField(
        max_length=20, blank=True, null=True, db_column="氏名漢字"
    )
    birth_date = models.DateTimeField(blank=True, null=True, db_column="生年月日")
    gender = models.CharField(max_length=1, blank=True, null=True, db_column="性別")
    home_postal_code = models.CharField(
        max_length=7, blank=True, null=True, db_column="自宅郵便番号"
    )
    home_address_kana = models.CharField(
        max_length=80, blank=True, null=True, db_column="自宅住所カナ"
    )
    home_address1_kanji = models.CharField(
        max_length=40, blank=True, null=True, db_column="自宅住所１漢字"
    )
    home_address2_kanji = models.CharField(
        max_length=40, blank=True, null=True, db_column="自宅住所２漢字"
    )
    home_phone_number = models.CharField(
        max_length=14, blank=True, null=True, db_column="自宅電話番号"
    )
    home_fax_number = models.CharField(
        max_length=14, blank=True, null=True, db_column="自宅ＦＡＸ番号"
    )
    home_location_code = models.CharField(
        max_length=3, blank=True, null=True, db_column="自宅所在地コード"
    )
    home_effective_start_date = models.DateTimeField(
        blank=True, null=True, db_column="自宅有効開始日"
    )
    home_address_display_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="自宅住所帳票表示許可フラグ"
    )
    workplace_use_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="勤務先業者所在地使用フラグ"
    )
    workplace_member_number = models.CharField(
        max_length=8, blank=True, null=True, db_column="勤務先会員番号"
    )
    workplace_name_kana = models.CharField(
        max_length=40, blank=True, null=True, db_column="勤務先業者名称カナ"
    )
    workplace_name_kanji = models.CharField(
        max_length=60, blank=True, null=True, db_column="勤務先業者名称漢字"
    )
    workplace_department_name = models.CharField(
        max_length=20, blank=True, null=True, db_column="勤務先部署名称"
    )
    workplace_postal_code = models.CharField(
        max_length=7, blank=True, null=True, db_column="勤務先郵便番号"
    )
    workplace_address_kana = models.CharField(
        max_length=80, blank=True, null=True, db_column="勤務先住所カナ"
    )
    workplace_address1_kanji = models.CharField(
        max_length=40, blank=True, null=True, db_column="勤務先住所１漢字"
    )
    workplace_address2_kanji = models.CharField(
        max_length=40, blank=True, null=True, db_column="勤務先住所２漢字"
    )
    workplace_phone_number = models.CharField(
        max_length=14, blank=True, null=True, db_column="勤務先電話番号"
    )
    workplace_fax_number = models.CharField(
        max_length=14, blank=True, null=True, db_column="勤務先ＦＡＸ番号"
    )
    workplace_location_code = models.CharField(
        max_length=3, blank=True, null=True, db_column="勤務先所在地コード"
    )
    workplace_effective_start_date = models.DateTimeField(
        blank=True, null=True, db_column="勤務先有効開始日"
    )
    workplace_address_display_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="勤務先住所帳票表示許可フラグ"
    )
    alternate_workplace_use_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="別勤務先業者所在地使用フラグ"
    )
    alternate_workplace_member_number = models.CharField(
        max_length=8, blank=True, null=True, db_column="別勤務先会員番号"
    )
    alternate_workplace_name_kana = models.CharField(
        max_length=40, blank=True, null=True, db_column="別勤務先業者名称カナ"
    )
    alternate_workplace_name_kanji = models.CharField(
        max_length=60, blank=True, null=True, db_column="別勤務先業者名称漢字"
    )
    alternate_workplace_department_name = models.CharField(
        max_length=20, blank=True, null=True, db_column="別勤務先部署名称"
    )
    alternate_workplace_postal_code = models.CharField(
        max_length=7, blank=True, null=True, db_column="別勤務先郵便番号"
    )
    alternate_workplace_address_kana = models.CharField(
        max_length=80, blank=True, null=True, db_column="別勤務先住所カナ"
    )
    alternate_workplace_address1_kanji = models.CharField(
        max_length=40, blank=True, null=True, db_column="別勤務先住所１漢字"
    )
    alternate_workplace_address2_kanji = models.CharField(
        max_length=40, blank=True, null=True, db_column="別勤務先住所２漢字"
    )
    alternate_workplace_phone_number = models.CharField(
        max_length=14, blank=True, null=True, db_column="別勤務先電話番号"
    )
    alternate_workplace_fax_number = models.CharField(
        max_length=14, blank=True, null=True, db_column="別勤務先ＦＡＸ番号"
    )
    alternate_workplace_location_code = models.CharField(
        max_length=3, blank=True, null=True, db_column="別勤務先所在地コード"
    )
    alternate_workplace_effective_start_date = models.DateTimeField(
        blank=True, null=True, db_column="別勤務先有効開始日"
    )
    email_address = models.CharField(
        max_length=80, blank=True, null=True, db_column="電子メールアドレス"
    )
    newsletter_email_address = models.CharField(
        max_length=80, blank=True, null=True, db_column="メルマガ用メールアドレス"
    )
    newsletter_subscription_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="メルマガ配信有無"
    )
    mobile_phone_number = models.CharField(
        max_length=14, blank=True, null=True, db_column="携帯電話番号"
    )
    mobile_email_address = models.CharField(
        max_length=30, blank=True, null=True, db_column="携帯メールアドレス"
    )
    join_date = models.DateTimeField(blank=True, null=True, db_column="入会日")
    withdrawal_date = models.DateTimeField(blank=True, null=True, db_column="退会日")
    withdrawal_reason_comment = models.CharField(
        max_length=200, blank=True, null=True, db_column="退会理由コメント"
    )
    membership_fee_exemption_start_date = models.DateTimeField(
        blank=True, null=True, db_column="会費免除開始日"
    )
    membership_fee_exemption_end_date = models.DateTimeField(
        blank=True, null=True, db_column="会費免除終了日"
    )
    invoice_sending_address = models.CharField(
        max_length=2, blank=True, null=True, db_column="請求書等送付先"
    )
    invoice_sending_address_start_date = models.DateTimeField(
        blank=True, null=True, db_column="請求書等送付先有効開始日"
    )
    mail_sending_address = models.CharField(
        max_length=2, blank=True, null=True, db_column="郵便物送付先"
    )
    mail_sending_address_start_date = models.DateTimeField(
        blank=True, null=True, db_column="郵便物送付先有効開始日"
    )
    headquarters_membership_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="本部入会フラグ"
    )
    headquarters_member_number = models.CharField(
        max_length=8, blank=True, null=True, db_column="本部会員番号"
    )
    rea_network_registration_date = models.DateTimeField(
        blank=True, null=True, db_column="ＲＥＡネット登録年月日"
    )
    web_password = models.CharField(
        max_length=6, blank=True, null=True, db_column="ＷＥＢパスワード"
    )
    notes = models.CharField(max_length=200, blank=True, null=True, db_column="備考")
    member_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="会員フラグ"
    )
    user_update_date = models.DateTimeField(
        blank=True, null=True, db_column="利用者更新日"
    )
    registration_datetime = models.DateTimeField(
        blank=True, null=True, db_column="登録日時"
    )
    update_datetime = models.DateTimeField(blank=True, null=True, db_column="更新日時")
    my_number_registration_flag = models.CharField(
        max_length=1, blank=True, null=True, db_column="マイナンバー登録有無フラグ"
    )
    invoice_registration_number = models.CharField(
        max_length=13, db_column="インボイス登録番号"
    )

    class Meta:
        managed = False
        db_table = "AA001個人会員管理テーブル"
