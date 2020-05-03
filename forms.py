from flask_wtf import Form
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email


class Form1Form(Form):
    # checkbox
    # checkbox_1 = BooleanField("checkbox_1",default=False)
    # checkbox_2 = BooleanField("checkbox_2", default=False)
    # checkbox_3 = BooleanField("checkbox_3", default=False)
    # checkbox_4 = BooleanField("checkbox_4", default=False)
    # checkbox_5 = BooleanField("checkbox_5",  default=False)
    # checkbox_6 = BooleanField("checkbox_6", default=False)
    # checkbox_7 = BooleanField("checkbox_7", default=False)
    # checkbox_8 = BooleanField("checkbox_8", default=False)
    # checkbox_9 = BooleanField("checkbox_9",  default=False)
    # checkbox_10 = BooleanField("checkbox_10", default=False)
    # checkbox_11 = BooleanField("checkbox_11", default=False)
    # checkbox_12 = BooleanField("checkbox_12", default=False)
    # checkbox_13 = BooleanField("checkbox_13",  default=False)
    # checkbox_14 = BooleanField("checkbox_14",  default=False)
    # checkbox_15 = BooleanField("checkbox_15", default=False)
    # checkbox_16 = BooleanField("checkbox_16", default=False)
    # actual
    actual_1 = StringField("actual_1")
    actual_2 = StringField("actual_2")
    actual_3 = StringField("actual_3")
    actual_4 = StringField("actual_4")
    actual_5 = StringField("actual_5")
    actual_6 = StringField("actual_6")
    actual_7 = StringField("actual_7")
    actual_8 = StringField("actual_8")
    actual_total = StringField("actual_total")

    # top 3 reasons
    #  t3r_1 = StringField('top3r_1')
    #  t3r_2 = StringField('top3r_2')
    #  t3r_3 = StringField('top3r_3')
    t3r_4 = StringField("top3r_4")
    t3r_5 = StringField("top3r_5")
    t3r_6 = StringField("top3r_6")
    t3r_7 = StringField("top3r_7")
    t3r_8 = StringField("top3r_8")
    t3r_total = StringField("top3r_total")

    # unloaded
    unloaded_1 = StringField("unloaded_1")
    unloaded_2 = StringField("unloaded_2")
    unloaded_3 = StringField("unloaded_3")
    unloaded_4 = StringField("unloaded_4")
    unloaded_5 = StringField("unloaded_5")
    unloaded_6 = StringField("unloaded_6")
    unloaded_7 = StringField("unloaded_7")
    unloaded_8 = StringField("unloaded_8")
    unloaded_total = StringField("unloaded_total")

    # ok
    ok_1 = StringField("ok_1")
    ok_2 = StringField("ok_2")
    ok_3 = StringField("ok_3")
    ok_4 = StringField("ok_4")
    ok_5 = StringField("ok_5")
    ok_6 = StringField("ok_6")
    ok_7 = StringField("ok_7")
    ok_8 = StringField("ok_8")
    ok_total = StringField("ok_total")

    # rejected
    rejected_1 = StringField("rejected_1")
    rejected_2 = StringField("rejected_2")
    rejected_3 = StringField("rejected_3")
    rejected_4 = StringField("rejected_4")
    rejected_5 = StringField("rejected_5")
    rejected_6 = StringField("rejected_6")
    rejected_7 = StringField("rejected_7")
    rejected_8 = StringField("rejected_8")
    rejected_total = StringField("rejected_total")

    # RD
    rd_1 = StringField("rd_1")
    rd_2 = StringField("rd_2")
    rd_3 = StringField("rd_3")
    rd_4 = StringField("rd_4")
    rd_5 = StringField("rd_5")
    rd_6 = StringField("rd_6")
    rd_7 = StringField("rd_7")
    rd_8 = StringField("rd_8")
    rd_total = StringField("rd_total")

    # dust
    dust_1 = StringField("dust_1")
    dust_2 = StringField("dust_2")
    dust_3 = StringField("dust_3")
    dust_4 = StringField("dust_4")
    dust_5 = StringField("dust_5")
    dust_6 = StringField("dust_6")
    dust_7 = StringField("dust_7")
    dust_8 = StringField("dust_8")
    dust_total = StringField("dust_total")

    # RD
    rd_1 = StringField("rd_1")
    rd_2 = StringField("rd_2")
    rd_3 = StringField("rd_3")
    rd_4 = StringField("rd_4")
    rd_5 = StringField("rd_5")
    rd_6 = StringField("rd_6")
    rd_7 = StringField("rd_7")
    rd_8 = StringField("rd_8")
    rd_total = StringField("rd_total")

    # UC
    uc_1 = StringField("uc_1")
    uc_2 = StringField("uc_2")
    uc_3 = StringField("uc_3")
    uc_4 = StringField("uc_4")
    uc_5 = StringField("uc_5")
    uc_6 = StringField("uc_6")
    uc_7 = StringField("uc_7")
    uc_8 = StringField("uc_8")
    uc_total = StringField("uc_total")

    # DSPRAY
    dspray_1 = StringField("dspray_1")
    dspray_2 = StringField("dspray_2")
    dspray_3 = StringField("dspray_3")
    dspray_4 = StringField("dspray_4")
    dspray_5 = StringField("dspray_5")
    dspray_6 = StringField("dspray_6")
    dspray_7 = StringField("dspray_7")
    dspray_8 = StringField("dspray_8")
    dspray_total = StringField("dspray_total")

    # SPITT
    spitt_1 = StringField("spitt_1")
    spitt_2 = StringField("spitt_2")
    spitt_3 = StringField("spitt_3")
    spitt_4 = StringField("spitt_4")
    spitt_5 = StringField("spitt_5")
    spitt_6 = StringField("spitt_6")
    spitt_7 = StringField("spitt_7")
    spitt_8 = StringField("spitt_8")
    spitt_total = StringField("spitt_total")

    # OThers
    others_1 = StringField("others_1")
    others_2 = StringField("others_2")
    others_3 = StringField("others_3")
    others_4 = StringField("others_4")
    others_5 = StringField("others_5")
    others_6 = StringField("others_6")
    others_7 = StringField("others_7")
    others_8 = StringField("others_8")
    others_total = StringField("others_total")

    reg = StringField("reg")
    cl = StringField("cl")
    plan = StringField("plan")
    faid = StringField("faid")
    nmiss = StringField("nmiss")

    breakdowndetails = StringField("breakdowndetails")
    shortcommunication = StringField("shortagecommunication")
    feedback = StringField("feedback")
    teamleadersign = StringField("teamleadersign")
    groupleadersign = StringField("groupleadersign")

    # standupmeetings
    standup_p = StringField("standup_p")
    standup_q = StringField("standup_q")
    standup_c = StringField("standup_c")
    standup_d = StringField("standup_d")
    standup_m = StringField("standup_m")
    standup_s = StringField("standup_s")

    # Total 'To Do' list check Plan
    to_do_list_check_plan = StringField("to_do_list_check_plan")
    actually_Done = StringField("actually_Done")


class Form2Form(Form):

    # checkbox
    # checkbox_1 = BooleanField("checkbox_1",default=False)
    # checkbox_2 = BooleanField("checkbox_2", default=False)
    # checkbox_3 = BooleanField("checkbox_3", default=False)
    # checkbox_4 = BooleanField("checkbox_4", default=False)
    # checkbox_5 = BooleanField("checkbox_5",  default=False)
    # checkbox_6 = BooleanField("checkbox_6", default=False)
    # checkbox_7 = BooleanField("checkbox_7", default=False)
    # checkbox_8 = BooleanField("checkbox_8", default=False)
    # checkbox_9 = BooleanField("checkbox_9",  default=False)
    # checkbox_10 = BooleanField("checkbox_10", default=False)

    # first hour output plan
    firstHourOutput_plan_1 = StringField("firstHourOutput_plan_1")
    firstHourOutput_plan_2 = StringField("firstHourOutput_plan_2")
    firstHourOutput_plan_3 = StringField("firstHourOutput_plan_3")

    # first hour output actual
    firstHourOutput_actual_1 = StringField("firstHourOutput_actual_1")
    firstHourOutput_actual_2 = StringField("firstHourOutput_actual_2")
    firstHourOutput_actual_3 = StringField("firstHourOutput_actual_3")

    # first hour output top 3 reasons
    firstHourOutput_top3reasons_1 = StringField("firstHourOutput_top3reasons_1")
    firstHourOutput_top3reasons_2 = StringField("firstHourOutput_top3reasons_2")

    # first hour output action
    firstHourOutput_action_1 = StringField("firstHourOutput_action_1")
    firstHourOutput_action_2 = StringField("firstHourOutput_action_2")

    # line stopper plan
    linestopper_plan_1 = StringField("linestopper_plan_1")
    linestopper_plan_2 = StringField("linestopper_plan_2")
    linestopper_plan_3 = StringField("linestopper_plan_3")
    linestopper_plan_4 = StringField("linestopper_plan_4")
    linestopper_plan_5 = StringField("linestopper_plan_5")
    linestopper_plan_6 = StringField("linestopper_plan_6")

    # line stopper actual
    linestopper_actual_1 = StringField("linestopper_actual_1")
    linestopper_actual_2 = StringField("linestopper_actual_2")
    linestopper_actual_3 = StringField("linestopper_actual_3")
    linestopper_actual_4 = StringField("linestopper_actual_4")
    linestopper_actual_5 = StringField("linestopper_actual_5")
    linestopper_actual_6 = StringField("linestopper_actual_6")

    # line stopper top 3 reasons
    linestopper_top3reasons_1 = StringField("linestopper_top3reasons_1")
    linestopper_top3reasons_2 = StringField("linestopper_top3reasons_2")
    linestopper_top3reasons_3 = StringField("linestopper_top3reasons_3")
    linestopper_top3reasons_4 = StringField("linestopper_top3reasons_4")
    linestopper_top3reasons_5 = StringField("linestopper_top3reasons_5")
    linestopper_top3reasons_6 = StringField("linestopper_top3reasons_6")

    # line stopper actual
    linestopper_action_1 = StringField("linestopper_action_1")
    linestopper_action_2 = StringField("linestopper_action_2")
    linestopper_action_3 = StringField("linestopper_action_3")
    linestopper_action_4 = StringField("linestopper_action_4")
    linestopper_action_5 = StringField("linestopper_action_5")
    linestopper_action_6 = StringField("linestopper_action_6")

    # team leader adherence name and p/a
    teamleader_name_1 = StringField("teamleader_name_1")
    teamleader_name_2 = StringField("teamleader_name_2")
    teamleader_name_3 = StringField("teamleader_name_3")
    teamleader_pa_1 = StringField("teamleader_p/a_1")
    teamleader_pa_2 = StringField("teamleader_p/a_2")
    teamleader_pa_3 = StringField("teamleader_p/a_3")

    # CONVEYOR UTILISATION plan
    conveyor_plan_1 = StringField("conveyor_plan_1")
    conveyor_plan_2 = StringField("conveyor_plan_2")
    conveyor_plan_3 = StringField("conveyor_plan_3")
    conveyor_plan_4 = StringField("conveyor_plan_4")
    conveyor_plan_5 = StringField("conveyor_plan_5")

    # CONVEYOR UTILISATION actual
    conveyor_actual_1 = StringField("conveyor_actual_1")
    conveyor_actual_2 = StringField("conveyor_actual_2")
    conveyor_actual_3 = StringField("conveyor_actual_3")
    conveyor_actual_4 = StringField("conveyor_actual_4")
    conveyor_actual_5 = StringField("conveyor_actual_5")

    # CONVEYOR UTILISATION top 3 reasons
    conveyor_top3reasons_1 = StringField("conveyor_top3reasonsl_1")
    conveyor_top3reasons_2 = StringField("conveyor_top3reasons_2")
    conveyor_top3reasons_3 = StringField("conveyor_top3reasons_3")

    # CONVEYOR UTILISATION action
    conveyor_action_1 = StringField("conveyor_action_1")
    conveyor_action_2 = StringField("conveyor_action_2")
    conveyor_action_3 = StringField("conveyor_action_3")

    # Absentism
    absent1 = StringField("absent1")
    absent2 = StringField("absent2")
    absent3 = StringField("absent3")

    # safety incident
    safe1 = StringField("safe1")
    safe2 = StringField("safe2")
    safe3 = StringField("safe3")

    # opening stock details
    stock_con300_1 = StringField("stock_con300_1")
    stock_con400_1 = StringField("stock_con400_1")
    stock_con600_1 = StringField("stock_con600_1")
    stock_con300_2 = StringField("stock_con300_2")
    stock_con400_2 = StringField("stock_con400_2")
    stock_con600_3 = StringField("stock_con600_2")
    stock_con300_3 = StringField("stock_con300_3")
    stock_con400_3 = StringField("stock_con400_3")
    stock_con600_3 = StringField("stock_con600_3")

    # leader sign
    groupleadersign = StringField("groupleadersign")
    unitmanagersign = StringField("unitmanagersignsign")

    # rework plan
    rework_plan_1 = StringField("rework_plan_1")
    rework_plan_2 = StringField("rework_plan_2")
    rework_plan_3 = StringField("rework_plan_3")
    rework_plan_4 = StringField("rework_plan_4")
    rework_plan_5 = StringField("rework_plan_5")

    # rework actual
    rework_actual_1 = StringField("rework_actual_1")
    rework_actual_2 = StringField("rework_actual_2")
    rework_actual_3 = StringField("rework_actual_3")
    rework_actual_4 = StringField("rework_actual_4")
    rework_actual_5 = StringField("rework_actual_5")

    # rework top3reasons
    rework_top3reasons_1 = StringField("rework_top3reasons_1")
    rework_top3reasons_2 = StringField("rework_top3reasons_2")
    rework_top3reasons_3 = StringField("rework_top3reasons_3")

    # rework actual
    rework_action_1 = StringField("rework_action_1")
    rework_action_2 = StringField("rework_action_2")
    rework_action_3 = StringField("rework_action_3")

    # actually done
    actuallydone_status = StringField("actuallydone_status")

    # feedback
    breakdown = StringField("breakdown")

    # breakdown
    feedback = StringField("feedback")

    # spare quantity
    sparequantity_plan = StringField("sparequantity_plan")
    sparequantity_actual = StringField("sparequantity_actual")

    # REWORK PARTS STATUS plan
    reworkpart_plan_1 = StringField("reworkpart_plan_1")

    # REWORK PARTS STATUS sanded
    reworkpart_sanded_1 = StringField("reworkpart_sanded_1")
    reworkpart_sanded_2a = StringField("reworkpart_sanded_2a")
    reworkpart_sanded_2b = StringField("reworkpart_sanded_2b")
    reworkpart_sanded_3a = StringField("reworkpart_sanded_3a")
    reworkpart_sanded_3b = StringField("reworkpart_sanded_3b")
    reworkpart_sanded_4a = StringField("reworkpart_sanded_4a")
    reworkpart_sanded_4b = StringField("reworkpart_sanded_4b")

    # REWORK PARTS STATUS scrap
    reworkpart_scrap_1 = StringField("reworkpart_scrap_1")
    reworkpart_scrap_2a = StringField("reworkpart_scrap_2a")
    reworkpart_scrap_2b = StringField("reworkpart_scrap_2b")
    reworkpart_scrap_3a = StringField("reworkpart_scrap_3a")
    reworkpart_scrap_3b = StringField("reworkpart_scrap_3b")
    reworkpart_scrap_4a = StringField("reworkpart_scrap_4a")
    reworkpart_scrap_4b = StringField("reworkpart_scrap_4b")
    reworkpart_scrap_2c = StringField("reworkpart_scrap_2c")

    # customer complaints plan
    customercomplaints_plan_1 = StringField("customercomplaints_plan_1")
    customercomplaints_plan_2 = StringField("customercomplaints_plan_2")
    customercomplaints_plan_3 = StringField("customercomplaints_plan_3")

    # customer complaints actual
    customercomplaints_actual_1 = StringField("customercomplaints_actual_1")
    customercomplaints_actual_2 = StringField("customercomplaints_actual_2")
    customercomplaints_actual_3 = StringField("customercomplaints_actual_3")

    # customer complaints top 3 reasons
    customercomplaints_top3reasons_1a = StringField("customercomplaints_top3reasons_1a")
    customercomplaints_top3reasons_1b = StringField("customercomplaints_top3reasons_1b")
    customercomplaints_top3reasons_1c = StringField("customercomplaints_top3reasons_1c")
    customercomplaints_top3reasons_2a = StringField("customercomplaints_top3reasons_2a")
    customercomplaints_top3reasons_2b = StringField("customercomplaints_top3reasons_2b")
    customercomplaints_top3reasons_2c = StringField("customercomplaints_top3reasons_2c")
    customercomplaints_top3reasons_3a = StringField("customercomplaints_top3reasons_3a")
    customercomplaints_top3reasons_3b = StringField("customercomplaints_top3reasons_3b")
    customercomplaints_top3reasons_3c = StringField("customercomplaints_top3reasons_3c")
    customercomplaints_top3reasons_4a = StringField("customercomplaints_top3reasons_4a")
    customercomplaints_top3reasons_4b = StringField("customercomplaints_top3reasons_4b")
    customercomplaints_top3reasons_4c = StringField("customercomplaints_top3reasons_4c")
    customercomplaints_top3reasons_5a = StringField("customercomplaints_top3reasons_5a")
    customercomplaints_top3reasons_5b = StringField("customercomplaints_top3reasons_5b")
    customercomplaints_top3reasons_5c = StringField("customercomplaints_top3reasons_5c")
    customercomplaints_top3reasons_6a = StringField("customercomplaints_top3reasons_6a")
    customercomplaints_top3reasons_6b = StringField("customercomplaints_top3reasons_6b")
    customercomplaints_top3reasons_6c = StringField("customercomplaints_top3reasons_6c")
    customercomplaints_top3reasons_7a = StringField("customercomplaints_top3reasons_7a")
    customercomplaints_top3reasons_7b = StringField("customercomplaints_top3reasons_7b")
    customercomplaints_top3reasons_7c = StringField("customercomplaints_top3reasons_7c")

    # customer complaints action
    customercomplaints_action_1a = StringField("customercomplaints_action_1a")
    customercomplaints_action_1b = StringField("customercomplaints_action_1b")
    customercomplaints_action_1c = StringField("customercomplaints_action_1c")
    customercomplaints_action_2a = StringField("customercomplaints_action_2a")
    customercomplaints_action_2b = StringField("customercomplaints_action_2b")
    customercomplaints_action_2c = StringField("customercomplaints_action_2c")
    customercomplaints_action_3a = StringField("customercomplaints_action_3a")
    customercomplaints_action_3b = StringField("customercomplaints_action_3b")
    customercomplaints_action_3c = StringField("customercomplaints_action_3c")
    customercomplaints_action_4a = StringField("customercomplaints_action_4a")
    customercomplaints_action_4b = StringField("customercomplaints_action_4b")
    customercomplaints_action_4c = StringField("customercomplaints_action_4c")
    customercomplaints_action_5a = StringField("customercomplaints_action_5a")
    customercomplaints_action_5b = StringField("customercomplaints_action_5b")
    customercomplaints_action_5c = StringField("customercomplaints_action_5c")
    customercomplaints_action_6a = StringField("customercomplaints_action_6a")
    customercomplaints_action_6b = StringField("customercomplaints_action_6b")
    customercomplaints_action_6c = StringField("customercomplaints_action_6c")
    customercomplaints_action_7a = StringField("customercomplaints_action_7a")
    customercomplaints_action_7b = StringField("customercomplaints_action_7b")
    customercomplaints_action_7c = StringField("customercomplaints_action_7c")


class Form3Form(Form):
    # checkbox
    # checkbox_1 = BooleanField("checkbox_1",default=False)
    # checkbox_2 = BooleanField("checkbox_2", default=False)
    # checkbox_3 = BooleanField("checkbox_3", default=False)
    # checkbox_4 = BooleanField("checkbox_4", default=False)
    # checkbox_5 = BooleanField("checkbox_5",  default=False)
    # checkbox_6 = BooleanField("checkbox_6", default=False)
    # checkbox_7 = BooleanField("checkbox_7", default=False)
    # checkbox_8 = BooleanField("checkbox_8", default=False)
    # checkbox_9 = BooleanField("checkbox_9",  default=False)
    # checkbox_10 = BooleanField("checkbox_10", default=False)
    # checkbox_11 = BooleanField("checkbox_11", default=False)
    # checkbox_12 = BooleanField("checkbox_12", default=False)
    # checkbox_13 = BooleanField("checkbox_13",  default=False)
    # checkbox_14 = BooleanField("checkbox_14",  default=False)
    # checkbox_15 = BooleanField("checkbox_15", default=False)
    # checkbox_16 = BooleanField("checkbox_16", default=False)
    # actual
    actual_1 = StringField("actual_1")
    actual_2 = StringField("actual_2")
    actual_3 = StringField("actual_3")
    actual_4 = StringField("actual_4")
    actual_5 = StringField("actual_5")
    actual_6 = StringField("actual_6")
    actual_7 = StringField("actual_7")
    actual_8 = StringField("actual_8")
    actual_total = StringField("actual_totala")

    # customercomplaint_1a
    customercomplaint_1a = StringField("customercomplaint_1a")
    customercomplaint_2a = StringField("customercomplaint_2a")
    customercomplaint_3a = StringField("customercomplaint_3a")
    customercomplaint_4a = StringField("customercomplaint_4a")
    customercomplaint_5a = StringField("customercomplaint_5a")
    customercomplaint_6a = StringField("customercomplaint_6a")
    customercomplaint_7a = StringField("customercomplaint_7a")
    customercomplaint_8a = StringField("customercomplaint_8a")
    customercomplaint_totala = StringField("customercomplaint_totala")

    # sd
    sd_1 = StringField("sd_1")
    sd_2 = StringField("sd_2")
    sd_3 = StringField("sd_3")
    sd_4 = StringField("sd_4")
    sd_5 = StringField("sd_5")
    sd_6 = StringField("sd_6")
    sd_7 = StringField("sd_7")
    sd_8 = StringField("sd_8")
    sd_total = StringField("sd_total")

    # RD
    rd_1 = StringField("rd_1")
    rd_2 = StringField("rd_2")
    rd_3 = StringField("rd_3")
    rd_4 = StringField("rd_4")
    rd_5 = StringField("rd_5")
    rd_6 = StringField("rd_6")
    rd_7 = StringField("rd_7")
    rd_8 = StringField("rd_8")
    rd_total = StringField("rd_total")

    # customercomplaint_1b
    customercomplaint_1b = StringField("customercomplaint_1b")
    customercomplaint_2b = StringField("customercomplaint_2b")
    customercomplaint_3b = StringField("customercomplaint_3b")
    customercomplaint_4b = StringField("customercomplaint_4b")
    customercomplaint_5b = StringField("customercomplaint_5b")
    customercomplaint_6b = StringField("customercomplaint_6b")
    customercomplaint_7b = StringField("customercomplaint_7b")
    customercomplaint_8b = StringField("customercomplaint_8b")
    customercomplaint_totalb = StringField("customercomplaint_totalb")

    # top 3 reasons
    t3r_1 = StringField("top3r_1")
    t3r_2 = StringField("top3r_2")
    t3r_3 = StringField("top3r_3")
    t3r_4 = StringField("top3r_4")
    t3r_5 = StringField("top3r_5")
    t3r_6 = StringField("top3r_6")
    t3r_7 = StringField("top3r_7")
    t3r_8 = StringField("top3r_8")
    t3r_total = StringField("top3r_total")

    # dust
    dust_1 = StringField("dust_1")
    dust_2 = StringField("dust_2")
    dust_3 = StringField("dust_3")
    dust_4 = StringField("dust_4")
    dust_5 = StringField("dust_5")
    dust_6 = StringField("dust_6")
    dust_7 = StringField("dust_7")
    dust_8 = StringField("dust_8")
    dust_total = StringField("dust_total")

    # UC
    uc_1 = StringField("uc_1")
    uc_2 = StringField("uc_2")
    uc_3 = StringField("uc_3")
    uc_4 = StringField("uc_4")
    uc_5 = StringField("uc_5")
    uc_6 = StringField("uc_6")
    uc_7 = StringField("uc_7")
    uc_8 = StringField("uc_8")
    uc_total = StringField("uc_total")

    # DS
    ds_1 = StringField("ds_1")
    ds_2 = StringField("ds_2")
    ds_3 = StringField("ds_3")
    ds_4 = StringField("ds_4")
    ds_5 = StringField("ds_5")
    ds_6 = StringField("ds_6")
    ds_7 = StringField("ds_7")
    ds_8 = StringField("ds_8")
    ds_total = StringField("ds_total")

    # SPITT
    spitt_1 = StringField("spitt_1")
    spitt_2 = StringField("spitt_2")
    spitt_3 = StringField("spitt_3")
    spitt_4 = StringField("spitt_4")
    spitt_5 = StringField("spitt_5")
    spitt_6 = StringField("spitt_6")
    spitt_7 = StringField("spitt_7")
    spitt_8 = StringField("spitt_8")
    spitt_total = StringField("spitt_total")
    # OThers
    others_1 = StringField("others_1")
    others_2 = StringField("others_2")
    others_3 = StringField("others_3")
    others_4 = StringField("others_4")
    others_5 = StringField("others_5")
    others_6 = StringField("others_6")
    others_7 = StringField("others_7")
    others_8 = StringField("others_8")
    others_total = StringField("others_total")

    reg = StringField("reg")
    cl = StringField("cl")
    plan = StringField("plan")
    faid = StringField("faid")
    nmiss = StringField("nmiss")

    breakdowndetails = StringField("breakdowndetails")
    shortcommunication = StringField("shortagecommunication")
    feedback = StringField("feedback")
    teamleadersign = StringField("teamleadersign")
    groupleadersign = StringField("groupleadersign")

    # standupmeetings
    standup_p = StringField("standup_p")
    standup_q = StringField("standup_q")
    standup_c = StringField("standup_c")
    standup_d = StringField("standup_d")
    standup_m = StringField("standup_m")
    standup_s = StringField("standup_s")

    # Total 'To Do' list check Plan
    to_do_list_check_plan = StringField("to_do_list_check_plan")
    actually_Done = StringField("actually_Done")
