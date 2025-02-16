# Generated by Django 4.1.3 on 2024-07-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.CharField(blank=True, max_length=255, null=True)),
                ('cpu', models.CharField(blank=True, max_length=255, null=True)),
                ('memory', models.CharField(blank=True, max_length=255, null=True)),
                ('network', models.CharField(blank=True, max_length=255, null=True)),
                ('disk_detail', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sys_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial', models.CharField(blank=True, max_length=255, null=True)),
                ('exchange_rate', models.FloatField(blank=True, null=True)),
                ('target', models.CharField(blank=True, max_length=255, null=True)),
                ('abbreviation', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'conversion',
            },
        ),
        migrations.CreateModel(
            name='SysImageSetting',
            fields=[
                ('edition', models.IntegerField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=126)),
                ('temp_path', models.CharField(blank=True, max_length=126, null=True)),
                ('cjcs', models.IntegerField(blank=True, null=True)),
                ('jgsj', models.IntegerField(blank=True, null=True)),
                ('dqsj', models.IntegerField(blank=True, null=True)),
                ('sfqy', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_image_setting',
            },
        ),
        migrations.CreateModel(
            name='SysLog',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('accout', models.CharField(blank=True, max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('time', models.CharField(blank=True, max_length=32, null=True)),
                ('content', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'sys_log',
            },
        ),
        migrations.CreateModel(
            name='SysMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('caption', models.CharField(blank=True, max_length=32, null=True)),
                ('lcon', models.CharField(blank=True, max_length=32, null=True)),
                ('url', models.CharField(blank=True, max_length=128, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'sys_menu',
            },
        ),
        migrations.CreateModel(
            name='SysOrg',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('org_name', models.CharField(blank=True, max_length=32, null=True)),
                ('org_code', models.CharField(blank=True, max_length=128, null=True)),
                ('pid', models.CharField(blank=True, max_length=32, null=True)),
                ('remark', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'sys_org',
            },
        ),
        migrations.CreateModel(
            name='SysRole',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('caption', models.CharField(blank=True, max_length=32, null=True)),
                ('abbreviation', models.CharField(blank=True, max_length=32, null=True)),
                ('remark', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'sys_role',
            },
        ),
        migrations.CreateModel(
            name='SysRoleMenu',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('role_id', models.CharField(blank=True, max_length=32, null=True)),
                ('role_name', models.CharField(blank=True, max_length=32, null=True)),
                ('menu_id', models.IntegerField(blank=True, null=True)),
                ('menu_name', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'sys_role_menu',
            },
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('pwd', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('account', models.CharField(blank=True, max_length=32, null=True)),
                ('tell', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=32, null=True)),
                ('level', models.CharField(blank=True, max_length=32, null=True)),
                ('gender', models.CharField(blank=True, max_length=32, null=True)),
                ('sfcj', models.IntegerField()),
            ],
            options={
                'db_table': 'sys_user',
            },
        ),
        migrations.CreateModel(
            name='SysUserOrg',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('org_id', models.CharField(blank=True, max_length=32, null=True)),
                ('org_name', models.CharField(blank=True, max_length=64, null=True)),
                ('user_id', models.CharField(blank=True, max_length=32, null=True)),
                ('user_name', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'sys_user_org',
            },
        ),
        migrations.CreateModel(
            name='SysUserRole',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('rle_id', models.CharField(blank=True, max_length=32, null=True)),
                ('rle_name', models.CharField(blank=True, max_length=32, null=True)),
                ('user_id', models.CharField(blank=True, max_length=32, null=True)),
                ('user_name', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'sys_user_role',
            },
        ),
    ]
