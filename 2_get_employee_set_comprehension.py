employee_ids = {
    row[0].value
    # Worksheet.rows now returns generator object
    for row in demo_worksheet.rows 
    if row[0].value != 'employee_num'
}