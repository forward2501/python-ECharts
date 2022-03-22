import web,xlrd

urls = (
    '/', 'index',
    #'/(.*)', 'index'
    '/chart','chart'
)
app = web.application(urls, globals())
render = web.template.render("templates/")

class index:
    #def GET(self):
        #i=web.input(name=None)
       # return render.index(i.name)

    # def GET(self, name):
    # return render.index(name)

    def GET(self):
        return render.index()

class chart:
    def GET(self):
        workbook = xlrd.open_workbook("homework.xls")
        worksheet1 = workbook.sheet_by_index(0)
        worksheet2 = workbook.sheet_by_index(1)
        worksheet3 = workbook.sheet_by_index(2)
        study_data = {
            "category": worksheet1.row_values(0),
            "data":worksheet1.row_values(1)
        }
        language_data = []
        language_title = worksheet2.row_values(3)
        language_value = worksheet2.row_values(4)
        for i in range(len(language_title)):
            language_data.append({"name":language_title[i],"value":language_value[i]})

        language_stat_data = []
        language_stat_title = worksheet2.row_values(0,0,3)
        language_stat_value = worksheet2.row_values(1,0,3)
        for i in range(len(language_stat_title)):
            language_stat_data.append({"name": language_stat_title[i], "value":  language_stat_value[i]})

        language_all_title = language_stat_title+language_title

        visit_data=[]
        visit_title = worksheet3.row_values(0)
        visit_value = worksheet3.row_values(1)
        for i in range(len(visit_title)):
            visit_data.append({"name": visit_title[i], "value":  visit_value[i]})

        return render.chart(study_data=study_data,language_data=language_data, language_title= language_title,language_stat_data=language_stat_data,language_stat_title=language_stat_title,language_all_title=language_all_title, visit_data= visit_data,visit_title=visit_title)

if __name__ == "__main__":
    app.run()