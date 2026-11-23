"""Authentication concepts develop into the concrete GitHub deployment path."""
from deckgen.layouts import section, statement, code_panel, content
import week09_layouts as L
import week11_figures as F
from week11_layouts import capture, github_details

OWASP = 'https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html'
OAUTH = 'https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps'
TEMPLATE = 'https://github.com/sd5913/github-oauth-d1-template'


def build():
    s = []
    s.append(section('01 / IDENTITY', 'Authentication', 'How does an application know who is asking?',
        notes='5-6 minutes. Build on Week 9 browser/server requests and Week 10 User, Conversation and Message rows. '
        'The database can identify a record, but last week the local operator selected a fictional profile. '
        'This week adds proof of the caller, then explains how that identity limits data access. '
        'The first half develops those ideas before opening deployment settings.'))
    s.append(L.diagram('A User row identifies a stored record.', F.local_identity(),
        '6-8 minutes. Read the left row: user 101 has the display name Ada. On the right any browser can submit '
        'user_id=101. The server has learned which record the browser requested, not who sent it. Ask whether '
        'changing the number to 202 should let Ada read Bo\'s conversation. Reuse the exact Week 10 ownership '
        'idea without repeating relational cardinality or rebuilding the handbook agent.'))
    s.append(L.compare('Authentication and authorization',
        ('Authentication', 'Who is making\nthis request?', 'Verify a credential or an existing session.'),
        ('Authorization', 'What may this\ncaller access?', 'Apply the rule to the requested resource.'),
        notes='8-10 minutes. A successful login establishes an identity for the application. Authorization checks '
        'what that identity may do: edit its own private note, read a public gallery, or administer a shared scene. '
        'A signed-in user can still be forbidden from another user\'s data. A public resource can deliberately '
        'allow anonymous access. These are separate decisions on the server, not properties of a visible button.',
        conclusion='A valid login does not grant access to every record.'))
    s.append(L.compare('Registration and login',
        ('Registration', 'Create the\naccount record.', 'Choose an identity and configure how to verify it.'),
        ('Login', 'Verify a returning\naccount holder.', 'Check the proof, then establish a session.'),
        notes='10-12 minutes. Restore the registration/login distinction from 2025 Week 10 slides39-43. '
        'A local password registration stores a password verifier with the account. Email validation can be '
        'another state of that record. External sign-in can create the local record on first use after the '
        'provider confirms an identity. Registration is not the action performed on every page refresh.'))
    s.append(L.rows('A credential supplies proof.', [
        ('Password', 'The person demonstrates knowledge of a secret.'),
        ('Passkey', 'A device signs a challenge with a private key.'),
        ('Session', 'The browser presents a previously issued credential.')],
        notes='12-14 minutes. A user name identifies an account; a credential supplies evidence that the caller '
        'may act as that account. A password can be guessed or stolen. A passkey uses public-key challenge '
        'verification; the private key is not sent to the server. A session credential is issued after login '
        'and can itself be stolen, so it also needs protection. MFA combines appropriate independent factors. '
        'Do not ask students to create a password database or memorize cryptographic algorithms today.'))
    s.append(L.compare('Hashing and encryption have different purposes.',
        ('Encryption', 'Recover the\noriginal value.', 'A key reverses the operation.'),
        ('Password hashing', 'Verify a\ncandidate value.', 'A slow one-way function makes guessing costly.'),
        notes='14-16 minutes. Encryption permits recovery with a key, useful for a private value the app must '
        'later display. Password verification needs to check a candidate, not recover the original password. '
        'A stolen hash can still be attacked by guessing candidates, so use a current password library with '
        'Argon2id or an appropriate supported alternative. A fast unsalted SHA-256 digest is unsuitable. '
        'Source checked 18 November2026 through Context7: ' + OWASP,
        conclusion='The database stores a password verifier.'))
    s.append(L.diagram('Registration stores a salted password hash.', F.registration(),
        '16-18 minutes. Follow the supplied password through the browser, protected HTTPS request, server '
        'and database record. The password library generates a random salt and runs a deliberately expensive '
        'password hashing algorithm. Store the result, salt and cost/algorithm parameters, commonly encoded '
        'together by the library, with the account. The salt is not a second secret. Neither logs nor the '
        'database should retain the submitted plaintext. This conceptual route explains login; our practical '
        'delegates account credentials to GitHub. Source: ' + OWASP))
    s.append(L.diagram('A salt separates otherwise identical passwords.', F.salts(),
        '18-20 minutes. Both invented users choose the same demonstration password. Distinct random salts '
        'produce different stored hashes. The illustrated hash A/hash B labels are schematic, not real encoded '
        'outputs. A salt prevents reusing one precomputed result across all accounts. It does not make a weak '
        'password unguessable or encrypt it. Modern password libraries normally manage salts and encoded '
        'parameters for the application. Source: ' + OWASP))
    s.append(L.diagram('Login verifies the candidate password.', F.password_login(),
        '20-22 minutes. The server finds the account\'s stored verifier and asks the password library to verify '
        'the submitted candidate. The library uses the stored salt and algorithm parameters, then compares '
        'safely. A match permits a new session. A mismatch rejects login. Explain why a user who forgets the '
        'password needs a verified reset rather than a service that emails the old password. The old 2025 '
        'unsalted example is historical, not the implementation to copy. Source: ' + OWASP))
    s.append(statement('Does the server need\nyour password\non every request?', size=103,
        notes='22-23 minutes. Give pairs twenty seconds to predict what happens when a logged-in user reloads '
        'a page. HTTP requests are separate exchanges. The application needs a way to link later requests '
        'to a successful login without resending the account password for every operation. Introduce sessions '
        'as the next mechanism, rather than treating a cookie as unexplained browser magic.'))
    s.append(L.diagram('A session connects later requests to a login.', F.session_cycle(),
        '23-25 minutes. After successful login the server issues a session cookie. The browser includes an '
        'applicable cookie on subsequent requests. The server verifies it before selecting private data. '
        'Cookies are one transport for session credentials, not a proof that any supplied content is true. '
        'A session ends by expiry, clearing the browser cookie, or server revocation if the design supports '
        'it. HTTPS protects transport. Source: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html'))
    s.append(L.compare('Two common session designs',
        ('Opaque session ID', 'Look up a random\nID on the server.', 'The server stores the session and can revoke it.'),
        ('Signed session data', 'Verify the data\nand its signature.', 'The template checks identity and expiry in a cookie.'),
        notes='25-27 minutes. Both designs require unpredictable or unforgeable credentials. An opaque ID '
        'points to server-held state. A signed payload carries fields the server can verify; signing detects '
        'changes and does not hide the fields. Our template uses the second design, not JWT-specific features '
        'or a D1 session table. Logout clears this browser\'s cookie. A copied valid cookie remains usable '
        'until expiry unless additional revocation is implemented. Template source: lib/session.ts.',
        conclusion='A signature protects integrity. Encryption protects confidentiality.'))
    s.append(code_panel('TEMPLATE / lib/session.ts', 'The session carries identity and expiry.', [
        '{', '  githubId: "101",', '  login: "ada",', '  kind: "session",', '  exp: expiresAt', '}'], lang='js',
        notes='27-28 minutes. This is a schematic object matching createSession, with invented identity and '
        'symbolic expiry. The server signs the serialized payload with SESSION_SECRET and verifies the '
        'signature, shape and expiry on each private request. HttpOnly limits page JavaScript access to the '
        'cookie. SameSite=Lax controls cross-site sending and Secure is enabled for production HTTPS. '
        'No password, access token or private note belongs in this readable payload.'))
    s.append(L.diagram('Authorization uses the verified user ID.', F.ownership(),
        '28-30 minutes. Reuse Week 10 foreign-key filtering. User101 reads notes.github_id=101; user202 reads '
        'its own row. The server takes githubId from the verified session, not from a user_id field supplied '
        'by the page. The real API accepts only a body string on POST. Ask whether hiding the Save button '
        'would protect another user\'s row from a direct HTTP request. It would not: the check belongs in '
        'the route and query. Source: template lib/handlers.ts.'))
    s.append(section('02 / GITHUB SIGN-IN', 'Delegated identity', 'Our app uses GitHub to identify the account holder.',
        notes='30-31 minutes. Move from the general theory to this application. GitHub already manages '
        'account credentials, login and additional checks. The user authorizes our OAuth App to obtain '
        'sufficient API access to identify them. OAuth is an access-delegation protocol. Our app uses that '
        'access to ask GitHub for the authenticated profile, then creates its own session.'))
    s.append(L.diagram('The browser returns with a temporary code.', F.oauth_code(),
        '31-33 minutes. Our login route creates random state, remembers it in a protected short-lived '
        'cookie and redirects the browser to GitHub. GitHub signs in the person and obtains authorization, '
        'then redirects to our configured callback with code and state. The Worker checks that the returned '
        'state belongs to the flow this browser started. A missing/mismatched/expired flow stops here. '
        'The app never sees the person\'s GitHub password. Source: ' + OAUTH))
    s.append(L.diagram('The Worker verifies the GitHub identity.', F.oauth_identity(),
        '33-35 minutes. The Worker exchanges code, client credential and PKCE verifier over HTTPS for an '
        'access token, then calls GET https://api.github.com/user. Validate the profile and use its numeric '
        'id as the stable owner key. GitHub login names can change. The template discards the token after '
        'this check and issues its own signed cookie. Separate browser redirects from server-to-server '
        'requests. GitHub recommends revalidating identity for each received access token. Source: ' + OAUTH))
    s.append(L.rows('Three values, three purposes', [
        ('State', 'Match the callback to this browser\'s login attempt.'),
        ('OAuth code', 'Exchange once for API access on the server.'),
        ('App session', 'Identify later requests to our application.')],
        notes='35-36 minutes. Have students trace which value exists before leaving our site, which comes '
        'back from GitHub, and which our own server creates afterward. The template also uses PKCE: a '
        'challenge goes in the authorization request and the server retains a verifier for the exchange. '
        'Do not confuse the GitHub access token, OAuth client secret, session-signing secret or Cloudflare '
        'deployment token. Each has a different audience and authority.'))
    s.append(L.diagram('The app runs in a Worker and stores notes in D1.', F.app_stack(),
        '36-38 minutes. The browser renders the page. Cloudflare Workers runs server routes; D1 stores '
        'notes across process restarts. GitHub holds source code and runs Actions jobs; it does not host '
        'this Worker just because the repository is there. Authentication establishes the owner, the query '
        'filters by that owner, and storage persists the body. Distinguish all three from a local fixture test.'))
    s.append(L.compare('Development and deployment use separate environments.',
        ('Local development', '127.0.0.1:3000', 'Local Worker, local D1 and ignored .dev.vars.'),
        ('Deployed application', 'Your HTTPS\nWorker origin', 'Remote Worker, remote D1 and runtime secrets.'),
        notes='38-39 minutes. Build on Week8\'s cloud development versus delivery distinction. A prepared '
        'coding workspace is not automatically a public application. Local and remote D1 have separate '
        'data and migrations. The OAuth callback must target the environment being used. Separate local '
        'and deployed OAuth Apps are a clear classroom option; current GitHub supports multiple callback '
        'URLs. The template selects its exact configured APP_URL and callback.',
        conclusion='The same source needs environment-specific configuration.'))
    s.append(capture('GitHub holds the application template.', 'github-template-overview.png',
        'Course template / actual repository capture, 18 November 2026',
        '39-40 minutes. Open the linked public template. Point out app, lib, migrations, tests and .github. '
        'The screenshot is an actual signed-out view: privileged controls are absent. Use the next slide '
        'to identify the signed-in template action. Students make a personal exercise copy; the public '
        'sd5913-owned group-project repository requirement remains separate.', TEMPLATE))
    s.append(capture('A template starts your own repository.', 'github-use-template.png',
        'Use this template > Create a new repository',
        '40-41 minutes. Actual GitHub Docs UI screenshot, retrieved 18 November 2026, CC BY 4.0. Sign in, '
        'open the course template and choose Use this template then Create a new repository. Select your '
        'personal owner and an exercise name. This starts a new history, unlike a fork. The documentation '
        'screenshot illustrates the control; it is not a newly created classroom deployment. Source: '
        'https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template'))
    s.append(L.rows('The OAuth App must know the return address.', [
        ('Personal Settings', 'Developer settings > OAuth Apps > New OAuth App'),
        ('Homepage', 'The application\'s APP_URL for this environment.'),
        ('Callback', 'APP_URL + /api/auth/github/callback')],
        notes='41-42 minutes. Open https://github.com/settings/applications/new in the real browser if '
        'demonstrating with a teaching copy. This is a personal OAuth App, not an installable GitHub App. '
        'The local origin is http://127.0.0.1:3000. Deployed APP_URL is the Worker\'s HTTPS origin without '
        'a trailing slash. Enter public registration information and put credentials directly into ignored '
        'local config or repository secrets. Do not project credential values. Source: '
        'https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app'))
    s.append(capture('Deployment values belong in repository Secrets.', 'github-secrets.png',
        'Repository Settings > Secrets and variables > Actions > Secrets',
        '42-43 minutes. Actual GitHub Docs screenshot retrieved 18 November 2026, CC BY 4.0. Navigate in '
        'the exercise repository, choose New repository secret, enter the exact name and value, then Add '
        'secret. Values are not displayed on these slides. The template uses this one location for all '
        'eight setup values, although some are public identifiers. Fork PRs do not receive these secrets. '
        'Source: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets'))
    s.append(L.rows('Cloudflare values select the deployment target.', [
        ('Account', 'CLOUDFLARE_ACCOUNT_ID'),
        ('Resources', 'CLOUDFLARE_WORKER_NAME\nCLOUDFLARE_D1_DATABASE_ID'),
        ('Permission', 'CLOUDFLARE_API_TOKEN')],
        notes='43-44 minutes. The student prepares a Worker name and D1 database in their own Cloudflare '
        'account using the template README. IDs identify resources; the API token authorizes deployment. '
        'Use the documented required Workers/D1 permissions. The runtime binding is DB. The deployment '
        'token belongs to the Actions job, not to the page or app user. Do not imply these identifiers '
        'are created by entering a GitHub secret.'))
    s.append(L.rows('Application values configure sign-in.', [
        ('Origin', 'APP_URL'),
        ('OAuth App', 'OAUTH_CLIENT_ID\nOAUTH_CLIENT_SECRET'),
        ('Our session', 'SESSION_SECRET')],
        notes='44-45 minutes. These complete the eight exact repository secret names. GitHub reserves '
        'the GITHUB_ prefix for repository secrets, so the workflow uses OAUTH_CLIENT_ID and '
        'OAUTH_CLIENT_SECRET. Its deployment script maps them to Worker runtime GITHUB_CLIENT_ID and '
        'GITHUB_CLIENT_SECRET. SESSION_SECRET signs the app session and is separate from every other '
        'credential. Full names and preparation belong in the tutorial, not a memorization test.'))
    s.append(L.diagram('Actions transfers secrets to the running Worker.', F.credential_transfer(),
        '45-46 minutes. The repository secret becomes an environment value in a job. The deploy script '
        'writes the three runtime values to an unlogged temporary file; Wrangler deploy --secrets-file '
        'installs them with the Worker. APP_URL and DB configuration have separate roles. A secret stored '
        'in GitHub does not automatically become a runtime binding. Source: '
        'https://developers.cloudflare.com/workers/configuration/secrets/#upload-secrets-alongside-code'))
    s.append(capture('The workflow file defines when deployment runs.', 'github-deploy-trigger.png',
        '.github/workflows/deploy.yml / push to main or manual workflow_dispatch',
        '46-47 minutes. Actual template source capture at 69cbed7,18 November 2026. Point to the on block '
        'and configuration job, then open the linked source to follow the deploy job. This workflow '
        'checks configuration before applying remote migrations and deploying. A PR runs credential-free '
        'checks. Merging into main can trigger a real deployment, so that decision follows human review. '
        'Source: ' + TEMPLATE + '/blob/69cbed7363412daa4a7e8c2c8fc4ed02a3f1afa5/.github/workflows/deploy.yml'))
    s.append(github_details('Actions shows the workflow and its runs.',
        'github-workflow-selection.png', 'github-workflow-run.png',
        'Select the workflow; open its run and jobs.\nA green run can include a skipped deploy.',
        '47-48 minutes. Open Actions and select Deploy to Cloudflare in the sidebar. The list shows the '
        'run, branch and commit. A successful run can still contain a skipped deployment; open the run '
        'and inspect jobs. In this public template production credentials are absent, so configuration '
        'succeeds and deployment skips. The screenshot does not claim a live Worker. Use your configured '
        'exercise copy for actual deployment. Source: ' + TEMPLATE + '/actions/workflows/deploy.yml', wide=True))
    s.append(capture('Run workflow starts the manual path.', 'github-run-workflow.png',
        'Choose the intended branch, then Run workflow in your configured copy.',
        '48-49 minutes. Actual GitHub Docs control screenshot retrieved 18 November 2026, CC BY 4.0. It '
        'shows an illustrative Browser Tests workflow, not our deployment. In our copy select Deploy to '
        'Cloudflare first. workflow_dispatch must exist on the default branch for this button. Review '
        'the selected branch, start once, then open the jobs and logs. This authoring session does not '
        'press the button or deploy. Source: https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow'))
    s.append(L.steps('Build, migrate and deploy change different things.', [
        ('Build', 'Create the application artifact.'),
        ('Migrate', 'Prepare the remote D1 schema.'),
        ('Deploy', 'Install code and runtime configuration.')],
        notes='49-51 minutes. Trace the template deploy job: npm ci, tests/typecheck, build, local '
        'checks/audit, remote migrations, deploy script. A green build does not prove a remote schema '
        'exists. A successful deployment does not prove callback configuration or two-account isolation. '
        'Inspect the current run and exact step on a failure, then test the URL. Worker startup is a '
        'different lifetime from a saved row. Source: template deploy.yml and README.'))
    s.append(github_details('A passing check describes the job that ran.',
        'github-check-summary.png', 'github-check-job.png',
        'Checks passed at 69cbed7.\nThis is CI evidence.\nLive sign-in needs\nits own acceptance check.',
        '51-52 minutes. Actual Checks run capture18 November 2026. Read the workflow name, commit, branch '
        'and job result. This proves that run\'s checks passed, not that a person signed in or a Worker '
        'was deployed. In a configured copy inspect deploy and its steps separately. The template\'s '
        'unconfigured deployment is intentionally skipped. Use these distinctions to diagnose what to '
        'inspect next, rather than treating every green badge as the same claim. Source: '
        + TEMPLATE + '/actions/runs/43684401618'))
    s.append(L.rows('The application check uses two accounts.', [
        ('Account A', 'Sign in, save a harmless note, reload and restart.'),
        ('Account B', 'A separate session sees only B\'s own note.'),
        ('Signed out', 'The private note API rejects the request.')],
        notes='52-54 minutes. Demonstrate on an already configured teaching copy if available. Preserve '
        'the same D1 state on restart. Use separate browser profiles and willing account holders; no '
        'shared passwords. A second user\'s save must leave A\'s note unchanged. Offline tests verify '
        'state/cookie/owner failure cases with labelled provider fixtures. They do not establish actual '
        'GitHub consent, Cloudflare permissions or classroom connectivity.'))
    s.append(statement('Which boundary failed:\nidentity, permission,\nor deployment?', size=98,
        notes='54-55 minutes. Ask three quick diagnosis questions. Callback mismatch: identity-flow '
        'configuration. B sees A\'s note: server authorization. No such table after deploy: remote database '
        'migration/binding. Have students explain why rerunning every command or disabling checks would '
        'not diagnose these different problems. Stop at minute 55 and protect the full break.'))
    return s
