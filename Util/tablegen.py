fin = open("Project Daloy.csv", "r")
fout = open("output.md", "w")
th = False
end = False
ch = False

def write(n, msg):
	global fout
	fout.write(("\t" * n) + msg + "\n")


for line in fin:
	tokens = [i.replace("\n", "") for i in line.split(",")]
	assert len(tokens) == 4

	if tokens[0] == "Grand Total":
		write(0, "# Grand Total: " + tokens[3])
		continue
	if th:
		write(1, "<tr>")
	if len(tokens[1]) == 0:
		if (len(tokens[3]) == 0):
			# Header
			th = ch = True
			end = False
			write(0, "<table>")
			write(1, "<tr>")
			write(2, "<td colspan = \"4\">" + tokens[0] + "</td>");
		else:
			# Subtotal
			write(2, "<td colspan=\"3\">" + tokens[0] + "</td>")
			write(2, "<td>" + tokens[3] + "</td>")
			end = True
	else:
		# Entry
		if ch:
			write(2, "<td><strong>" + tokens[0] + "</strong></td>")
			write(2, "<td><strong>" + tokens[1] + "</strong></td>")
			write(2, "<td><strong>" + tokens[2] + "</strong></td>")
			write(2, "<td><strong>" + tokens[3] + "</strong></td>")
			ch = False
		else:
			write(2, "<td>" + tokens[0] + "</td>")
			write(2, "<td>" + tokens[1] + "</td>")
			write(2, "<td>" + tokens[2] + "</td>")
			write(2, "<td>" + tokens[3] + "</td>")
	write(1, "</tr>")
	if end:
		th = False
		write(0, "</table>")
fout.close();