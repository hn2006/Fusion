from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.conf import settings

def send_invitation_email(inv):
    """
    Send the initial invitation email to the professor with inline HTML.
    """
    thesis_title = inv.submission.thesis.research_theme
    accept_url = '' + reverse('procedures:invitation_action', args=[inv.token, 'accept'])
    reject_url = '' + reverse('procedures:invitation_action', args=[inv.token, 'reject'])
    expires_at = inv.expires_at.strftime('%Y-%m-%d') if inv.expires_at else None


    subject = f"Invitation to review: {thesis_title}"
    html = f"""
    <html>
      <body>
        <p>Dear {inv.prof_name},</p>
        <p>
          You are invited to review the thesis titled
          <strong>{thesis_title}</strong>.
        </p>
        <p>
          <a href="{accept_url}">Accept Review</a> |
          <a href="{reject_url}">Decline Review</a>
        </p>
        <p><small>This link expires on {expires_at} . Do not share it.</small></p>
      </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject,
        html,  # fallback to HTML in plain-text slot
        settings.DEFAULT_FROM_EMAIL,
        [inv.prof_email],
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()


def send_review_form_email(inv):
    """
    Send the review form link after the professor has accepted the invitation.
    """
    thesis_title = inv.thesis.title
    review_url = settings.SITE_URL + reverse('review_detail', args=[inv.token])

    subject = f"Review form: {thesis_title}"
    html = f"""
    <html>
      <body>
        <p>Dear {inv.prof_name},</p>
        <p>
          Thank you for accepting to review <strong>{thesis_title}</strong>.
          Please complete your review using the link below:
        </p>
        <p><a href="{review_url}">Fill Out Review Form</a></p>
        <p><small>Do not share this link; it is unique to you.</small></p>
      </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject,
        html,
        settings.DEFAULT_FROM_EMAIL,
        [inv.prof_email],
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()


def send_thank_you_email(inv):
    """
    Send a thank-you note once the professor submits their review.
    """
    thesis_title = inv.thesis.title

    subject = f"Thank you for reviewing: {thesis_title}"
    html = f"""
    <html>
      <body>
        <p>Dear {inv.prof_name},</p>
        <p>
          Thank you for completing your review of
          <strong>{thesis_title}</strong>. Your feedback is greatly appreciated.
        </p>
        <p>Best regards,<br/>The Thesis Committee</p>
      </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject,
        html,
        settings.DEFAULT_FROM_EMAIL,
        [inv.prof_email],
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()
