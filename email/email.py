import re


def fun(s):
   a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
   return(a)
    # return True if s is a valid email, else return False


def filter_mail(emails):
   return filter(fun, emails)


if __name__ == '__main__':
  n = int(input())
  emails = []
  for _ in range(n):
    emails.append(input())

  filtered_emails = filter_mail(emails)
  filtered_emails.sort()
  print
  filtered_emails


# def test():
#   assert filter_mail("gmao@fmfm.com") ==