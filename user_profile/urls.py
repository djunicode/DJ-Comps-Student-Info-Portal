from django.conf.urls import url
from django.urls import path
from . import views

app_name = "user_profile"
urlpatterns = [
    url(r"^$", views.homepage, name="homepage"),
    url(r"^register/student/$", views.register, name="register"),
    url(r"^login/student/$", views.user_login, name="user_login"),
    url(r"^register/teacher/$", views.register_teacher, name="register_teacher"),
    url(r"^login/teacher/$", views.user_login_teacher, name="user_login_teacher"),
    path(
        "activate/<uidb64>/<token>/",
        views.activate,
        name="activate",
    ),
    url(r"^logout/student/$", views.logout_student, name="logout_student"),
    url(r"^logout/teacher/$", views.logout_teacher, name="logout_teacher"),
    url(r"^login/recruiter/$", views.user_login_recruiter, name="user_login_recruiter"),
    url(r"^logout/recruiter/$", views.logout_recruiter, name="logout_recruiter"),
    url(r"^student_profile/(\d+)$", views.student_profile, name="student_profile"),
    url(r"^notifications/$", views.notifs, name="notifs"),
    url(r"^search/$", views.student_list, name="student_list"),
    url(r"^teacherdashboard/$", views.teacher_dashboard, name="teacher_dashboard"),
    url(r"^search/$", views.student_list, name="student_list"),
    url(r"^internship/(\d+)$", views.internship, name="internship"),
    url(r"^hackathon/(\d+)$", views.hackathon, name="hackathon"),
    url(r"^project/(\d+)$", views.project, name="project"),
    url(r"^beproject/(\d+)$", views.beproject, name="beproject"),
    url(r"^committee/(\d+)$", views.committee, name="committee"),
    url(r"^researchpaper/(\d+)$", views.researchpaper, name="researchpaper"),
    url(r"^extracurricular/(\d+)$", views.extracurricular, name="extracurricular"),
    url(r"^searchany/", views.searchany, name="searchany"),
    url(r"^editprofile", views.show_edit_studentprofile, name="show_edit_studentprofile"),
    url(r"^edit_basic_info/(\d+)$", views.edit_basic_info),
    url(r"^edit_competitive_exams/(\d+)$", views.edit_competitive_exams),
    url(r"^edit_academic_info/(\d+)$", views.edit_academic_info),
    url(r"^edit_skill_info/(\d+)$", views.edit_skill_info),
    url(r"^edit_hackathon_info/(\d+)$", views.edit_hackathon_info),
    url(r"^edit_project_info/(\d+)$", views.edit_project_info),
    url(r"^edit_internship_info/(\d+)$", views.edit_internship_info),
    url(r"^edit_committee_info/(\d+)$", views.edit_committee_info),
    url(r"^edit_research_paper_info/(\d+)$", views.edit_research_paper_info),
    url(r"^edit_beproject_info/(\d+)$", views.edit_beproject_info),
    url(r"^delete_project_info/(\d+)$", views.delete_project_info),
    url(r"^delete_hackathon_info/(\d+)$", views.delete_hackathon_info),
    url(r"^delete_committee_info/(\d+)$", views.delete_committee_info),
    url(r"^delete_skill_info/(\d+)$", views.delete_skill_info),
    url(r"^delete_internship_info/(\d+)$", views.delete_internship_info),
    url(r"^delete_researchpaper_info/(\d+)$", views.delete_researchpaper_info),
    url(r"^delete_extra_info/(\d+)$", views.delete_extra_info),
    url(r"^edit_extra_info/(\d+)$", views.edit_extra_info),
    url(r"^delete_admit_info/(\d+)$", views.delete_admit_info),
    url(r"^edit_admit_info/(\d+)$", views.edit_admit_info),

    url(r"^delete_placement_info/(\d+)$", views.delete_placement_info),
    url(r"^edit_placement_info/(\d+)$", views.edit_placement_info),

    url(r"^filters_adv/$", views.filters_adv, name="filters_adv"),
    path("internship_approved/<int:id>", views.internship_approved, name="iapproved"),
    path("internship_rejected/<int:id>", views.internship_rejected, name="irejected"),

    path("hackathon_approved/<int:id>", views.hackathon_approved, name="hackathon-approved"),
    path("hackathon_rejected/<int:id>", views.hackathon_rejected, name="hackathon-rejected"),

    path("project_approved/<int:id>", views.project_approved, name="project-approved"),
    path("project_rejected/<int:id>", views.project_rejected, name="project-rejected"),

    path("research_paper_approved/<int:id>", views.research_paper_approved, name="research-paper-approved"),
    path("research_paper_rejected/<int:id>", views.research_paper_rejected, name="research-paper-rejected"),

    path("be_project_approved/<int:id>", views.BE_project_approved, name="be-project-approved"),
    path("be_project_rejected/<int:id>", views.BE_project_rejected, name="be-project-rejected"),

    path("admit_approved/<int:id>", views.admit_approved, name="admit-approved"),
    path("admit_rejected/<int:id>", views.admit_rejected, name="admit-rejected"),

    path("placement_approved/<int:id>", views.placement_approved, name="placement-approved"),
    path("placement_rejected/<int:id>", views.placement_rejected, name="placement-rejected"),


    path("competitive_exam_approved/<int:id>", views.competitive_exams_approved, name="competitive-exam-approved"),
    path("competitive_exam_rejected/<int:id>", views.competitive_exams_rejected, name="competitive-exam-rejected"),

    path("committee_approved/<int:id>", views.committee_approved, name="committee-approved"),
    path("committee_rejected/<int:id>", views.committee_rejected, name="committee-rejected"),


    path("all_excel", views.download_all_excel, name="all-excel"),
    path("forgot-password/",views.ForgotPassword,name="forgot_password"),
    path("reset_password_request/", views.ResetPasswordRequest, name="reset_password_request"),
    path("password-reset-confirm/<uidb64>/<token>/", views.PasswordResetConfirm, name="password-reset-confirm"),
    path("rese_password/<int:user_id>/", views.ResetPassword, name="reset_password"),
]
