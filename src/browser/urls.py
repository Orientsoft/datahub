from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^login', 'browser.auth.login'),
    url(r'^register', 'browser.auth.register'),
    url(r'^logout', 'browser.auth.logout'),

    url(r'^forgot', 'browser.auth.forgot'),
    url(r'^reset/(\w+)', 'browser.auth.reset'),
    url(r'^settings', 'browser.auth.settings'),
    url(r'^verify/(\w+)', 'browser.auth.verify'),

    url(r'^$', 'browser.views.home'),

    url(r'^console$', 'browser.views.console'),
    url(r'^console/$', 'browser.views.console'),

    url(r'^visualize$', 'browser.views.visualize'),
    url(r'^visualize/$', 'browser.views.visualize'),

    url(r'^newrepo$', 'browser.views.newrepo'),
    url(r'^newrepo/$', 'browser.views.newrepo'),

    url(r'^data-refiner$', 'browser.views.data_refiner'),
    url(r'^data-refiner/$', 'browser.views.data_refiner'),

    url(r'^refine-data$', 'browser.views.refine_data'),
    url(r'^refine-data/$', 'browser.views.refine_data'),

    url(r'^newtable/(\w+)/(\w+)$', 'browser.views.newtable'),
    url(r'^newtable/(\w+)/(\w+)/$', 'browser.views.newtable'),

    url(r'^create_table_from_file$', 'browser.views.create_table_from_file'),
    url(r'^create-table-from-file-data$', 'browser.views.create_table_from_file_data'),

    url(r'^service$', 'browser.views.service_binary'),
    url(r'^service/binary$', 'browser.views.service_binary'),
    url(r'^service/json$', 'browser.views.service_json'),

    url(r'^browse/(\w+)/(\w+)/(\w+)$', 'browser.views.table'),
    url(r'^browse/(\w+)/(\w+)/(\w+)/(\w+)$', 'browser.views.table'),
    url(r'^browse/(\w+)/(\w+)/(\w+)/(\w+)/$', 'browser.views.table'),

    url(r'^browse/(\w+)/(\w+)$', 'browser.views.repo'),
    url(r'^browse/(\w+)/(\w+)/$', 'browser.views.repo'),

    url(r'^browse/(\w+)$', 'browser.views.user'),
    url(r'^browse/(\w+)/$', 'browser.views.user'),


    ### start dbwipes urls ###

    url(r'^dbwipes/(\w+)/(\w+)$', 'browser.views.repo'),
    url(r'^dbwipes/(\w+)/(\w+)/$', 'browser.views.repo'),

    url(r'^dbwipes/(\w+)$', 'browser.views.user'),
    url(r'^dbwipes/(\w+)/$', 'browser.views.user'),

    url(r'^dbwipes/(\w+)/(\w+)/(\w+)$', 'dbwipes.views.index'),
    url(r'^dbwipes/(\w+)/(\w+)/(\w+)/$', 'dbwipes.views.index'),

    url(r'^api/databases$', 'apps.dbwipes.views.dbs'),
    url(r'^api/databases/$', 'apps.dbwipes.views.dbs'),
    url(r'^api/tables$', 'apps.dbwipes.views.tables'),
    url(r'^api/tables/$', 'apps.dbwipes.views.tables'),
    url(r'^api/schema$', 'apps.dbwipes.views.schema'),
    url(r'^api/schema/$', 'apps.dbwipes.views.schema'),
    url(r'^api/tuples/$', 'apps.dbwipes.views.api_tuples'),
    url(r'^api/query/$', 'apps.dbwipes.views.api_query'),
    url(r'^api/column_distribution/$', 'apps.dbwipes.views.column_distribution'),
    url(r'^api/column_distributions/$', 'apps.dbwipes.views.column_distributions'),
    url(r'^api/requestid/$', 'apps.dbwipes.views.requestid'),
    url(r'^api/status/$', 'apps.dbwipes.views.api_status'),
    url(r'^api/scorpion$', 'apps.dbwipes.views.scorpion'),
    url(r'^api/scorpion/$', 'apps.dbwipes.views.scorpion')

)