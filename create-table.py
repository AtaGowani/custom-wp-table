import csv

headers = []
data = []

with open('data.csv', newline='') as csvfile:
  header = True
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')
  for row in reader:
    print(row)
    if header:
      headers = row
      header = False
      continue
    data.append(row)

styles = """
<style>
  /* The Modal (background) */
  .modal {
    display: none;
    /* Hidden by default */
    position: fixed;
    /* Stay in place */
    z-index: 1;
    /* Sit on top */
    padding-top: 100px;
    /* Location of the box */
    left: 0;
    top: 0;
    width: 100%;
    /* Full width */
    height: 100%;
    /* Full height */
    overflow: auto;
    /* Enable scroll if needed */
    background-color: rgb(0, 0, 0);
    /* Fallback color */
    background-color: rgba(0, 0, 0, 0.4);
    /* Black w/ opacity */
  }

  /* Modal Content */
  .modal-content {
    background-color: #fefefe;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
  }

  /* The Close Button */
  .close {
    color: #aaaaaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }

  .close:hover,
  .close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
  }

  table {
    font-family: sans-serif;
    width: 100%;
    table-layout: fixed;
  }

  .tbl-header {
    background-color: #0D47A18f;
  }

  .tbl-content {
    height: 300px;
    overflow-x: auto;
    margin-top: 0px;
    border: 1px solid #0D47A14d;
  }

  tbody tr:nth-child(even) {
    background-color: #0d48a126;
  }

  tbody tr:hover {
    background-color: #0d48a154;
  }

  th {
    padding: 20px 15px;
    text-align: left;
    font-weight: 500;
    font-size: 12px;
    color: #fff;
    text-transform: uppercase;
  }

  td {
    padding: 15px;
    text-align: left;
    vertical-align: middle;
    font-weight: 300;
    font-size: 12px;
    color: #000;
    border-bottom: solid 1px #0D47A11a;
  }

  /* for custom scrollbar for webkit browser*/

  ::-webkit-scrollbar {
    width: 6px;
  }

  ::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  }

  ::-webkit-scrollbar-thumb {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  }
</style>
"""

def createTableHeader(headers):
  pre_header_html = """
  <div class="tbl-header">
  <table cellpadding="0" cellspacing="0" border="0">
    <thead>
      <tr>
  """
  header_html = ""
  post_header_html = """
        </tr>
      </thead>
    </table>
  </div>
  """

  for header in headers:
    header_html += "<th>" + header + "</th>"

  return pre_header_html + header_html + post_header_html

def createTableData(data):
  row_number = 0
  pre_data_html = """
  <div id="tbl-content" class="tbl-content">
  <table cellpadding="0" cellspacing="0" border="0">
    <tbody>
  """
  data_html = ""
  post_data_html = """
      </tbody>
    </table>
  </div>
  """

  for row in data:
    pre_table_row = """
    <div class='table-data'>
        <tr id='cp-""" + str(row_number) + "'>"

    table_row = ""
    post_table_row = """
        </tr>
        <!-- Modal with data -->
        <div id="cp-""" + str(row_number) + """-data" class="modal">

          <!-- Modal content -->
          <div class="modal-content">
            <span class="close">&times;</span>
            <p>This modal will have info about the company.</p>
          </div>

        </div>
      </div>
    """
    for value in row:
      table_row += "<td>" + value + "</td>"
    data_html += pre_table_row + table_row + post_table_row
    row_number+=1

  return pre_data_html + data_html + post_data_html

table_header = createTableHeader(headers)
table_data = createTableData(data)

script = """
<script>
  var table_content = document.getElementById("tbl-content");
  var table_rows = table_content.getElementsByTagName("tr");
  var close_buttons = document.getElementsByClassName("close");

  for (var i = 0; i < close_buttons.length; i++) {
    close_buttons[i].addEventListener("click",  (e) => {
      parent_modal = e.currentTarget.parentNode.parentNode;
      parent_modal.style.display = "none";
    })
  }

  for (var i = 0; i < table_rows.length; i++) {
    var tbl_row = table_rows[i];
    var row_id = tbl_row.id;
    if (row_id) {
      tbl_row.addEventListener("click", (e) => {
        var modal_el = document.getElementById(e.currentTarget.id + "-data");
        modal_el.style.display = "block";
      })
    }
  }
</script>
"""

final_html = styles + table_header + table_data + script

f = open("table.html", "w")
f.write(final_html)
f.close()