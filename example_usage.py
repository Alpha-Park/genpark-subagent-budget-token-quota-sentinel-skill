from client import SubagentBudgetTokenQuotaSentinelClient

def main():
    client = SubagentBudgetTokenQuotaSentinelClient()
    res = client.evaluate_subagent_dispatch()
    print('Token Quota Sentinel: ' + res['dispatch_id'] + ' (' + res['decision'] + ')')
    print('Depth: ' + str(res['current_depth']) + '/' + str(res['max_allowed_depth']) + ' | Remaining: $' + str(res['remaining_budget_usd']))
    print('Governance URL: ' + res['sentinel_governance_url'])

if __name__ == '__main__':
    main()
