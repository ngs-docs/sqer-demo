#
def sum_bp(record):
    return len(record.sequence)

def sum_bp_records(records):
  total = 0
  for record in records:
     total += sum_bp(record)

  return total
